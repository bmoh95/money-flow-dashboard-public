# Cash/platform bounty scout: all candidates failed preflight

- Run: 2026-05-19_1002_money-flow
- Checked: 2026-05-19T10:07:16+09:00

## 후보 검토
- **NO-GO / HIGH_RISK** [UnsafeLabs #828 T3 turbo graph $15](https://github.com/UnsafeLabs/Bounty-Hunters/issues/828) — Algora cash/platform route and small scope exist, assignee 없음. 그러나 _meta.json에 complete generation_context/session-start disclosure를 요구하고 이미 3명 attempt; system/context disclosure 금지로 구현/PR 중단.
- **NO-GO / HIGH_RISK** [UnsafeLabs #761 FastAPI UploadFile validation $80](https://github.com/UnsafeLabs/Bounty-Hunters/issues/761) — Algora $80, PR 가능. 그러나 contributor_meta.json session_init 전체 공개 요구 + 경쟁 attempt 4건; 시스템 초기 지시 공개 위험으로 자동 PR 불가.
- **NO-GO / HIGH_RISK** [UnsafeLabs #766 FastAPI WebSocket heartbeat $180](https://github.com/UnsafeLabs/Bounty-Hunters/issues/766) — Algora $180, assignee 없음. 그러나 runtime_instructions 전체 공개 요구, 기존 PR #1153 제출/경쟁, fast merge 조건 이슈 선행 요구로 승인확률 낮음.
- **NO-GO / HIGH_RISK** [UnsafeLabs #788 Laravel RBAC $175](https://github.com/UnsafeLabs/Bounty-Hunters/issues/788) — Algora $175, assignee 없음. 그러나 초기 프롬프트/지시문 공개형 provenance 요구와 여러 attempts; 구현 범위도 migration/model/trait/middleware/test로 작지 않음.
- **NO-GO / HIGH_RISK** [UnsafeLabs #841 T3 body-size limit $190](https://github.com/UnsafeLabs/Bounty-Hunters/issues/841) — Algora $190, assignee 없음. 그러나 _provenance.json에 platform-provided pre-task context 전체 공개 요구, PR #1080 등 기존 제출 존재.
- **NO-GO / DUPLICATE** [Devpool/Ubiquity #5957 reminder on PR reopening $75](https://github.com/devpool-directory/devpool-directory/issues/5957) — Price 75 USD/Time 2 Hours label 확인. 하지만 원본 daemon-disqualifier PR #139/#145 등 이미 제출, /attempt 경쟁 존재. 중복 승인 가능성 낮음.
- **NO-GO / DUPLICATE** [Opire $50 changelog skill](https://github.com/claude-builders-bounty/claude-builders-bounty/issues/1) — Opire cash-style claim route는 명확하나 댓글 약 900개, 다수 /opire try, broad subjective artifact. 신규 자동 PR 승인확률 낮음.
- **NO-GO / DUPLICATE** [Auki Hagall ROS2 relay $50](https://github.com/aukilabs/hagall/issues/62) — Direct $50 bounty로 보이나 WIP/broad Go+ROS2 scope, 여러 참여 댓글 및 PR #65 이미 제출. 지급/선정 조건도 별도 private payment 가능성.
