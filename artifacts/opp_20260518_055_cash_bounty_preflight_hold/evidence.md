# Cash bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 참여자격, 사용자 관여도, 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/854
   - 후보: UnsafeLabs/Bounty-Hunters #854 — $140 branch protection status display and force-push prevention
   - 지급: Algora bot, $140 cash/platform bounty. /attempt then PR with /claim flow.
   - preflight: Issue open, assignee 없음, PR endpoint works. 경쟁 PR 검색상 직접 #854 PR은 closed 3건만 확인. 댓글에는 과거 automated attempts 존재. 참여 조건: AI-only allowed, /attempt 필요, payout profile may be required after merge.
   - 결정: HOLD / AUTH_BLOCKED — 가장 유망하지만 PR 전 /attempt 댓글과 fork 생성/PR 오픈이 필요함. 현재 환경은 GitHub SSH 인증은 있으나 gh/GitHub API token이 없고 bmoh95 fork도 없어 자동 제출 루프가 막힘.

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/860
   - 후보: UnsafeLabs/Bounty-Hunters #860 — $115 global search across chat/files/git history
   - 지급: Algora bot, $115 cash/platform bounty.
   - preflight: Issue open, assignee 없음. 댓글/PR 검색에서 prior Hermes/zp6/OpenClaw PR 다수 closed 및 active attempt comments 확인. 구현 범위가 T3 app 전역 검색으로 넓음.
   - 결정: NO-GO / DUPLICATE — 중복 선점 기록과 넓은 범위 때문에 빠른 승인 odds 낮음.

3. https://github.com/UnsafeLabs/Bounty-Hunters/issues/864
   - 후보: UnsafeLabs/Bounty-Hunters #864 — $100 t3code:// custom protocol deep links
   - 지급: Algora bot, $100 cash/platform bounty.
   - preflight: Issue open, assignee 없음. 댓글에 multiple /attempt automation entries. Search API rate limit으로 PR 중복 전체 확인은 제한됐지만 같은 repo 최근 PR 과밀과 broad desktop/runtime integration scope 확인.
   - 결정: NO-GO / NO_EVIDENCE — 중복 PR 확정 확인이 부족하고 desktop protocol scope가 커서 자동 PR 기준 미달.

4. https://github.com/archestra-ai/archestra/issues/4225
   - 후보: archestra-ai/archestra #4225 — $80 guardrails blocked Tool Result Policy bypass
   - 지급: Algora bot, $80 bounty.
   - preflight: Issue open but assignees iskhakov/VadimLarinTech present. Bot says core team assignment needed. Open competing PRs #4765/#4227/#4725 and many closed similar fixes.
   - 결정: NO-GO / DUPLICATE — 보안/guardrails 성격 + assignee + 경쟁 PR 과밀로 자동 제출 부적합.

5. https://github.com/spaceandtimefdn/sxt-proof-of-sql/issues/560
   - 후보: spaceandtimefdn/sxt-proof-of-sql #560 — improve Rust test coverage
   - 지급: Algora $200+$229 bounty, per uncovered-line style.
   - preflight: Issue open, multiple contributors allowed. 그러나 PR search shows hundreds of related coverage PRs and open PRs #1279/#1697/#1549/#1613/#1594 등. Rust coverage target selection requires substantial local build/test time.
   - 결정: NO-GO / DUPLICATE — payment clear지만 crowded long-tail coverage bounty라 quick micro-bounty loop에 부적합.

6. https://github.com/Expensify/App/issues/90552
   - 후보: Expensify/App #90552 — $250 selected payer highlighted background bug
   - 지급: Expensify external issue, apparent paid contributor flow.
   - preflight: Issue open but assignee bernhardoj present, multiple proposals in comments, onboarding requires Slack/email contributor flow. Prior PR #90886 closed. Large React Native app.
   - 결정: NO-GO / HIGH_USER_INPUT — Slack/onboarding/proposal-review route and existing assignee make autonomous low-burden PR unsuitable.

결론: 1건은 cash/platform·저경쟁 후보로 HOLD, 5건은 중복/참여부담/범위 리스크로 NO-GO. 외부 댓글·claim·PR 제출 없음.
