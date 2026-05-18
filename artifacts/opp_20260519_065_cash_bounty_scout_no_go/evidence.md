# Cash/platform bounty scout

범위: GitHub/Algora/Opire/IssueHunt/Expensify direct-payout 우선. 블로그/content fallback 없음.
검토 기준: 실제 bounty, open 상태, 중복/경쟁 PR, PR route, payout rail, 참여자격, 외부 서비스/지갑/개인정보 부담, 승인 가능성.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/758
   - 후보: UnsafeLabs #758 — FastAPI OAuth2 refresh support, $150 Algora
   - 지급: A: Algora bot comment says $150 bounty, /attempt #758 then PR body /claim #758.
   - preflight: Open, no assignee, PR route exists. Existing open PRs #1522 and #1580, plus multiple closed PRs (#1190/#894/#986/#1074). Recent commenter withdrew because provenance/config snapshot requirements and prior work make safe submission weak.
   - 결정: NO-GO / DUPLICATE — cash/platform route clear, but duplicate/open PR competition makes approval odds poor.

2. https://github.com/SecureBananaLabs/bug-bounty/issues/30
   - 후보: SecureBananaLabs #30 — API benchmark suite, $750 label
   - 지급: B: issue labels show bug bounty/💎 Bounty/$750, but repo-specific payout/claim rail is less clear than Algora/Opire.
   - preflight: Open, no assignee, but at least 10 open PRs mention #30. Acceptance requires all /api endpoints, realistic payloads, auth benchmark token, CI/reporting; high project-specific setup burden.
   - 결정: NO-GO / DUPLICATE — many active competing PRs and broad benchmark scope; not a quick safe micro-bounty.

3. https://github.com/SecureBananaLabs/bug-bounty/issues/80
   - 후보: SecureBananaLabs #80 — original pixel art, $780 label
   - 지급: B: issue labels show bug bounty/💎 Bounty/$780, but payment route appears repo-specific and comments include wallet-style claims.
   - preflight: Open, no assignee, but 10+ open PRs already submit pixel art for #80. Creative asset bounty with subjective approval and possible wallet/payment disclosure comments.
   - 결정: NO-GO / DUPLICATE — scope is easy but heavily saturated and payout/profile route is not safely cash/platform-confirmed.

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
   - 후보: Claude Builders #3 — destructive bash pre-tool hook, $100 Opire
   - 지급: A: issue body says $100 powered by Opire; expected flow /opire try + PR.
   - preflight: Open, no assignee, but 519 comments and many open PRs (#1602/#956/#702/#381/#755/#1202/#1145/#1071/#791/#770). Security hook scope is crowded and overrepresented.
   - 결정: NO-GO / DUPLICATE — payout is clear, but extreme competition/duplicate risk blocks automatic PR.

5. https://github.com/algora-io/algora/issues/238
   - 후보: Algora #238 — hide unauthorized edit/delete buttons on bounty page
   - 지급: B: found by Algora/bounty search, but issue itself has no visible bounty amount or current payout terms in checked body/comments.
   - preflight: Open, no assignee, but at least 9 open PRs already fix #238. UI reproduction requires Algora login/state; duplicate proposal/comments already present.
   - 결정: NO-GO / PAYMENT_UNCLEAR — payout unclear and active duplicate PRs make it unsuitable.

6. https://github.com/sindresorhus/awesome-lint/issues/37
   - 후보: awesome-lint #37 — header image lint rule, $60 IssueHunt
   - 지급: A: IssueHunt badge says $60 funded and bot says submit PR via IssueHunt.
   - preflight: Open, no assignee. However PR endpoint for upstream returned 404/disabled via checked route, open PR #225 exists, and multiple commenters already prepared compare branches. IssueHunt likely requires account/claim path.
   - 결정: NO-GO / NO_CHANNEL — funding exists but contribution/claim route is blocked/unclear and work is already contested.

7. https://github.com/Expensify/App/issues/90985
   - 후보: Expensify #90985 — narrow-screen workspace navigation flash, $250
   - 지급: A/B: title has $250 and Expensify External/Help Wanted labels; paid contributor flow exists.
   - preflight: Open but assignee eVoloshchak present. Comments show existing proposals, ProposalPolice duplicate withdrawals, and contributor onboarding requires email/Slack plus Upwork profile. No PR yet but eligibility/user-input burden is high.
   - 결정: NO-GO / HIGH_USER_INPUT — cash task but assigned and requires personal contributor/Upwork onboarding; not automatic.

결론: 이번 7건은 모두 지급 경로/참여조건/중복PR/외부계정 부담 중 하나가 막혀 자동 구현·claim·PR 기준 미달.
