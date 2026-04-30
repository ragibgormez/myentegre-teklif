# Plan: V2 & V3 Tasarım Dili Refactor

## Amaç
3 demo birbirinden net şekilde ayrışmalı, her biri kendi referansının DNA'sını taşımalı:
- **V1** = Sonos minimal-luxury (✅ mevcut hali yeterli)
- **V2** = Dream Big premium-corporate-prestige
- **V3** = Ren Edu warm-photo-journey

İçerikler **değişmeyecek** (Anasayfa sectionları aynı, sadece görsel tasarım dili değişiyor).

---

## Mevcut Durum Analizi (Karşılaştırma)

### V1 vs Sonos — ✅ Hizalı
| Sonos DNA | V1'de var mı? |
|-----------|----------------|
| Full-bleed video/image hero | ✅ Var (hero.mp4) |
| Transparent → white scroll navbar | ✅ Var |
| Massive bold sans-serif (Town Display + Inter) | ✅ Var |
| Black/white dominant + sparse orange | ✅ Var |
| Full-bleed tile grid | ✅ Var |
| White outline CTAs | ✅ Var |

**V1 dokunulmuyor.**

### V2 vs Dream Big — ❌ DNA Eksik
| Dream Big DNA | V2'de | Sorun |
|---------------|--------|--------|
| Prestijli kurum logoları carousel/grid (Harvard, MIT vb.) | ❌ Yok | Bunun yerine 4-mosaic icon kart var (generic) |
| "Hayalindeki ___ ilk adımı ___ ile at" hero copy | ❌ Generic copy | "Geleceğini şekillendir" — Dream Big formatına benzemiyor |
| Belirgin "10+ Ivy League" gibi trust metric block | ⚠️ Var ama sosyal proof biçiminde, daha küçük | Hero altına prominent metric block lazım |
| Geniş whitespace (py-32+) luxury feel | ⚠️ Yeterli değil | Daha fazla nefes alanı |
| 5-kolon footer (Yurt Dışı/Etkinlikler/Blog/İletişim/Neredeyiz) | ⚠️ 4-kolon | "Neredeyiz" 5. kolon eksik |
| "Randevu Talebi" prominent CTA | ⚠️ "Ücretsiz Danışmanlık" mevcut | İsim farklı ama format uygun |

### V3 vs Ren Edu — ❌ DNA Eksik
| Ren Edu DNA | V3'te | Sorun |
|-------------|--------|--------|
| Photography-driven full-width hero | ❌ Yok | Geometric SVG decorative shapes var (ucgen + daire) |
| Auto-rotating slider hero (3-5 slide) | ❌ Yok | Statik tek hero |
| Deep navy + accent color | ❌ Yok | Orange dominant, navy yok |
| Icon-on-top service cards (Detay → link) | ⚠️ Var ama farklı format | Card design farklı (gradient placeholder) |
| Country/flag cards format | ❌ Yok | "City + count" var ama flag/pin format değil |
| Testimonial slider | ❌ Statik | Auto-rotate yok |
| 6-kolon dark navy footer | ❌ 5-kolon | 6. kolon eksik, navy bg yok |

---

## Refactor Planı

### V2 — Dream Big DNA (anasayfa: `core/templates/core/v2-modern.html`)

