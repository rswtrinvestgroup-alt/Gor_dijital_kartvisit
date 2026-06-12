# Gor Dijital Kartvizit — Hosting Rehberi

Bu rehber, projeyi 7/24 canlıya almak için adım adım yönergeler içerir.

---

## 1. HTML Kartvizit (Gor klasörü)

### Netlify (Önerilen — Ücretsiz)

1. [netlify.com](https://netlify.com) hesabı açın
2. **Add new site → Deploy manually**
3. `Gor` klasörünü sürükleyip bırakın
4. Site URL'niz: `https://random-name.netlify.app`

### Hosting sonrası yapılacaklar

`Gor/config.js` dosyasını düzenleyin:

```javascript
const SITE_CONFIG = {
  publicUrl: 'https://sizin-site.netlify.app',  // ← buraya
  telegramBot: 'https://t.me/Gor_OffLife_kartvisit_bot',
  analyticsId: 'G-XXXXXXXXXX',  // Google Analytics (opsiyonel)
  // ...
};
```

Sonra Netlify'a tekrar yükleyin.

### Özellikler (hazır)
- ✅ 5 dil
- ✅ SEO + Open Graph + Twitter Card
- ✅ QR kod (Telegram bot + site linki)
- ✅ vCard indirme (rehbere kaydet)
- ✅ Paylaş butonu
- ✅ PWA manifest
- ✅ Güvenlik header'ları (netlify.toml)

---

## 2. Telegram Bot (telegram-bot klasörü)

### Seçenek A — Bilgisayarınızda (geliştirme)

```bash
cd telegram-bot
python bot.py
```

> Bilgisayar kapalıyken bot çalışmaz.

### Seçenek B — Render.com (7/24 ücretsiz)

1. [render.com](https://render.com) hesabı açın
2. GitHub'a projeyi yükleyin
3. **New → Web Service** → repo seçin
4. Root Directory: `telegram-bot`
5. Environment Variables ekleyin:
   - `TELEGRAM_BOT_TOKEN`
   - `OPENAI_API_KEY` (opsiyonel)
   - `WEBHOOK_URL` = `https://gor-bot.onrender.com`
   - `ADMIN_CHAT_ID` = Telegram ID'niz ([@userinfobot](https://t.me/userinfobot))
6. Deploy

### Seçenek C — Docker

```bash
cd telegram-bot
docker compose up -d
```

---

## 3. .env Dosyası (Bot)

`telegram-bot/.env` örneği:

```env
TELEGRAM_BOT_TOKEN=your_token
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
WEBHOOK_URL=https://your-bot.onrender.com
ADMIN_CHAT_ID=123456789
PORT=8080
```

> ⚠️ `.env` dosyasını asla GitHub'a yüklemeyin!

---

## 4. Token Güvenliği

Token sohbette paylaşıldıysa:
1. [@BotFather](https://t.me/BotFather) → `/mybots` → bot → **Revoke token**
2. Yeni token'ı `.env` dosyasına yazın

---

## 5. Test Checklist

### Kartvizit
- [ ] Tüm diller çalışıyor
- [ ] WhatsApp / Telegram / E-posta butonları
- [ ] QR kod görünüyor
- [ ] vCard indiriliyor
- [ ] Mobilde düzgün görünüyor

### Bot
- [ ] `/start` → dil seçimi
- [ ] Tüm menü butonları
- [ ] SSS soruları
- [ ] Sipariş akışı
- [ ] Rehber formu → WhatsApp
- [ ] Admin bildirimi (ADMIN_CHAT_ID ile)

---

## 6. Önerilen URL Yapısı

| Servis | URL |
|---|---|
| Kartvizit | `https://gor.netlify.app` |
| Telegram Bot | `@Gor_OffLife_kartvisit_bot` |
| WhatsApp | `wa.me/79220918218` |

---

Sorular için: gor077887@gmail.com
