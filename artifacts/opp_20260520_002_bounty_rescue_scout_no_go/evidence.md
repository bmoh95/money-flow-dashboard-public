# Bounty rescue scout: no eligible cash PR after retry

- Run: `2026-05-20_0137_money-flow`
- Checked: 2026-05-20T01:51:16+09:00
- Final filter: 78 candidates, hard excluded share 0.077, warnings none
- Deep preflight: 18 candidates

## Candidate outcomes
- **NO-GO / HIGH_USER_INPUT** [devpool mirror: Opire / Ubiquity business-development#89](https://github.com/devpool-directory/devpool-directory/issues/5030) — Price 400 USD label exists, but linked Ubiquity issue has repeated bot warnings: core-team/admin required to start; many closed PRs/comments. Not eligible for automatic PR.
- **NO-GO / DUPLICATE** [devpool mirror: Nomic Embeddings +10% Accuracy](https://github.com/devpool-directory/devpool-directory/issues/5064) — Price 900 USD label exists, but linked text-vector issue already has claimed/open PR #155 and follow-up comments. No superior small diff path.
- **NO-GO / HIGH_USER_INPUT** [Hugin Messenger translation bounty](https://github.com/kryptokrona/hugin-native/issues/13) — Pays $20 worth of XKR and asks for an XKR address; wallet/address is L4. Also rejects AI-generated translation and already has several open translation PRs.
- **NO-GO / HIGH_RISK** [Glowstone 1.13-board Bountysource set](https://github.com/GlowstoneMC/1.13-board/issues/20) — Issues #20/#22/#25/#26/#30 are old Bountysource items. Maintainer explicitly says AI PRs are not accepted for clean-room legal reasons; several recent claimed/closed PRs exist.
- **NO-GO / PAYMENT_UNCLEAR** [Invoice Scope Google SSO / Opire plugin](https://github.com/crisesarmiento/invoice-scope/issues/28) — Opire bot confirms the issue has no reward yet. Existing open PR activity is unrelated; no funded claim route.
- **NO-GO / DUPLICATE** [Bountysource spam reporting](https://github.com/bountysource/core/issues/1148) — $100 Bountysource issue, but repo is stale and has multiple active open PRs (#1600/#1605/#1606/#1351) for the same spam-reporting scope.
- **NO-GO / PAYMENT_UNCLEAR** [Invidious listen-mode quality labels](https://github.com/iv-org/invidious/issues/2513) — $10 bounty is BTC-only per project comment, so wallet/address flow is blocked. Multiple open/closed PRs already target the same UI label fix.
- **NO-GO / DUPLICATE** [IssueHunt $4 prefixed workspace config](https://github.com/Kreyren/git-workspace/issues/1) — IssueHunt $4 route exists, but open PRs #2/#3 already implement the exact prefixed config behavior. No duplicate PR.
- **NO-GO / DUPLICATE** [LimeText undo stack regions](https://github.com/limetext/backend/issues/101) — $15 Bountysource route exists, but open PRs #131/#132 already add the region undo behavior and regression coverage.
- **NO-GO / HIGH_USER_INPUT** [LiveHelperChat Telegram bot text actions](https://github.com/LiveHelperChat/livehelperchat/issues/1505) — Bounty label/IssueHunt URL exists, but issue is assigned to maintainer remdex and has /attempt activity. Scope is integration work, not an unclaimed micro-fix.
- **NO-GO / NO_EVIDENCE** [k3d --platform support](https://github.com/k3d-io/k3d/issues/1602) — Issue only contains a sponsor-if-urgent IssueHunt link; no funded bounty amount. Existing PR #1603 already covers platform support.
- **NO-GO / NO_EVIDENCE** [k3d Windows kubeconfig host.docker.internal bug](https://github.com/k3d-io/k3d/issues/1574) — Issue only has a generic IssueHunt sponsor link and no funded amount/claim path. Not a direct-payout bounty candidate.
- **NO-GO / DUPLICATE** [Algora official page: Zed replace mode](https://github.com/zed-industries/zed/issues/4440) — Issue is closed and $500 Algora bounty was already awarded in 2024. Not current.
- **NO-GO / HIGH_RISK** [Algora official page: PX4 collision prevention](https://github.com/PX4/PX4-Autopilot/issues/22464) — Issue is closed; autopilot collision-prevention rewrite is broad/safety-sensitive with previous closed PRs. Not an automatic bounty task.
- **NO-GO / DUPLICATE** [Algora official page: Archestra granular budgeting](https://github.com/archestra-ai/archestra/issues/3603) — Closed/rewarded $150 bounty with assigned contributors and closed PRs. Not current.
- **NO-GO / DUPLICATE** [Algora official page: Archestra agent import/export](https://github.com/archestra-ai/archestra/issues/4201) — Closed/rewarded $50 bounty with assigned contributor and closed PRs. Not current.
- **NO-GO / NO_EVIDENCE** [IssueHunt query false positive: awesome-ai-money-tools suggestion](https://github.com/yiweichen10/awesome-ai-money-tools/issues/1) — Directory-submission request mentioning bounty platforms, not a payer-backed bounty.
- **NO-GO / NO_CHANNEL** [IssueHunt support request 401](https://github.com/BoostIO/issuehunt-requests/issues/27) — Platform support/auth mapping request for another user; no PR/funded task route and would involve account support.