#### 1. Hero Bölümü Refactor
**Eski**: Sol 2x2 mosaic kart placeholder + sağ search/CTA
**Yeni** (Dream Big):
- **Sol**: Buyuk "Hayalindeki YKS başarısına ilk adımı EN Deneyim'le at" başlığı + arama bar + iki CTA
- **Sağ**: **Prestijli kurum logo grid** (5 placeholder card with FA icons + isim: TED Mensubu, MEB Onaylı, TÜBİTAK Partner, Bilim Olimpiyatları, ULSF Member). Logo görselleri yerine icon + isim kartları (Dream Big ana DNA'sı).
- Hero altında prominent **trust metric block**: 4 büyük rakam (10+ / 50.000+ / %95 / 200+) — Dream Big "Ivy League" formatı

#### 2. Section Spacing & Whitespace
- `section { padding: 8rem 2rem; }` (py-32)
- Mobile: 4rem
- Geniş luxury feel

#### 3. Footer 5-Kolon
**Eski**: Brand / Kurumsal / Endeneyim / Abonelikler / İletişim
**Yeni** (Dream Big DNA):
- Brand (logo + slogan + sosyal)
- Kurumsal (Hakkımızda, Franchise, İK)
- Endeneyim (Neden Endeneyim, Ayrıcalıklar, Şubeler)
- Abonelikler (Solo, Elite, Premium)
- **NEREDEYİZ?** (3 sehir adresi: Cihannüma İstanbul, Çankaya Ankara, Konak İzmir)

#### 4. CTA Buton Refresh
- "Ücretsiz Danışmanlık Al" prominent orange button
- "Detayları İncele" outline secondary

#### 5. Renk Tonu
- Beyaz dominant, gri-tonu sectionlar
- Orange çok az kullanılan accent (Dream Big premium minimal)

### V3 — Ren Edu DNA (anasayfa: `core/templates/core/v3-journey.html`)

#### 1. Hero Bölümü Refactor (En kritik değişiklik)
**Eski**: Geometric SVG (üçgen + daire) + deep gradient + statik metin
**Yeni** (Ren Edu):
- Geometric SVG'leri tamamen kaldır
- **Auto-rotating CSS slider** (3 slide):
  - Slide 1: "Geleceğini EN Deneyim ile planla" + warm photo blur background
  - Slide 2: "Sana en yakın deneyimi keşfet" + map/branch photo bg
  - Slide 3: "200+ şube, 6 şehir, sen" + city panorama bg
- CSS keyframes ile 6s/slide loop
- Slide indicator dots
- Her slide'da iki CTA: "Hemen Başvur" (orange filled) + "Detaylı Bilgi" (outline)

#### 2. Color Refactor — Deep Navy + Orange
- `:root { --navy: #1A2332; --orange: #f37422; --warm: #fdf2e9; }`
- Sticky scrolled navbar: navy bg, beyaz logo
- Footer: full navy background
- Section dividers: warm gradient

#### 3. Service Cards (Ayrıcalıklar) — Ren Edu Tarzı
**Eski**: Gradient block placeholders
**Yeni**: 4 service card grid:
```
┌────────────────┐
│ [BIG ICON]     │
│ Title          │
│ 2-line desc    │
│ Detay →        │
└────────────────┘
```
Beyaz card, subtle shadow, hover'da orange border-bottom.

#### 4. Şehir Cards — Country Flag Format
**Eski**: City name + branch count
**Yeni**: Pin icon (FA) + city name + branch count + "Şubeleri Gör" link. 6 city grid.

#### 5. Testimonial Auto-Slider
**Eski**: 3 statik testimonial side-by-side
**Yeni**: CSS-only auto-rotating slider (3 testimonial, 5s/each), prev/next dots indicator.

#### 6. Footer 6-Kolon Dark Navy
- Brand (logo-white + slogan + sosyal)
- Kurumsal
- Endeneyim
- Abonelikler
- İletişim
- **Mobil Uygulama** (App Store + Google Play badges — placeholder)

---

## Alt Sayfalar (Kurumsal)

V2 ve V3'ün **18 alt sayfasında** sadece nav + footer + renk paleti güncellenir. İçerikler **değişmeyecek**.

### V2 Alt Sayfaları (6 dosya)
- Yeni 5-kolon footer kopyala
- Section spacing py-32
- Beyaz dominant palette korusun (zaten beyaz)

### V3 Alt Sayfaları (6 dosya)
- Yeni 6-kolon dark navy footer kopyala
- Color update: navy + orange
- Hero gradient warm orange-cream korunacak

---

## Strateji & Subagent Kullanımı

### Subagent Plan (Sonnet, paralel)
- **Agent A**: V2 anasayfa Dream Big DNA refactor (`v2-modern.html`)
- **Agent B**: V3 anasayfa Ren Edu DNA refactor (`v3-journey.html`)
- **Agent C** (sequential, A bittikten sonra): V2 alt sayfaları nav+footer sync
- **Agent D** (sequential, B bittikten sonra): V3 alt sayfaları nav+footer sync

### Riskler
- Subagent yine relative link kullanabilir → prompt'a EXPLICIT URL format yaz
- Subagent eskine geri dönebilir generic sayfa yazıp → prompt'a "MUST follow Dream Big/Ren Edu DNA" tekrar tekrar vurgula
- Color refactor V3'te alt sayfalarda inconsistency olabilir → bir sonraki agent'a "MATCH the new v3-journey.html palette" de

### Verification
- `curl /v[1-3]/[kurumsal/...]/` 21 endpoint hepsi 200
- Visual: tarayıcıda V2/V3 hero açılış, Dream Big/Ren Edu site karşılaştırması
- DNA checklist (yukarıdaki tablodaki ❌ → ✅)

---

## Milestone Sırası

1. **Plan onayı** (kullanıcı bu dökümanı onaylar)
2. **2 paralel agent başlat** (V2 + V3 anasayfa refactor)
3. **Anasayfa testleri** (curl + browser visual)
4. **2 paralel agent başlat** (V2 + V3 alt sayfa sync)
5. **18 endpoint smoke test**
6. **Commit + push**
7. **Coolify auto-deploy**
8. **state.md + todo.md güncelle**

Tahmini süre: ~30-45 dakika (agent paralel + kullanıcı approval cycles)
