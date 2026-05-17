# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/756
   - 근거(A): Algora 댓글상 $250, open, PR endpoint works, Laravel email verification scope는 로컬 구현 가능. Reject: CONTRIBUTING.md가 “research project, bounties symbolic, not paid bounty work”라고 명시해 현금성 지급 신뢰가 깨짐; 이미 /attempt 3건 존재.
   - 결정: NO-GO / PAYMENT_UNCLEAR

2. https://github.com/woodpecker-ci/autoscaler/issues/102
   - 근거(A): $50 bounty label/open. Reject: open PR #624/#602가 Oracle autoscaler provider를 이미 구현 중; cloud provider 구현 범위가 $50 대비 크고 중복.
   - 결정: NO-GO / DUPLICATE

3. https://github.com/ClankerNation/OpenAgents/issues/133
   - 근거(A): /bounty $8500, open, PR 가능. Reject: Solidity oracle 변경은 고위험이고 issue가 modified file에 full session/startup instructions 삽입을 요구해 안전/프라이버시 경계 위반.
   - 결정: NO-GO / HIGH_RISK

4. https://github.com/algora-io/algora/issues/238
   - 근거(A): Algora UI bug issue open. Reject: open PR #267/#266/#257/#256/#253/#248/#239 등 동일 이슈 해결 시도 다수; 늦은 추가 PR 승인 odds 낮음.
   - 결정: NO-GO / DUPLICATE

5. https://github.com/aporthq/aport-integrations/issues/4
   - 근거(A): $50 USD n8n custom node bounty open. Reject: open PRs 50개 중 #111/#112가 n8n node를 이미 제출; publish/install docs 요구 대비 소액.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/aporthq/aport-integrations/issues/31
   - 근거(A): $10 USD n8n policy node bounty open. Reject: #112 등 직접 경쟁 PR 존재, n8n example/docs/tests 요구가 $10 대비 과함.
   - 결정: NO-GO / LOW_MARGIN

7. https://github.com/zanakinz/ZUI/issues/3
   - 근거(B): $10–20 USD ZUI input blocking availability thread. Reject: open PR #4/#5/#6/#7 already target Bounty #001; issue itself is availability 확인 thread라 지급/claim path 불명확.
   - 결정: NO-GO / DUPLICATE

8. https://github.com/FreeCAD/FPA/issues/470
   - 근거(B): FreeCAD Bugfix Rewards Program discussion/open. Reject: this is reward program submission/discussion, not a concrete reward-eligible bug with acceptance criteria; cash distance and exact payout unclear.
   - 결정: NO-GO / NO_CHANNEL

9. https://github.com/HavenOnStellar/Haven_Docs/issues/5
   - 근거(B): Architecture diagram docs issue open. Reject: no explicit cash/platform bounty label in issue; Stellar/on-chain bounty lifecycle docs but payout rail absent.
   - 결정: NO-GO / NO_EVIDENCE

10. https://github.com/crossbario/autobahn-testsuite/issues/144
   - 근거(B): Jules/Algora challenge link mention. Reject: issue is program discussion, not active task; open PR already adds participation guide, payout acceptance unclear.
   - 결정: NO-GO / PAYMENT_UNCLEAR

결론: GO 후보 없음. 코딩, /attempt, claim, PR 제출하지 않음.
