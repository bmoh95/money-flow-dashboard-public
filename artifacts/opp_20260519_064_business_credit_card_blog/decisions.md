# Red Team / Audit

Failure modes:
1. 세무조언처럼 읽힐 위험: '공제 가능' 단정 대신 '공제 여부 확인/변경'으로 표현해야 함.
2. 검색 경쟁 강함: 등록방법 글은 많음. 차별점은 등록·조회·공제확인 분리와 신규사업자 실수 방지.
3. 이미지/카테고리/공식 출처 QA 전 publish 금지: 카드 이미지 가독성, Tistory categoryId, public spacing 확인 필요.

Decision: HOLD / redteam_hold. Blocker is routine backlog work, not user approval.
