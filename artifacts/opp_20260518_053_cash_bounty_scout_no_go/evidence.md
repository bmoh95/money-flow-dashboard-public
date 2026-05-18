# Cash bounty/direct-payout scout

검토 기준: 실제 bounty 여부, open 상태, 중복/경쟁 PR, PR 가능 여부, payout rail, 참여자격, 사용자 관여도, 난이도, 승인/지급 가능성. 콘텐츠 fallback 없음.

1. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1
   - 후보: claude-builders-bounty #1 — $50 structured CHANGELOG generator skill/script
   - 지급: Opire-powered $50; issue body says /opire try, PR, automatic payment on merge.
   - preflight: Issue open, assignee 없음, PR endpoint works. 그러나 comments 800+ and open PRs include #1598/#1610/#1611/#1614/#1618 등 동일 changelog generator submissions; repeated /opire try comments.
   - 결정: NO-GO / DUPLICATE — 요구사항은 작지만 이미 직접 중복 PR이 많아 늦은 제출의 승인·지급 odds 낮음.

2. https://github.com/claude-builders-bounty/claude-builders-bounty/issues/4
   - 후보: claude-builders-bounty #4 — $150 Claude Code PR review agent
   - 지급: Opire-powered $150; issue body says /opire try, PR, automatic payment on merge.
   - preflight: Issue open, assignee 없음, PR endpoint works. 그러나 open PR #1567/#1588/#1590/#1594/#1603/#1616 등 PR-review agent submissions 다수; comments 380+.
   - 결정: NO-GO / DUPLICATE — cash/platform은 선명하지만 경쟁 PR 과밀 및 테스트 출력 요구로 빠른 승인 가능성이 낮음.

3. https://github.com/highlight/highlight/issues/8635
   - 후보: highlight/highlight #8635 — replace workspace/project settings antd components
   - 지급: Algora/💎 Bounty label visible on open issue.
   - preflight: Issue open but assignee Vadman97 present. PR endpoint works, open PR #10368/#10370/#10378/#10398/#10403/#10406/#10407/#10408/#10409/#10429/#10431/#10433/#10435/#10440/#10442 등 동일 refactor slices 과밀.
   - 결정: NO-GO / DUPLICATE — 큰 코드베이스·assigned issue·동일 slice 경쟁으로 작은 자동 PR 승인 odds 낮음.

4. https://github.com/taskforcesh/bullmq/issues/126
   - 후보: taskforcesh/bullmq #126 — IssueHunt $20 Working with batches docs
   - 지급: IssueHunt $20 funded badge; bot text says submit PR via IssueHunt to receive reward.
   - preflight: Issue open, assignee 없음, PR endpoint works. 그러나 docs PR #3776와 #3863가 이미 동일 batch/realtime updates docs를 제출했고 maintainer comment links current Pro docs.
   - 결정: NO-GO / DUPLICATE — 문서 micro-bounty로는 적합하지만 이미 동일 해결 PR이 있어 새 PR은 중복.

5. https://github.com/Nishant1500/bee-launcher/issues/7
   - 후보: Nishant1500/bee-launcher #7 — IssueHunt $1 custom texture/resource pack upload
   - 지급: IssueHunt $1 funded badge; bot text says submit PR via IssueHunt to receive reward.
   - preflight: Issue open but assignee Nishant1500 present. PR endpoint works; PR #74 already adds resource pack upload flow and issue comment links it. Issue scope also bundles unrelated feature ideas.
   - 결정: NO-GO / DUPLICATE — $1 금액은 허용 대상이나 기존 PR이 핵심 기능을 선점했고 원 issue 범위가 잡다해 승인 odds 낮음.

6. https://github.com/ubiquity/business-development/issues/90
   - 후보: ubiquity/business-development #90 — GitHub Based Marketing
   - 지급: Price: 200 USD label; Ubiquity bot flow.
   - preflight: Issue open, PR endpoint works. 최근 bot comments say “must be core team member, or administrator to start this task”; wallet command flow visible. Task is outbound GitHub marketing/search/commenting style.
   - 결정: NO-GO / HIGH_USER_INPUT — 참여자격 preflight 실패(core/admin requirement) + wallet/profile flow + 외부 마케팅/스팸 평판 리스크.

결론: 자동 구현/claim/PR 제출까지 갈 GO 후보 없음. 낮은 금액 자체가 아니라 경쟁 선점, 참여자격 실패, 지급/마케팅 리스크 때문에 중단.
