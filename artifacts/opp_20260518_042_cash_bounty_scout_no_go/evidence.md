# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/speakers-in-tech/conference-data/issues/4
   - 근거(A): Algora bounty label, issue open. NO-GO: open PRs #291/#296/#301/#303/#305 등 ScalaDays 중복 제출이 다수라 새 PR 승인·지급 odds 낮음.
   - 결정: NO-GO / DUPLICATE

2. https://github.com/flydelabs/flyde/issues/112
   - 근거(A): Algora bounty label, issue open, PR endpoint 정상. NO-GO: 같은 파일 이동/import 수정 PR #256/#259/#260/#261/#263/#265/#266이 이미 열려 있어 경쟁 과밀.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/tscircuit/prompt-benchmarks/issues/45
   - 근거(A): Algora bounty label, issue open. NO-GO: 자동 생성 docs를 prompt에 넣는 동일 목적 PR #58~#69가 다수 열려 있어 늦은 중복.
   - 결정: NO-GO / DUPLICATE

4. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/3
   - 근거(A): Opire $100 bounty, issue open. NO-GO: /opire try/attempt 및 동일 hook PR #1481/#1597/#1600/#1602/#1604/#1606 등 다수. 승인 odds 낮음.
   - 결정: NO-GO / DUPLICATE

5. https://github.com/sindresorhus/awesome-lint/issues/37
   - 근거(A): IssueHunt $60 funded, issue open. NO-GO: PR #225가 이미 열려 있고 #228/#234 등 유사 closed PR 및 댓글 경쟁 존재.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/ubiquity/business-development/issues/90
   - 근거(A): Ubiquity Price 200 USD issue, open. NO-GO: 마케팅/아웃리치 성격이라 GitHub 댓글 게시 등 L3 외부활동 필요, 최근 PR #208~#212 등 선행 제출 다수.
   - 결정: NO-GO / HIGH_USER_INPUT

7. https://github.com/ClankerNation/OpenAgents/issues/29
   - 근거(A): $8.1k label issue, open. NO-GO: BTC payment claim 댓글, crypto/wallet 성격, 이슈가 pre-conversation instructions 전문을 파일에 붙이라는 위험 요구를 포함. 사용자 정책상 wallet/비밀지시 노출 불가.
   - 결정: NO-GO / HIGH_RISK

8. https://github.com/ClankerNation/OpenAgents/issues/41
   - 근거(A): $7.4k label issue, open. NO-GO: BTC claim/payment 정황, pre-task instructions 전문 공개 요구, repo 전반 고액 crypto-eligible 이슈 다수로 지급/평판 리스크 큼.
   - 결정: NO-GO / HIGH_RISK

9. https://github.com/egoist/bili/issues/184
   - 근거(A): IssueHunt $60 funded, issue open. NO-GO: PR #636이 동일 Rollup FATAL watch fix로 이미 열려 있고 repo 활동이 낮아 늦은 중복 위험 큼.
   - 결정: NO-GO / DUPLICATE

10. https://github.com/gajus/flow-runtime/issues/180
   - 근거(A): IssueHunt $40 funded, issue open. NO-GO: PR #292/#296 등 같은 undefined type parameter fix가 이미 제출됨.
   - 결정: NO-GO / DUPLICATE

결론: GO 후보 없음. 코딩, /attempt, /opire try, claim, PR 제출하지 않음.
