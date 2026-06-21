import http from "node:http";

let balance = 0;
let seq = 1;
const ledger = [];

function json(res, status, body) {
  res.writeHead(status, { "Content-Type": "application/json" });
  res.end(JSON.stringify(body));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    let raw = "";
    req.on("data", (c) => (raw += c));
    req.on("end", () => {
      try {
        resolve(raw ? JSON.parse(raw) : {});
      } catch {
        reject(new Error("invalid json"));
      }
    });
  });
}

export function resetState() {
  balance = 0;
  seq = 1;
  ledger.length = 0;
}

export async function handler(req, res) {
  const url = new URL(req.url, "http://localhost");

  if (req.method === "GET" && url.pathname === "/balance") {
    return json(res, 200, { balance: Math.round(balance * 100) / 100 });
  }

  if (req.method === "GET" && url.pathname === "/transactions") {
    return json(res, 200, [...ledger].reverse());
  }

  if (req.method === "POST" && url.pathname === "/transactions") {
    let body;
    try {
      body = await readBody(req);
    } catch {
      return json(res, 400, { detail: "Invalid JSON" });
    }

    const { kind, amount, note } = body;
    if (!["credit", "debit"].includes(kind) || typeof amount !== "number" || amount <= 0) {
      return json(res, 422, { detail: "Validation failed" });
    }
    if (kind === "debit" && amount > balance) {
      return json(res, 400, { detail: "Insufficient funds" });
    }

    const tx = {
      id: seq++,
      kind,
      amount,
      note: note ?? null,
      at: new Date().toISOString(),
    };
    ledger.push(tx);
    balance += kind === "credit" ? amount : -amount;
    return json(res, 201, tx);
  }

  json(res, 404, { detail: "Not found" });
}

export function createServer() {
  return http.createServer((req, res) => {
    handler(req, res).catch(() => json(res, 500, { detail: "Internal error" }));
  });
}

if (import.meta.url === `file://${process.argv[1]}`) {
  createServer().listen(3000, () => console.log("B5 balance API on :3000"));
}
