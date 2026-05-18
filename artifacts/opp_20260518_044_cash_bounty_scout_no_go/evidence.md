# Bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 사용자 관여도, 예상 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/rxrbln/t2sde/issues/141
   - t2sde #141 — LibreOffice optional dependencies packaging
   - 근거: A: open issue with bounty-M (40€) label; PR endpoint works; PR #379 already opened for libabw/libvisio deps.
   - 지급: cash-like project bounty label 40€; exact settlement route not fully documented on issue.
   - 경쟁/PR: Existing open PR #379 directly addresses part of the dependency packaging request.
   - 결정: NO-GO / DUPLICATE — 이미 동일 범위 PR이 열려 있고, 전체 optional dependencies 범위가 넓어 40€ 대비 승인 odds 낮음.

2. https://github.com/taskforcesh/bullmq/issues/126
   - bullmq #126 — Working with batches documentation
   - 근거: A: IssueHunt $20 funded badge, issue open; PR endpoint works; open PR #3863 and #3776 already cover docs.
   - 지급: IssueHunt funded $20.
   - 경쟁/PR: At least two open documentation PRs reference #126.
   - 결정: NO-GO / DUPLICATE — 현금성은 있지만 기존 문서 PR 2건 선점. 새 PR은 늦은 중복이며 금액도 낮음.

3. https://github.com/Nishant1500/bee-launcher/issues/7
   - bee-launcher #7 — Custom texture pack upload
   - 근거: A: IssueHunt $1 funded badge, issue open; PR endpoint works; open PR #74 adds resource pack upload button.
   - 지급: IssueHunt funded $1.
   - 경쟁/PR: Open PR #74 directly overlaps requested feature.
   - 결정: NO-GO / LOW_MARGIN — $1 보상, 기존 PR 선점, UI/launcher 검증 부담으로 순마진 불가.

4. https://github.com/gogs/gogs/issues/2696
   - gogs #2696 — Show merge commit label in commit view
   - 근거: A/B: issue open and help wanted, but no visible funded bounty label in GitHub metadata; PR endpoint works; PR #8261 open for same change.
   - 지급: No clear cash/platform bounty found from GitHub issue metadata.
   - 경쟁/PR: Open PR #8261 directly implements merge commit label.
   - 결정: NO-GO / PAYMENT_UNCLEAR — 지급 근거 불명확하고 동일 PR 선점. 현금성 scout 기준 미달.

5. https://github.com/OWASP-BLT/BLT/issues/6119
   - OWASP-BLT #6119 — Education Cleanup
   - 근거: A: open issue with paid/sponsors labels; body says first successful deletion PR earns $1 via GitHub Sponsors; many open deletion PRs (#6443/#6428/#6426/#6420 etc.).
   - 지급: GitHub Sponsors $1 first successful deletion PR.
   - 경쟁/PR: Many active cleanup PRs; tiny payout.
   - 결정: NO-GO / LOW_MARGIN — 지급은 명확하지만 $1라 검토/PR/리뷰 부담이 수익성 기준을 크게 밑돎.

6. https://github.com/tscircuit/pcb-viewer/issues/163
   - pcb-viewer #163 — Replace disableAutoFocus usage
   - 근거: A: /bounty $3 and 💎 Bounty label, issue open; PR endpoint works; PR #862/#863/#867/#868/#869 overlap.
   - 지급: Algora-style /bounty $3.
   - 경쟁/PR: Multiple open PRs already rename/replace the same fixture/prop.
   - 결정: NO-GO / DUPLICATE — $3 저가 + 경쟁 PR 다수로 승인/지급 기대값 낮음.

7. https://github.com/potpie-ai/potpie/issues/222
   - potpie #222 — Support multiple LLMs through LiteLLM
   - 근거: A: 💎 Bounty label, issue open; PR endpoint works; requirement spans provider service, user LLM choice/key APIs, agent execution, CrewAI removal.
   - 지급: Bounty label visible; amount not in captured body/labels.
   - 경쟁/PR: No direct duplicate confirmed before API rate-limit, but open PR queue is busy and scope is broad.
   - 결정: NO-GO / HIGH_USER_INPUT — 대형 리팩터/키 관리/API 설계 범위라 payout 금액 불명확 상태에서 승인 odds 대비 부담 과대.

결론: GO 후보 없음. 코딩, claim, /opire try, 댓글, PR 제출하지 않음.
