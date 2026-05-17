# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/RFC-5322/issues/1
   - 근거(A): $400 Algora label and issue open; repo PR endpoint works and open PR count was 0. Reject: CONTRIBUTING says bounties are symbolic/not paid work, humans not allowed, CAP block asks for full init context; scope is full RFC 5322 parser from scratch with no code skeleton/tests.
   - 결정: NO-GO / HIGH_RISK

2. https://github.com/ClankerNation/OpenAgents/issues/136
   - 근거(A): $1k bounty issue open with PR route, but repo had ~30 open PRs and existing attempt PR #252 referenced. Issue requires contributor traceability block with complete pre-session instructions; payment comment uses BTC/wallet. Reject for competition, wallet rail, and secret/prompt disclosure risk.
   - 결정: NO-GO / HIGH_RISK

3. https://github.com/ClankerNation/OpenAgents/issues/133
   - 근거(A): $8k bounty issue open, but ~30 open PRs, multiple attempts, and required file header demands complete raw startup instructions. Existing comments include BTC wallet payment. Reject despite high nominal amount because approval/payment and security risk are unacceptable.
   - 결정: NO-GO / HIGH_RISK

4. https://github.com/UnsafeLabs/Bounty-Hunters/issues/829
   - 근거(A): $500 Algora bot bounty, issue open, but already has multiple /attempt or /opire try comments and repo had ~30 open PRs. Target project path is nested T3 Code with Effect retry/auth state complexity; approval odds too low now.
   - 결정: NO-GO / OPPORTUNITY_COST

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/826
   - 근거(A): $300 Algora bot bounty, issue open, but comments link submitted PR #12 and additional attempts. Repo had ~30 open PRs. Reject as likely already contested/claimed.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/UnsafeLabs/Bounty-Hunters/issues/804
   - 근거(A): $200 Algora bot bounty, issue open, but comments link submitted PR #4, /opire try, and another /attempt. Repo had ~30 open PRs. Reject as crowded and low EV.
   - 결정: NO-GO / DUPLICATE

7. https://github.com/Reqrefusion/FreeCAD-Documentation-Project/issues/25
   - 근거(B): Bounty/Reward labels and open issue; payer/channel unclear, amount absent, repo had ~30 open PRs, and maintainer says existing docs do not fit wiki style. Broad documentation archaeology with unclear payment. Reject.
   - 결정: NO-GO / PAYMENT_UNCLEAR

8. https://github.com/yeheskieltame/claudelance/issues/139
   - 근거(A): Opire/on-chain bounty open for 1 CELO with stake 0.1 CELO, but requires ERC-8004 Agent Identity on Celo and wallet/stake flow; multiple attempts and 9 open PRs. Token/wallet/stake conflicts with user cash/platform preference.
   - 결정: NO-GO / PAYMENT_UNCLEAR

9. https://github.com/SecureBananaLabs/bug-bounty/issues/30
   - 근거(A): $750 Algora bot bounty open, but 21 comments, ~30 open PRs, and broad benchmark suite requiring realistic auth token/schema coverage. Reject for high competition, setup burden, and unclear test-token access.
   - 결정: NO-GO / HIGH_USER_INPUT

결론: GO 후보 없음. 현금성·플랫폼 지급 명확성·낮은 경쟁도·승인 가능성을 동시에 충족하지 못해 코딩/claim/PR 제출하지 않음.
