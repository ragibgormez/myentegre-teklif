# Lessons Learned

## [Sonnet] Subagent Quality Issues
- **Pattern**: Subagent kurumsal alt sayfaları yazarken relative link (`hikayemiz.html`) kullandı; Django routing'de çalışmıyordu.
- **Fix**: Subagent prompt'una "MUST use absolute URLs `/v[1-3]/kurumsal/<page>/`" net olarak yaz.

- **Pattern**: Subagent V3 alt sayfalarında aktif sayfa linkini `href="#"` yaptı; tıklayınca hiçbir şey olmuyordu.
- **Fix**: Active state için CSS class kullan (`.active`), URL her zaman gerçek olsun.

- **Pattern**: Subagent escape karakterleri `\'img/logo.png\'` kullandı Django `{% static %}` tag'inde — TemplateSyntaxError.
- **Fix**: Subagent prompt'unda örnek static usage'ı net göster (single quote, escape yok).

- **Pattern**: Subagent yazdığı sayfada eksik dropdown linki (Yönetim Kadromuz) bıraktı.
- **Fix**: Subagent verification step'ı istemeden bırakma; "verify with grep -c <pattern>" şart.

## [Infrastructure] Coolify Deployment
- **Pattern**: Image build sırasında "exporting layers" → "Gracefully shutting down" hatası.
- **Fix**: Image boyutu çok büyüktü (build-essential, libpq-dev, netcat = +360MB). `psycopg[binary]` precompiled wheel kullanır, apt paketlerine ihtiyaç yok. → 830MB → 286MB.

- **Pattern**: "Bind for 0.0.0.0:8000 failed: port is already allocated" Coolify deployment.
- **Fix**: Coolify Traefik kullanıyor, `ports: "8000:8000"` host bind kaldırıldı, sadece `expose: "8000"`.
- **Fix (lokal)**: `docker-compose.override.yml` ile lokalde port mapping; Coolify otomatik yüklemiyor.

- **Pattern**: Coolify `docker-compose.yml` ararken `.yml` bulamadı.
- **Fix**: `.yml` → `.yaml` rename.

## [Django] Template Caching
- **Pattern**: Template değiştirip restart edince eski versiyon servis ediliyor.
- **Fix**: Bind mount yok production compose'da, container build sırasında kopyalıyor. Template değişiminde rebuild gerekiyor: `docker compose up -d --build web`.

## [Subagent Scope]
- **Pattern**: Sonnet agent V3 refactor'da 7+ dakika sonra "Stream idle timeout" hatası verdi, dosyaya hiç değişiklik uygulayamadı.
- **Fix**: Büyük refactor'ları sub-tasks'a böl. 1 agent = 1 sayfada max 3-4 major change. Hero + color + service + city + testimonial + footer = ÇOK FAZLA. Bunu 2-3 sequential agent yap.
- **Lesson**: Agent prompt 5KB+ olunca token budget zorlaniyor. Section bazli ayri agent'lar daha guvenli.

## [Brand Identity]
- **Pattern**: Subagent generic accent color kullandı (#ed6c05) — gerçek brand kit'inde #f37422.
- **Fix**: Subagent prompt'una resmi renk paletini hex hex olarak yaz.

- **Pattern**: SVG logo eski "çatılı" versiyondu; tasarımcı "çatısız" istedi.
- **Fix**: PNG logo kullan (logo-white.png/logo-dark.png), scroll-driven swap CSS ile.
