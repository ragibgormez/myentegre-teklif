# Project State

## Project State
- Phase: dev
- Last completed: V2 Dream Big DNA + V3 Ren Edu DNA refactor (anasayfa + 6 alt sayfa her biri)
- Next up: Commit + push, Coolify auto-deploy, browser visual review
- Blockers: none

## Key Decisions
- 3 demo (V1/V2/V3) anasayfa farklı tasarım dilleri için (2026-04-30)
- V1 = Sonos (dokunulmuyor), V2 = Dream Big, V3 = Ren Edu (2026-04-30)
- V2 DNA: 5-card prestij grid (TED/MEB/TÜBİTAK/Bilim Olimpiyatları/ULSF), 5-kolon footer (+Neredeyiz), 8rem section padding (2026-04-30)
- V3 DNA: navy `#1A2332` + orange accent, hero auto-slider (3 slide), 6-kolon dark navy footer + Mobil Uygulama (2026-04-30)
- Logo "çatısız" hali kullanılıyor (logo-white.png/logo-dark.png) (2026-04-30)
- Town fontu başlıklarda, body Inter/Plus Jakarta (Town body için yetersiz variant) (2026-04-30)
- Renk paleti: #f37422 (primary), #c23f1b, #9b1618, #ff7727, #fec841 (Renkler.psd'den) (2026-04-30)
- Coolify deployment: docker-compose.yaml + expose only (no host port) (2026-04-30)
- Bind mount yok production için, lokal override ile port mapping (2026-04-30)

## Active Context
- Branch: main
- Recently changed:
  - core/templates/core/v2-modern.html (Dream Big DNA: prestij grid, trust metric, 5-kolon footer)
  - core/templates/core/v3-journey.html (Ren Edu DNA: hero slider, navy palette, 6-kolon footer)
  - core/templates/core/v2/kurumsal/*.html (5-kolon Neredeyiz footer + 8rem padding sync)
  - core/templates/core/v3/kurumsal/*.html (navy CSS variables + 6-kolon dark navy footer sync)
- Test suite: 22 endpoint manual curl — hepsi 200 OK
- Stack: Django 5.0 + Postgres 16 + gunicorn + whitenoise + Docker Compose

## Endpoints (canlı)
- `/` → Tasarım seçici
- `/v1/` → Sonos minimalist anasayfa
- `/v2/` → Dream Big premium-corporate anasayfa
- `/v3/` → Ren Edu warm-photo journey anasayfa
- `/{v1,v2,v3}/kurumsal/{hikayemiz,yonetim-kadromuz,felsefemiz,insan-kaynaklari,kurumsal-kimlik,franchise}/` → 18 alt sayfa
- `/admin/` → Django admin

## Brand Assets
- core/static/img/logo-white.png — beyaz logo (koyu arkaplan)
- core/static/img/logo-dark.png — siyah logo (açık arkaplan)
- core/static/fonts/Town10-Display-{Medium,Bold,Black}.otf
- core/static/video/hero.mp4 (V1 hero arkaplan video)
