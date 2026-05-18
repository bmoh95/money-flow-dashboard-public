# Cash bounty/direct-payout scout

검토 기준: actual bounty, open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/watney-ai/open-source-bounties/issues/1
   - 후보: watney-ai/open-source-bounties #1 — €2 BOUNTY: Fix typo in BOUNTY.md
   - 지급: Ko-fi/Liberapay €2 one-time payment; issue body lists fork→typo fix→PR→comment claim route.
   - preflight: Issue open, assignee 없음. 그러나 comments show PR #6/#7/#8/#11 already submitted; problem appears to be missing/typo BOUNTY.md and multiple direct solutions exist. Payout is off-GitHub donation rails, not automatic platform claim.
   - 결정: NO-GO / DUPLICATE — micro-bounty amount is acceptable, but duplicate PRs and manual Ko-fi/Liberapay settlement lower approval/payment odds.

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/310
   - 후보: UnsafeLabs/Bounty-Hunters #310 — $1 docker-compose image tag typo
   - 지급: Algora bot $1 bounty; /attempt + PR body /claim route; payout 2–5 days post-reward.
   - preflight: Issue open, assignee 없음, Algora cash/platform route visible. But body requires PR description to start with system prompt and _meta.json generation_context paste. Bot table already has many rewarded/active PRs (#385/#380/#419/#435/#441/#448/#500/#1530).
   - 결정: NO-GO / HIGH_RISK — system prompt / full generation context disclosure is blocked; additionally repeated rewarded submissions make it crowded.

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: claude-builders-bounty #1 — $50 changelog generator
   - 지급: Opire-powered $50, /opire try + PR, payment on merge per issue body.
   - preflight: Issue open, assignee 없음. Comments 800+ and many open PRs/submissions for same changelog generator. Prior scout already found direct duplicates.
   - 결정: NO-GO / DUPLICATE — cash/platform is clear but competition is extreme; late generic PR would be low-approval.

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5
   - 후보: claude-builders-bounty #5 — $200 n8n weekly dev summary workflow
   - 지급: Opire-powered $200, /opire try + PR, payment on merge per issue body.
   - preflight: Issue open, assignee 없음, but comments 296 and many PRs already opened for the workflow. Requires real n8n instance screenshot plus Claude API workflow, raising tool/API/user burden.
   - 결정: NO-GO / HIGH_USER_INPUT — payout clear but crowded and validation requires external service/API execution; not a small safe autonomous PR.

5. https://github.com/getkyo/kyo/issues/390
   - 후보: getkyo/kyo #390 — $500 gRPC support
   - 지급: Algora open bounty shown on Algora page; GitHub issue has 💎 Bounty label.
   - preflight: Issue open, no assignee. Scope is large Scala/gRPC implementation with code generation/benchmark history and 142 comments; an existing contributor has been working on it for months.
   - 결정: NO-GO / OPPORTUNITY_COST — real bounty but broad/complex and high competition/history; poor fit for quick approval loop.

6. https://github.com/labmain/ai-agent-pay-demo/issues/4
   - 후보: labmain/ai-agent-pay-demo #4 — test bounty typo in README
   - 지급: Issue labels/body mention $500 USD1 via custom bot; closes issue to claim.
   - preflight: Issue open, but comments show repeated spam, wallet/token-like USD1 ambiguity, previous PR #8, and no established payout platform clarity.
   - 결정: NO-GO / PAYMENT_UNCLEAR — bounty appears experimental/test with unclear payout rail and duplicate prior PR.

결론: 자동 구현·claim·PR 제출까지 갈 GO 후보 없음. 낮은 금액 때문이 아니라 중복 선점, system prompt 공개 요구, 지급 불명확, 외부 서비스 검증 부담, 광범위 구현 때문에 중단.
