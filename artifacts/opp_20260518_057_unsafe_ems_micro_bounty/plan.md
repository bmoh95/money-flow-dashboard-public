# Plan — UnsafeLabs #573 EMS $1 micro-bounty

- Scope: `python/tls_handshake.py`의 EMS master secret derivation만 수정.
- Acceptance: EMS negotiated branch uses `b"extended master secret"` and session hash seed; non-EMS remains `b"master secret"` with client/server random seed.
- Submission: `/attempt #573`, fork branch, PR body includes `/claim #573`.
- Verification: `py_compile`, focused pytest 2 cases, GitHub checks.
- Out of scope: unrelated TLS bugs, security audit metadata prompt disclosure, broad refactor.
