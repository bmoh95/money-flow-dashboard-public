# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback은 사용하지 않음.

1. https://github.com/UnsafeLabs/RFC-5322/issues/1
   - 근거(A): $400 ABNF-compliant RFC 5322 Python parser. Issue open and PR route has 0 open PRs, but CONTRIBUTING.md explicitly says the bounty is symbolic/research-only and not paid bounty work. NO-GO: PAYMENT_UNCLEAR/HIGH_RISK.
   - 결정: NO-GO

2. https://github.com/ClankerNation/OpenAgents/issues/140
   - 근거(A): $3k request-id middleware bounty. Low comment count, but CONTRIBUTING.md repeats symbolic/research-only warning and payment is crypto-oriented. User cannot rely on token/wallet rail. NO-GO: HIGH_RISK/PAYMENT_UNCLEAR.
   - 결정: NO-GO

3. https://github.com/tscircuit/jlcsearch/issues/92
   - 근거(A): Algora-style $75 is_extended_promotional column. Issue open and PRs accepted, but 100 open PRs with many direct matches (#309-#316) and 64 issue comments. NO-GO: crowded/approval odds too low.
   - 결정: NO-GO

4. https://github.com/sindresorhus/awesome-lint/issues/37
   - 근거(A): IssueHunt $60 header-image lint rule. Legit funded badge and clear npm test path, but open PR #225 plus several ready fork implementations in comments. Low reward and duplicate risk. NO-GO: OPPORTUNITY_COST.
   - 결정: NO-GO

5. https://github.com/pschanely/CrossHair/issues/115
   - 근거(A): IssueHunt $100 trace callback performance. Legit funded badge, but maintainer says goalposts evolved; open competing PRs #409/#411/#412 and C-extension/performance benchmark burden. NO-GO: crowded + high review risk.
   - 결정: NO-GO

6. https://github.com/LibVNC/libvncserver/issues/686
   - 근거(B): ExtendedMouseButtons feature mentions IssueHunt incentive path, but no visible funded badge/amount in issue, PR #720 already implements it, and maintainer asked repeat commenters to stop. NO-GO: NO_EVIDENCE/DUPLICATE.
   - 결정: NO-GO

7. https://github.com/potpie-ai/potpie/issues/222
   - 근거(A): LiteLLM migration bounty-labeled issue. Maintainer comment says team is taking it internally; existing migrations/fork patches exist. Broad system rewrite with unclear payout amount. NO-GO: already reserved internally.
   - 결정: NO-GO

8. https://github.com/Reqrefusion/FreeCAD-Documentation-Project/issues/27
   - 근거(B): Documentation reward labels present, but payout mechanism/amount unclear and maintainer response requires prior FreeCAD proof before discussing reward. Existing docs PRs cover pieces. NO-GO: PAYMENT_UNCLEAR/HIGH_USER_INPUT.
   - 결정: NO-GO

결론: GO 후보 없음. 실제 지급 가능성/승인 확률/경쟁도 기준 미달이라 코딩·claim·PR 제출하지 않음.
