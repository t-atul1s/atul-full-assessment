==> B4 balance API

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
.....                                                                    [100%]
5 passed in 0.14s
[32mPASS B4 balance API[0m
==> B5 node balance API

> b5-node-balance-api@1.0.0 test
> node --test tests/api.test.js

TAP version 13
# Subtest: B5 node balance API
    # Subtest: credits increase balance
    ok 1 - credits increase balance
      ---
      duration_ms: 8.838333
      type: 'test'
      ...
    # Subtest: rejects overdraft
    ok 2 - rejects overdraft
      ---
      duration_ms: 2.283583
      type: 'test'
      ...
    # Subtest: lists newest transactions first
    ok 3 - lists newest transactions first
      ---
      duration_ms: 2.711833
      type: 'test'
      ...
    1..3
ok 1 - B5 node balance API
  ---
  duration_ms: 14.486208
  type: 'suite'
  ...
1..1
# tests 3
# suites 1
# pass 3
# fail 0
# cancelled 0
# skipped 0
# todo 0
# duration_ms 79.590542
[32mPASS B5 node balance API[0m
==> B6 rust log counter

running 2 tests
..
test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

[32mPASS B6 rust log counter[0m
==> I4 currency API

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
....                                                                     [100%]
4 passed in 0.14s
[32mPASS I4 currency API[0m
==> I6 bugfix

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
....                                                                     [100%]
4 passed in 0.02s
[32mPASS I6 bugfix[0m
==> I3 mini change

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
..                                                                       [100%]
2 passed in 0.13s
[32mPASS I3 mini change[0m
==> A3 fraud ingest API

[notice] A new release of pip is available: 25.3 -> 26.1.2
[notice] To update, run: pip install --upgrade pip
.                                                                        [100%]
1 passed in 0.12s
[32mPASS A3 fraud ingest API[0m
==> A3 fraud scorer
warning: type `Event` is more private than the item `score_event`
  --> src/main.rs:19:1
   |
19 | pub fn score_event(ev: &Event) -> Score {
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ function `score_event` is reachable at visibility `pub`
   |
note: but type `Event` is only usable at visibility `pub(crate)`
  --> src/main.rs:4:1
   |
 4 | struct Event {
   | ^^^^^^^^^^^^
   = note: `#[warn(private_interfaces)]` on by default

warning: type `Score` is more private than the item `score_event`
  --> src/main.rs:19:1
   |
19 | pub fn score_event(ev: &Event) -> Score {
   | ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ function `score_event` is reachable at visibility `pub`
   |
note: but type `Score` is only usable at visibility `pub(crate)`
  --> src/main.rs:12:1
   |
12 | struct Score {
   | ^^^^^^^^^^^^

warning: field `account_id` is never read
 --> src/main.rs:6:5
  |
4 | struct Event {
  |        ----- field in this struct
5 |     event_id: String,
6 |     account_id: String,
  |     ^^^^^^^^^^
  |
  = note: `Event` has a derived impl for the trait `Debug`, but this is intentionally ignored during dead code analysis
  = note: `#[warn(dead_code)]` (part of `#[warn(unused)]`) on by default


running 2 tests
..
test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

[32mPASS A3 fraud scorer[0m
==> A4 modernization
..                                                                       [100%]
2 passed in 0.03s
[32mPASS A4 modernization[0m
==> A6 perf bench
n=200000
naive=0.008462s fast=0.000001s speedup=7692.4x
[32mPASS A6 perf bench[0m
==> I5 dockerized API
[33mBLOCKED I5 dockerized API (docker not installed — config-only dry-run)[0m
==> D1 terraform
[33mBLOCKED D1 terraform (terraform not installed — config-only dry-run)[0m
==> D2 docker compose stack
[33mBLOCKED D2 docker compose stack (docker not installed — config-only dry-run)[0m
==> D4 k8s manifests
[33mBLOCKED D4 k8s manifests (kubectl not installed — config-only dry-run)[0m

Summary: pass=10 fail=0 skip=0 blocked=4
