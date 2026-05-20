# Public Render QA — EITC deadline blog

- checked_at: 2026-05-21T02:52:56+09:00
- public URL: https://beemo.tistory.com/63
- mobile URL: https://beemo.tistory.com/m/63
- Attention/Cash Gate: PASS (`폭발 후보`; 5월 정기신청 마감, 기한 후 95% 지급, 직접 금전 영향)
- manage/posts category: PASS (`돈관리·구매체크/세금·장부` / categoryId `1295942` / visibility `PUBLIC`)
- fact QA: PASS (`fact_recheck_20260521.json`, 국세청 공식 페이지 4개 핵심 문구 재확인)
- body images: PASS (3 Kakao CDN PNGs, 1200×675, desktop/mobile nonzero render)
- image spacing: PASS (desktop img→caption 7px, caption→next H2 24px)
- OG/mobile thumbnail: PASS (public/mobile `og:image` is not Tistory default placeholder)
- home-list thumbnail: PASS by browser vision (real designed thumbnail, no gray/default T placeholder)
- raw Markdown/work-note leak: PASS (0 hits)
- official/source links: PASS (4/4 labels found)
- decision: `redteam_hold` → `tracking`
