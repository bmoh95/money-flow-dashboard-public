# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성.

1. https://github.com/UnsafeLabs/Bounty-Hunters/issues/763
   - 근거(A): UnsafeLabs/FastAPI DynamicCORSMiddleware $300. Issue open, labels show bounty/AI-agent friendly, PR route open, but repo has 30+ open PRs and matching FastAPI PR noise; platform payout route not independently visible beyond issue label.
   - 결정: NO-GO

2. https://github.com/UnsafeLabs/Bounty-Hunters/issues/768
   - 근거(A): UnsafeLabs/FastAPI API key rate limit $350. Open with bounty labels, but crowded PR queue and broad security/API design surface; payout/claim rules unclear outside issue metadata.
   - 결정: NO-GO

3. https://github.com/UnsafeLabs/Bounty-Hunters/issues/818
   - 근거(A): UnsafeLabs/T3 Code fiber interrupt $120. Open, low comments, but Effect orchestration semantics are subjective; low reward vs review risk and unclear payout rail.
   - 결정: NO-GO

4. https://github.com/UnsafeLabs/Bounty-Hunters/issues/611
   - 근거(A): UnsafeLabs/Context Rift typo registry $400. Open but asks contributors to paste full session startup instructions into repository metadata; rejected for instruction/privacy leakage risk and existing competing PR #1460.
   - 결정: NO-GO

5. https://github.com/ClankerNation/OpenAgents/issues/140
   - 근거(A): OpenAgents request-ID middleware /bounty $3300. Open, PR route open, but repo has 0 stars, many bot-like high-value bounties, 49 open PRs, matching PR #246 already submitted, and required platform_instructions leakage is high-risk.
   - 결정: NO-GO

6. https://github.com/ClankerNation/OpenAgents/issues/150
   - 근거(A): OpenAgents audit-log /bounty $2600. Open but matching PR #274 exists; same instruction-leakage requirement and payout trust risk. NO-GO.
   - 결정: NO-GO

7. https://github.com/Reqrefusion/FreeCAD-Documentation-Project/issues/30
   - 근거(A): FreeCAD Documentation Release_notes_1.2 labeled Bounty/Reward/$$$/€€€, open with no PRs, but body has no amount, payout rail, acceptance owner, or settlement terms. HOLD/NO-GO until terms appear.
   - 결정: NO-GO

8. https://github.com/piotrwitek/utility-types/issues/51
   - 근거(A): IssueHunt $35 docs issue. Funded, but marked in progress and has multiple submitted/open PRs (#207/#208/#211/#216). Low payout and crowded.
   - 결정: NO-GO

9. https://github.com/prest/prest/issues/284
   - 근거(A): IssueHunt $20 mock adapter docs. Funded, but submitted/open PRs #962/#963/#965 already cover it; low payout.
   - 결정: NO-GO

10. https://github.com/LibVNC/libvncserver/issues/686
   - 근거(A): Issue points to IssueHunt route for ExtendedMouseButtons, but no current funded amount in issue and open PR #720 already targets the same feature. NO-GO.
   - 결정: NO-GO

결론: GO 후보 없음. instruction leakage 요구/경쟁 PR 선점/지급 불명확/낮은 보상 대비 리뷰 부담으로 코딩·claim·PR 제출하지 않음.
