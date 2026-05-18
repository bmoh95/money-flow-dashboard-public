# Cash bounty/direct-payout scout

검토 기준: actual bounty, open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/827
   - 후보: UnsafeLabs #827 — T3 Code contracts schema round-trip tests, $25 Algora
   - 지급: Algora bot posts $25 bounty; PR body must include /claim #827; cash/platform route visible.
   - preflight: Issue open, assignee 없음, PR route exists, labels good first/AI Agent friendly. Comments include two attempts but no open PR found by #827 search. Acceptance requires every exported Schema type in contracts, .audit.json, PR title agent name + [ T3 Code]. Scope is larger than quick safe patch because contracts exports are numerous across auth/git/ipc/orchestration/provider/runtime/settings.
   - 결정: HOLD / OPPORTUNITY_COST — closest candidate, payout/route clear and competition moderate, but “every exported Schema type” makes implementation too broad for this cron window without risking incomplete bounty PR.

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/792
   - 후보: UnsafeLabs #792 — Laravel global scope/user observer/UUID, $110 Algora
   - 지급: Algora bot posts $110 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Comments include zp6 PR, cerredz /attempt, mkcash /bounty try. Requires migration, observer, scope, lazy-loading behavior and tests in Laravel app.
   - 결정: NO-GO / DUPLICATE — clear payout, but already contested/submitted and not a small micro-doc/test patch.

3. https://github.com/UnsafeLabs/Bounty-Hunters/issues/749
   - 후보: UnsafeLabs #749 — Laravel rate limiting/session fallback, $120 Algora
   - 지급: Algora bot posts $120 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Comments include existing PR/submission and multiple attempts. Acceptance includes 429 behavior, fallback session driver, debug route, tests.
   - 결정: NO-GO / DUPLICATE — direct competition and behavior/test scope make approval odds weak.

4. https://github.com/UnsafeLabs/Bounty-Hunters/issues/818
   - 후보: UnsafeLabs #818 — T3 orchestration fiber interruption checkpointing, $120 Algora
   - 지급: Algora bot posts $120 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Maintainer/comment notes PR #1479 already submitted/complete; multiple attempts. Touches interruption/checkpoint behavior.
   - 결정: NO-GO / DUPLICATE — existing completed PR noted by commenter; duplicate/high-risk state logic.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/864
   - 후보: UnsafeLabs #864 — Electron t3code:// deep linking, $100 Algora
   - 지급: Algora bot posts $100 bounty and /attempt + /claim flow.
   - preflight: Issue open, assignee 없음. Multiple attempts plus existing PR references/claims. Requires Electron protocol handler, IPC routing, cold-start behavior, path traversal validation.
   - 결정: NO-GO / DUPLICATE — directly contested and platform-specific verification burden too high.

6. https://github.com/velodrome-finance/indexer/issues/738
   - 후보: Velodrome #738 — doc note for legacy $0 totalEmissionsUSD
   - 지급: No visible bounty amount/claim route in issue body; ready-for-agent label only.
   - preflight: Issue open, assignee 없음. Open PR #739 already addresses #738 exactly. Payout unclear.
   - 결정: NO-GO / PAYMENT_UNCLEAR — not a verified bounty and already has direct PR.

7. https://github.com/sindresorhus/macos-wallpaper/issues/25
   - 후보: IssueHunt #25 — macos-wallpaper multi-screen get bug, $60
   - 지급: IssueHunt bot says $60 open bounty; submit via IssueHunt.
   - preflight: Issue open, assignee 없음. Issue is from Mojave-era discussion; maintainer suspected macOS behavior; repo PR API unavailable/archived-like check failed. Requires old macOS multi-monitor reproduction.
   - 결정: NO-GO / HIGH_USER_INPUT — payout visible, but reproduction requires specific old macOS/display setup and PR route check failed.

결론: #827은 지급/경쟁 면에서 가장 가까웠지만 acceptance가 contracts 전체 exported Schema coverage라 불완전 PR 위험이 높아 HOLD. 나머지는 중복 PR·지급 불명확·외부 재현 부담으로 자동 구현/댓글/PR 제출 기준 미달.
