import assert from "node:assert/strict";
import http from "node:http";
import { describe, it, beforeEach, afterEach } from "node:test";
import { createServer, resetState } from "../server.js";

function request(server, method, path, body) {
  return new Promise((resolve, reject) => {
    const port = server.address().port;
    const opts = {
      hostname: "127.0.0.1",
      port,
      path,
      method,
      headers: body ? { "Content-Type": "application/json" } : {},
    };
    const req = http.request(opts, (res) => {
      let data = "";
      res.on("data", (c) => (data += c));
      res.on("end", () => resolve({ status: res.statusCode, body: JSON.parse(data || "{}") }));
    });
    req.on("error", reject);
    req.end(body ? JSON.stringify(body) : undefined);
  });
}

describe("B5 node balance API", () => {
  let server;

  beforeEach(async () => {
    resetState();
    server = createServer();
    await new Promise((r) => server.listen(0, r));
  });

  afterEach(() => server.close());

  it("credits increase balance", async () => {
    const post = await request(server, "POST", "/transactions", { kind: "credit", amount: 80 });
    assert.equal(post.status, 201);
    const bal = await request(server, "GET", "/balance");
    assert.equal(bal.body.balance, 80);
  });

  it("rejects overdraft", async () => {
    await request(server, "POST", "/transactions", { kind: "credit", amount: 10 });
    const post = await request(server, "POST", "/transactions", { kind: "debit", amount: 99 });
    assert.equal(post.status, 400);
  });

  it("lists newest transactions first", async () => {
    await request(server, "POST", "/transactions", { kind: "credit", amount: 1 });
    await request(server, "POST", "/transactions", { kind: "credit", amount: 2 });
    const list = await request(server, "GET", "/transactions");
    assert.deepEqual(list.body.map((t) => t.amount), [2, 1]);
  });
});
