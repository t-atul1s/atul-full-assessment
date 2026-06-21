/** Poll pending events, score via Rust CLI, PATCH results back. */
import { spawnSync } from "node:child_process";
import http from "node:http";

const API = process.env.FRAUD_API ?? "http://127.0.0.1:8001";
const SCORER = process.env.SCORER_BIN ?? "../scorer/target/debug/fraud-scorer";

function request(method, path, body) {
  const url = new URL(path, API);
  const payload = body ? JSON.stringify(body) : null;
  return new Promise((resolve, reject) => {
    const req = http.request(
      url,
      {
        method,
        headers: payload ? { "Content-Type": "application/json", "Content-Length": Buffer.byteLength(payload) } : {},
      },
      (res) => {
        let data = "";
        res.on("data", (c) => (data += c));
        res.on("end", () => resolve({ status: res.statusCode, body: data ? JSON.parse(data) : null }));
      },
    );
    req.on("error", reject);
    if (payload) req.write(payload);
    req.end();
  });
}

export async function pollOnce() {
  const pending = await request("GET", "/events?state=pending");
  if (!Array.isArray(pending.body)) return 0;
  let scored = 0;
  for (const ev of pending.body) {
    const input = JSON.stringify({
      event_id: ev.event_id,
      account_id: ev.account_id,
      value: ev.value,
      channel: ev.channel,
    });
    const run = spawnSync(SCORER, [], { input, encoding: "utf8" });
    if (run.status !== 0) continue;
    const result = JSON.parse(run.stdout);
    await request("PATCH", `/events/${ev.event_id}/score`, {
      event_id: ev.event_id,
      score: result.score,
      band: result.band,
      flags: result.flags,
    });
    scored += 1;
  }
  return scored;
}

if (import.meta.url === `file://${process.argv[1]}`) {
  pollOnce().then((n) => console.log(`scored ${n} event(s)`));
}
