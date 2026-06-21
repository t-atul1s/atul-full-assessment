#!/usr/bin/env node
/** I4 — Node CLI client for currency convert API */
import http from "node:http";

const API = process.env.CONVERT_API ?? "http://127.0.0.1:8000";

function parseArgs(argv) {
  const out = {};
  for (let i = 2; i < argv.length; i += 2) {
    const key = argv[i].replace(/^--/, "");
    out[key] = argv[i + 1];
  }
  return out;
}

function postConvert(payload) {
  const url = new URL("/convert", API);
  const body = JSON.stringify(payload);
  return new Promise((resolve, reject) => {
    const req = http.request(
      url,
      { method: "POST", headers: { "Content-Type": "application/json", "Content-Length": Buffer.byteLength(body) } },
      (res) => {
        let data = "";
        res.on("data", (c) => (data += c));
        res.on("end", () => {
          const parsed = JSON.parse(data);
          if (res.statusCode >= 400) reject(new Error(parsed.detail ?? data));
          else resolve(parsed);
        });
      },
    );
    req.on("error", reject);
    req.write(body);
    req.end();
  });
}

async function main() {
  const { amount, source, target } = parseArgs(process.argv);
  if (!amount || !source || !target) {
    console.error("Usage: node cli.js --amount 100 --source USD --target INR");
    process.exit(1);
  }
  const result = await postConvert({ amount: Number(amount), source, target });
  console.log(`${result.amount} ${result.source} -> ${result.result} ${result.target} (rate ${result.rate})`);
}

main().catch((e) => {
  console.error(e.message);
  process.exit(1);
});
