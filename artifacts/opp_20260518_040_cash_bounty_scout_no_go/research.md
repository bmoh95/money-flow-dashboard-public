# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/devpool-directory/devpool-directory/issues/5906
   - 근거(A): Price 75 USD, open, linked upstream Dynamic Sitemap issue. PR endpoint works and no matching open PR found. Reject/HOLD: March /attempt exists and prior clarifying comment from user has no maintainer response; payout/review path should not be assumed before confirmation.
   - 결정: NO-GO / NO_APPROVAL

2. https://github.com/devpool-directory/devpool-directory/issues/5911
   - 근거(A): Price 75 USD, open, linked upstream Self Invalidations issue. No matching open PR found. Reject/HOLD: existing March /attempt plus user clarification comment unanswered; starting implementation risks duplicate/unpaid work.
   - 결정: NO-GO / NO_APPROVAL

3. https://github.com/devpool-directory/devpool-directory/issues/5886
   - 근거(A): Price 450 USD, open. Reject: claimant already posted implementation PR #5947 for Plugin Health Monitor; competing PR would be late and lower approval odds.
   - 결정: NO-GO / DUPLICATE

4. https://github.com/devpool-directory/devpool-directory/issues/5066
   - 근거(A): Price 600 USD, open. Reject: existing claimant announced Cow Swap implementation; scope includes CoW SDK/permit/order flow and likely wallet/crypto product context, high user/payment risk.
   - 결정: NO-GO / HIGH_RISK

5. https://github.com/devpool-directory/devpool-directory/issues/5064
   - 근거(A): Price 900 USD, open. Reject: PR #155 already submitted and discussed by multiple users; approval odds for a new duplicate implementation are weak.
   - 결정: NO-GO / DUPLICATE

6. https://github.com/karakeep-app/karakeep/issues/836
   - 근거(B): User-pledged 50 USD PDF highlighting feature, open approved feature request. Reject: not platform escrow/official payout, broad PDF text-layer/highlighter integration, many open repo PRs and existing scope clarification comment by user unanswered.
   - 결정: NO-GO / PAYMENT_UNCLEAR

7. https://github.com/ivrit-ai/ivrit-py/issues/15
   - 근거(B): 100 NIS bounty with README rules, open. Reject: PR #21 already submitted and maintainer reviewing; duplicate performance work would require benchmark/GPU setup and approval odds low.
   - 결정: NO-GO / DUPLICATE

8. https://github.com/zio/zio/issues/9844
   - 근거(B): Open issue labeled $1K, comments include /bounty $100 maintainer-only and attempts. Reject: reward amount/payout source ambiguous, ZIO core concurrency API design high review burden, no Algora payment comment captured.
   - 결정: NO-GO / PAYMENT_UNCLEAR

9. https://github.com/tscircuit/graphics-debug/issues/42
   - 근거(A): Algora $8 open bounty. Reject: 200+ competing/related PRs observed for objectLimit and reward label already present; $8 is below margin threshold.
   - 결정: NO-GO / LOW_MARGIN

10. https://github.com/tscircuit/schematic-trace-solver/issues/29
   - 근거(A): Algora $100 open bounty. Reject: 90+ comments and multiple active PRs (#365/#363/#358/#357) for same-net trace combining; crowded route and algorithmic scope reduce approval odds.
   - 결정: NO-GO / DUPLICATE

11. https://github.com/UnsafeLabs/Bounty-Hunters/issues/752
   - 근거(A): Algora $200 open Laravel auth bounty. Reject: repo has many AI-agent PRs and prior project guidance recorded as symbolic/research-oriented; issue already has submitted PR #22 and competing attempt comment.
   - 결정: NO-GO / PAYMENT_UNCLEAR

결론: GO 후보 없음. 코딩, /attempt, claim, PR 제출하지 않음.
