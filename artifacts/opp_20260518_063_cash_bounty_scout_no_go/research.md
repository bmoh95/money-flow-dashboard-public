# Cash/platform bounty scout

범위: GitHub/Opire/Algora/Ubiquity/IssueHunt 스타일 현금성 direct-payout 우선. 콘텐츠 fallback 없음.
검토 기준: 실제 bounty, open 상태, 중복 PR, PR route, payout rail, 참여자격, 외부 서비스/지갑/개인정보 부담, 승인 가능성.

1. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: Claude Builders #1 — structured CHANGELOG skill/script, $50 Opire
   - 지급: A: issue body says $50 powered by Opire; claim flow is /opire try then PR, payment on merge.
   - preflight: Open, no assignee, PR route exists. However issue has ~891 comments and multiple open PRs mention #1 (#1637, #1628, #1627, #1625). Acceptance requires real-repo sample output.
   - 결정: NO-GO / DUPLICATE — cash/platform payout clear, but competition is extreme and existing submissions cover the same acceptance criteria.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
   - 후보: Claude Builders #4 — Claude Code PR review sub-agent, $150 Opire
   - 지급: A: issue body says $150 powered by Opire; /opire try + PR, payment on merge.
   - preflight: Open, no assignee, PR route exists. ~403 comments, many /opire try attempts, open PRs already mention #4 (e.g. #1629, #1624). Requires testing on 2 real PRs and structured outputs.
   - 결정: NO-GO / DUPLICATE — payout clear but overcrowded; broad agent output quality and duplicate risk make approval odds low.

3. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/5
   - 후보: Claude Builders #5 — n8n weekly dev summary workflow, $200 Opire
   - 지급: A: issue body says $200 powered by Opire; /opire try + PR, payment on merge.
   - preflight: Open, no assignee, PR route exists. ~300 comments and existing attempts. Requires real n8n instance screenshot plus Claude API workflow, which implies external service/testing burden.
   - 결정: NO-GO / HIGH_USER_INPUT — cash/platform route visible but requires external n8n/API execution evidence and is crowded.

4. https://github.com/UnsafeLabs/Bounty-Hunters/issues/611
   - 후보: UnsafeLabs #611 — fix typos in knowledge-base/context.json, $400 label
   - 지급: A: issue labels include 💎 Bounty and $400; issue/comment flow uses /bounty try and PR.
   - preflight: Open, no assignee. Existing maintainer/user comment says PR #1469 already submitted; open PR hits include #1651 and #1638 for the same issue. Requires contributor registry self-entry/payment details comments appear in thread.
   - 결정: NO-GO / DUPLICATE — micro-doc style but already has multiple PRs; self-registry/payment-comment pattern adds user/payout burden.

5. https://github.com/UnsafeLabs/Bounty-Hunters/issues/760
   - 후보: UnsafeLabs #760 — FastAPI BackgroundTasks error handling/retry
   - 지급: B: bounty-style repo/labels but no visible dollar label in checked issue output; comments include /attempt and /bounty try.
   - preflight: Open, no assignee, PR route exists. Multiple attempts. Scope changes FastAPI BackgroundTasks API behavior: callback, retries, logging, task_results and tests.
   - 결정: NO-GO / PAYMENT_UNCLEAR — implementation is non-trivial public API work and payout amount/rail was not clear enough for automatic PR.

6. https://github.com/UnsafeLabs/Bounty-Hunters/issues/853
   - 후보: UnsafeLabs #853 — T3 Code env validation at server startup, $35
   - 지급: A: issue labels include 💎 Bounty and $35; comments include /opire try.
   - preflight: Open, no assignee. Existing PR #963 referenced, recent /opire try and open PR #1678 mention #853. Requires config schema, startup CLI flag, formatted error table, tests.
   - 결정: NO-GO / DUPLICATE — small payout and scope acceptable in theory, but active/open competing PRs reduce approval odds.

7. https://github.com/ubiquity/.github/issues/124
   - 후보: Ubiquity #124 — Unified Authentication, $600
   - 지급: A: labels include Price: 600 USD and Time: <1 Day.
   - preflight: Open, no assignee. Bot comments warn “You must be a core team member, or an administrator to start this task.” Requires Supabase auth across GitHub/Google Drive/Telegram.
   - 결정: NO-GO / HIGH_USER_INPUT — cash label clear, but participant eligibility blocks non-core users and scope needs external accounts/integrations.

결론: cash/platform 후보는 있었지만, 이번 7건 모두 중복/과밀, 외부 서비스 부담, 참여자격 제한, 지급 불명확 중 하나로 자동 구현·claim·PR 기준 미달.
