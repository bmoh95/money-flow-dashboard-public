# Cash bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 참여자격, 사용자 관여도, 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/tscircuit/pcb-viewer/issues/163
   - 후보: tscircuit/pcb-viewer #163 — disableAutoFocus → focusOnHover={false}
   - 지급: Algora-style /bounty $3; bot comment shows $3 bounty and /attempt flow.
   - preflight: Issue open, PR endpoint works, assignee 없음. 그러나 comments에 다수 /attempt 및 PR #857/#861/#862/#863/#867/#868/#869 등 동일 범위 open PR 확인.
   - 결정: NO-GO / DUPLICATE — 낮은 금액 때문이 아니라 동일 fixture/prop 교체 PR이 이미 과밀해 승인·지급 odds가 낮음.

2. https://github.com/tscircuit/schematic-trace-solver/issues/29
   - 후보: tscircuit/schematic-trace-solver #29/#34 — same-net trace segment merge phase
   - 지급: Algora-style /bounty $100 labels/body visible.
   - preflight: Issue open, assignee 없음, PR endpoint works. 그러나 open PR #362/#363/#364/#365 및 claim PR #269/#270 계열이 같은 요구를 이미 구현 중.
   - 결정: NO-GO / DUPLICATE — 보상은 좋지만 경쟁 PR이 직접 겹치고 알고리즘/테스트 부담이 커 새 PR 제출은 늦은 중복.

3. https://github.com/spaceandtimefdn/sxt-proof-of-sql/issues/560
   - 후보: spaceandtimefdn/sxt-proof-of-sql #560 — improve Rust test coverage
   - 지급: Algora $200+$229.2; maintainer comment says $0.10 per newly covered line.
   - preflight: Issue open, maintainer permits parallel smaller PRs. 그러나 comments에 다수 /attempt, open PR #1725~#1744 등이 이미 작은 slice를 선점. 미점유 uncovered line 식별에는 repo clone+coverage 분석이 필요.
   - 결정: HOLD / OPPORTUNITY_COST — 잠재 후보지만 현재 scout 내에서 무경쟁 작은 slice를 검증하지 못함. 구현 전 coverage/PR file-list 비교 필요.

4. https://github.com/kcolbchain/research/issues/1
   - 후보: kcolbchain/research #1 — MEV on L2 rollups research brief
   - 지급: Opire `/opire try` comments visible; cash/platform 가능성은 있으나 issue body에는 amount/settlement detail 없음.
   - preflight: Issue open, assignee 없음, PR endpoint works. Comments show repeated /opire try and one participant withdrew after noting PR #10 already merged a 2,576-word brief satisfying scope.
   - 결정: NO-GO / DUPLICATE — 이미 충족된 범위로 보이며 지급 조건도 GitHub issue 본문만으로 불충분. 새 글 제출은 중복/저품질 리스크.

5. https://github.com/ubiquity/business-development/issues/90
   - 후보: ubiquity/business-development #90 — GitHub Based Marketing
   - 지급: Price: 200 USD label; Ubiquity bot flow.
   - preflight: Issue open. Bot comments repeatedly say “must be core team member or administrator to start this task”; wallet/profile flow also appears. Task itself is outbound marketing/commenting style.
   - 결정: NO-GO / HIGH_USER_INPUT — 참여자격 preflight 실패(core/admin requirement) + 외부 마케팅/댓글 스팸 위험 + wallet/L4성 정보 요구 가능.

6. https://github.com/SolFoundry/solfoundry/issues/855
   - 후보: SolFoundry #855 — GitHub Action for external repos to post bounties
   - 지급: 500K $FNDRY token reward; non-cash/wallet route.
   - preflight: Issue open, /opire try와 여러 claim/comment 및 PR #1109 제출 확인. Scope는 GitHub Action+integration으로 중간 이상.
   - 결정: NO-GO / PAYMENT_UNCLEAR — 토큰/지갑 payout 중심이고 기존 PR/claim이 있어 user 정책상 현금성 우선 scout에서 탈락.

7. https://github.com/Scottcjn/rustchain-bounties/issues/2796
   - 후보: rustchain-bounties #2796 — BoTTube discussion thread
   - 지급: 2 RTC token/community bounty.
   - preflight: Issue open but requires BoTTube account activity, social/community engagement, proof posting and wallet-like RTC address. Many claims already posted.
   - 결정: NO-GO / HIGH_USER_INPUT — 토큰·외부 커뮤니티·계정/지갑·마케팅성 활동이 필요해 자동 현금성 PR 루프에 부적합.

결론: 자동 구현/claim/PR 제출까지 갈 GO 후보 없음. Space and Time coverage는 별도 깊은 coverage 분석 전 HOLD 성격이나 이번 scout에서는 신규 구현하지 않음.
