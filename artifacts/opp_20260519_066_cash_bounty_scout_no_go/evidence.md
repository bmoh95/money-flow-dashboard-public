# Cash bounty/direct-payout scout

검토 기준: actual bounty/open state, duplicate/competition PR, PR route, payout rail, participant constraints, user burden, approval/payment odds. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/920
   - 후보: UnsafeLabs #920 — CrossChainBridge replay protection, $900
   - 지급: GitHub labels show 💎 Bounty/$900 and comments use /opire try or /bounty try; platform-like route visible but payment comments include wallet/PayPal attempts.
   - preflight: Issue open, assignee 없음, PR endpoint available. 10 comments already, recent /opire try by Adamchaua plus other claim comments. Security/crypto bridge signature/EIP-712 scope requires correct replay-safe implementation and tests.
   - 결정: NO-GO / DUPLICATE — high-value but already contested, high-risk crypto security patch; wallet/payment-noise comments reduce safe automatic submission odds.

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/919
   - 후보: UnsafeLabs #919 — FlashLoan minimum fee/drainage protection, $250
   - 지급: GitHub labels show 💎 Bounty/$250 and /opire try comments indicate cash/platform-style route.
   - preflight: Issue open, assignee 없음. 10 comments; Abu1982, mkcash, Adamchaua already claiming/attempting. Acceptance covers fee math, max loan cap, rebasing-token accounting, pause/unpause, fee accrual, tests.
   - 결정: NO-GO / DUPLICATE — competition exists and acceptance spans security-sensitive Solidity behavior beyond safe quick micro-bounty.

3. https://github.com/UnsafeLabs/Bounty-Hunters/issues/917
   - 후보: UnsafeLabs #917 — TokenVesting overflow/revoke fixes, $350
   - 지급: GitHub labels show 💎 Bounty/$350 and /opire try comments indicate platform-style route.
   - preflight: Issue open, assignee 없음. 8 comments; multiple interest/claim comments. Requires overflow-safe vesting math, remainder correctness, cliff revoke fix, fuzz/boundary tests.
   - 결정: NO-GO / DUPLICATE — not rejected for amount; rejected because contested crypto/security math with high correctness risk.

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5
   - 후보: Claude Builders #5 — n8n weekly dev summary workflow, $200 Opire
   - 지급: Issue body says $200 powered by Opire, /opire try, PR with workflow+README, payment released on merge.
   - preflight: Issue open, assignee 없음. 301 comments and many attempts. Acceptance requires real n8n instance, Claude API call/screenshot, destination webhook/email docs, EN/FR variables.
   - 결정: NO-GO / HIGH_USER_INPUT — payout clear but requires external API/service setup and crowded subjective workflow review.

5. https://github.com/ubiquity/business-development/issues/90
   - 후보: Ubiquity #90 — GitHub Based Marketing, $200 label
   - 지급: Issue labels include Price: 200 USD, but UbiquityOS bot controls assignment/start.
   - preflight: Issue open, assignee 없음. Bot response says “must be a core team member, or an administrator to start this task”; existing detailed submission comment and open PRs #202/#203.
   - 결정: NO-GO / HIGH_USER_INPUT — participant eligibility fails before coding; core-team/admin requirement blocks automatic work.

6. https://github.com/sindresorhus/fkill-cli/issues/6
   - 후보: fkill-cli #6 — Smart mode, $40 IssueHunt
   - 지급: IssueHunt badge/bot says $40 funded and submit via IssueHunt.
   - preflight: Issue open, assignee 없음, but issue is old and current maintainer comment points to unresolved UX direction. Open PRs #90/#91 exist. Claim/payment likely requires IssueHunt account/profile.
   - 결정: NO-GO / NO_CHANNEL — funded but PR/acceptance path is stale/ambiguous, competing PRs exist, and IssueHunt payout account would add user burden.

7. https://github.com/prest/prest/issues/284
   - 후보: prest #284 — mock adapter documentation, $20 IssueHunt
   - 지급: IssueHunt badge says $20 funded; issue body lists submitted pull requests.
   - preflight: Issue open, assignee 없음. Issue body already lists submitted PRs #962/#963/#964/#965, and GitHub shows many open PRs.
   - 결정: NO-GO / DUPLICATE — small docs bounty fits micro-bounty preference, but direct duplicate PRs already exist; approval/payment odds poor.

결론: 7건 모두 자동 구현·댓글·claim·PR 제출 기준 미달. 낮은 금액 때문이 아니라 중복/참여자격/외부계정/고위험 보안 범위 때문에 정지.
