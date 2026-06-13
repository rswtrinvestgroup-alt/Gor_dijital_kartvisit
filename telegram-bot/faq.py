from typing import Optional

FAQ_ITEMS = [
    {
        "id": "services",
        "labels": {
            "tr": "🤖 Hizmetler",
            "ru": "🤖 Услуги",
            "hy": "🤖 Ծառայություններ",
            "es": "🤖 Servicios",
            "en": "🤖 Services",
        },
        "keywords": [
            "hizmet", "servis", "ne yap", "yapay zeka", "ai agent", "bot",
            "service", "services", "what can", "automation",
            "услуг", "что может", "агент", "автоматизац",
            "ծառայություն", "ինչ կարող", "ագենտ",
            "servicio", "qué puede", "automatización",
        ],
        "answers": {
            "tr": (
                "<b>Yapay Zeka Hizmetleri:</b>\n\n"
                "▸ <b>Otonom Satış Ajanları</b> — 7/24 çalışan, randevu alan AI asistanlar\n"
                "▸ <b>Web & Landing Page</b> — Dönüşüm odaklı AI entegreli siteler\n"
                "▸ <b>Ekonomik Otomasyon</b> — Maliyetleri %30'a kadar azaltan veri analizi\n\n"
                "Detaylı görüşme için WhatsApp'tan ulaşabilirsiniz."
            ),
            "ru": (
                "<b>Услуги ИИ:</b>\n\n"
                "▸ <b>Автономные агенты продаж</b> — AI-ассистенты 24/7\n"
                "▸ <b>Web & Landing Page</b> — Сайты с интеграцией ИИ\n"
                "▸ <b>Экономическая автоматизация</b> — Снижение расходов до 30%\n\n"
                "Свяжитесь через WhatsApp для подробностей."
            ),
            "hy": (
                "<b>ԱԻ Ծառայություններ:</b>\n\n"
                "▸ <b>Ավտոնոմ վաճառքի գործակալներ</b> — 24/7 AI օգնականներ\n"
                "▸ <b>Web & Landing Page</b> — ԱԻ ինտեգրված կայքեր\n"
                "▸ <b>Տնտեսական ավտոմատացում</b> — Ծախսերի նվազեցում մինչև 30%\n\n"
                "Մանրամասների համար գրեք WhatsApp-ում։"
            ),
            "es": (
                "<b>Servicios de IA:</b>\n\n"
                "▸ <b>Agentes de ventas autónomos</b> — Asistentes AI 24/7\n"
                "▸ <b>Web & Landing Page</b> — Sitios con integración de IA\n"
                "▸ <b>Automatización económica</b> — Reducción de costos hasta 30%\n\n"
                "Contacta por WhatsApp para más detalles."
            ),
            "en": (
                "<b>AI Services:</b>\n\n"
                "▸ <b>Autonomous Sales Agents</b> — 24/7 AI assistants\n"
                "▸ <b>Web & Landing Page</b> — AI-integrated conversion sites\n"
                "▸ <b>Economic Automation</b> — Up to 30% cost reduction\n\n"
                "Contact via WhatsApp for details."
            ),
        },
    },
    {
        "id": "prices",
        "labels": {
            "tr": "💰 Fiyatlar",
            "ru": "💰 Цены",
            "hy": "💰 Գներ",
            "es": "💰 Precios",
            "en": "💰 Pricing",
        },
        "keywords": [
            "fiyat", "ücret", "maliyet", "ne kadar", "kaç para", "bütçe",
            "price", "pricing", "cost", "how much", "budget",
            "цен", "стоим", "сколько",
            "գին", "արժե",
            "precio", "cuánto", "costo",
        ],
        "answers": {
            "tr": (
                "<b>Fiyatlandırma:</b>\n\n"
                "Her proje işletmenin ihtiyacına göre özelleştirilir. "
                "Hazırlanan çözümlerde ortalama <b>%30 maliyet tasarrufu</b> hedeflenir.\n\n"
                "Ücretsiz ön görüşme için WhatsApp'tan yazın — projenize özel teklif hazırlanır."
            ),
            "ru": (
                "<b>Цены:</b>\n\n"
                "Каждый проект индивидуален. Средняя цель — <b>экономия до 30%</b> на затратах.\n\n"
                "Напишите в WhatsApp для бесплатной консультации и персонального предложения."
            ),
            "hy": (
                "<b>Գնագոյացում:</b>\n\n"
                "Յուրաքանչյուր նախագիծ անհատական է։ Նպատակը <b>մինչև 30% ծախսերի խնայողություն</b> է։\n\n"
                "Անվճար խորհրդատվության համար գրեք WhatsApp-ում։"
            ),
            "es": (
                "<b>Precios:</b>\n\n"
                "Cada proyecto es personalizado. Objetivo: <b>ahorro de hasta 30%</b> en costos.\n\n"
                "Escribe por WhatsApp para una consulta gratuita y propuesta personalizada."
            ),
            "en": (
                "<b>Pricing:</b>\n\n"
                "Every project is customized. Target: <b>up to 30% cost savings</b>.\n\n"
                "Message on WhatsApp for a free consultation and custom quote."
            ),
        },
    },
    {
        "id": "contact",
        "labels": {
            "tr": "📞 İletişim",
            "ru": "📞 Контакты",
            "hy": "📞 Կապ",
            "es": "📞 Contacto",
            "en": "📞 Contact",
        },
        "keywords": [
            "iletişim", "ulaş", "telefon", "numara", "adres", "contact",
            "reach", "phone", "email", "whatsapp", "telegram",
            "контакт", "связ", "телефон",
            "կապ", "հեռախոս",
            "contacto", "teléfono", "correo",
        ],
        "answers": {
            "tr": (
                "<b>İletişim:</b>\n\n"
                "💬 WhatsApp: <a href=\"tel:+79220918218\">+7 922 091 82 18</a>\n"
                "✈️ Telegram: @SargsyanOfLife\n"
                "🤖 Bot: @Gor_OffLife_kartvisit_bot\n"
                "✉️ E-posta: gor077887@gmail.com\n"
                "📍 İspanya: <a href=\"tel:+34678276626\">+34 678 27 66 26</a>\n"
                "🐦 X: @laguataa\n"
                "🌐 Kartvizit: rswtrinvestgroup-alt.github.io/Gor_dijital_kartvisit/Gor/"
            ),
            "ru": (
                "<b>Контакты:</b>\n\n"
                "💬 WhatsApp: +7 922 091 82 18\n"
                "✈️ Telegram: @SargsyanOfLife\n"
                "✉️ E-mail: gor077887@gmail.com\n"
                "📍 Офис в Испании: +34 678 27 66 26\n"
                "🐦 X/Twitter: @laguataa"
            ),
            "hy": (
                "<b>Կապ:</b>\n\n"
                "💬 WhatsApp: +7 922 091 82 18\n"
                "✈️ Telegram: @SargsyanOfLife\n"
                "✉️ E-mail: gor077887@gmail.com\n"
                "📍 Իսպանիայի գրասենյակ: +34 678 27 66 26\n"
                "🐦 X/Twitter: @laguataa"
            ),
            "es": (
                "<b>Contacto:</b>\n\n"
                "💬 WhatsApp: +7 922 091 82 18\n"
                "✈️ Telegram: @SargsyanOfLife\n"
                "✉️ Correo: gor077887@gmail.com\n"
                "📍 Oficina España: +34 678 27 66 26\n"
                "🐦 X/Twitter: @laguataa"
            ),
            "en": (
                "<b>Contact:</b>\n\n"
                "💬 WhatsApp: +7 922 091 82 18\n"
                "✈️ Telegram: @SargsyanOfLife\n"
                "✉️ Email: gor077887@gmail.com\n"
                "📍 Spain Office: +34 678 27 66 26\n"
                "🐦 X/Twitter: @laguataa"
            ),
        },
    },
    {
        "id": "experience",
        "labels": {
            "tr": "👤 Hakkında",
            "ru": "👤 О Gor",
            "hy": "👤 Gor-ի մասին",
            "es": "👤 Sobre Gor",
            "en": "👤 About Gor",
        },
        "keywords": [
            "tecrübe", "deneyim", "kim", "gor", "hakkında", "kimsin",
            "experience", "who", "about", "background", "years",
            "опыт", "кто", "о гор",
            "փորձ", "ով է",
            "experiencia", "quién", "años",
        ],
        "answers": {
            "tr": (
                "<b>Gor Sargsyan</b> — Ekonomist ve AI Mühendisi\n\n"
                "Otonom yapay zeka ajanları, dönüşüm odaklı web çözümleri ve "
                "ekonomik otomasyon alanlarında uzmanlaşmıştır."
            ),
            "ru": (
                "<b>Гор Саргсян</b> — Экономист и ИИ-инженер\n\n"
                "Специализация: автономные ИИ-агенты, конверсионные веб-решения, экономическая автоматизация."
            ),
            "hy": (
                "<b>Գոր Սարգսյան</b> — Տնտեսագետ և ԱԻ Ինժեներ\n\n"
                "Մասնագիտացում՝ ավտոնոմ գործակալներ, վեբ կայքեր, տնտեսական ավտոմատացում։"
            ),
            "es": (
                "<b>Gor Sargsyan</b> — Economista e Ingeniero de IA\n\n"
                "Especializado en agentes autónomos, sitios web y automatización económica."
            ),
            "en": (
                "<b>Gor Sargsyan</b> — Economist and AI Engineer\n\n"
                "Specialized in autonomous AI agents, conversion-focused web solutions, and economic automation."
            ),
        },
    },
    {
        "id": "guide",
        "labels": {
            "tr": "🚀 Tasarruf Rehberi",
            "ru": "🚀 Руководство",
            "hy": "🚀 Ուղեցույց",
            "es": "🚀 Guía",
            "en": "🚀 Guide",
        },
        "keywords": [
            "rehber", "pdf", "indir", "tasarruf", "guide", "download", "savings",
            "руководств", "скачать", "экономи",
            "ուղեցույց", "ներբեռն",
            "guía", "descargar", "ahorro",
        ],
        "answers": {
            "tr": (
                "<b>Tasarruf Rehberi</b>\n\n"
                "İşletmenizde yapay zeka ile %30 tasarruf yöntemlerini öğrenin.\n\n"
                "Rehberi almak için ana menüden <b>🚀 Tasarruf Rehberi</b> butonuna tıklayın "
                "ve telefon numaranızı gönderin."
            ),
            "ru": (
                "<b>Руководство по экономии</b>\n\n"
                "Узнайте, как сэкономить 30% с помощью ИИ.\n\n"
                "Нажмите <b>🚀 Руководство</b> в меню и отправьте номер телефона."
            ),
            "hy": (
                "<b>Խնայողության Ուղեցույց</b>\n\n"
                "Սովորեք, թե ինչպես խնայել 30% ԱԻ-ի միջոցով։\n\n"
                "Սեղմեք <b>🚀 Ուղեցույց</b> և ուղարկեք հեռախոսահամարը։"
            ),
            "es": (
                "<b>Guía de Ahorro</b>\n\n"
                "Aprende a ahorrar 30% con IA.\n\n"
                "Pulsa <b>🚀 Guía de Ahorro</b> en el menú y envía tu número."
            ),
            "en": (
                "<b>Savings Guide</b>\n\n"
                "Learn how to save 30% with AI.\n\n"
                "Tap <b>🚀 Savings Guide</b> in the menu and send your phone number."
            ),
        },
    },
    {
        "id": "order",
        "labels": {
            "tr": "🛒 Sipariş",
            "ru": "🛒 Заказ",
            "hy": "🛒 Պատվեր",
            "es": "🛒 Pedido",
            "en": "🛒 Order",
        },
        "keywords": [
            "sipariş", "siparis", "satın al", "almak istiyorum", "teklif", "order",
            "buy", "purchase", "quote", "proposal",
            "заказ", "купить", "заказать",
            "պատվեր", "գնել",
            "pedido", "comprar", "cotización",
        ],
        "answers": {
            "tr": (
                "<b>Sipariş Nasıl Verilir?</b>\n\n"
                "1️⃣ İhtiyacınızı belirtin (AI Agent, Web, Otomasyon)\n"
                "2️⃣ WhatsApp'tan Gor ile ücretsiz görüşme yapın\n"
                "3️⃣ Size özel teklif hazırlanır\n"
                "4️⃣ Onay sonrası proje başlar\n\n"
                "Hemen sipariş için <b>🛒 Sipariş Ver</b> butonuna tıklayın veya WhatsApp'tan yazın."
            ),
            "ru": (
                "<b>Как заказать?</b>\n\n"
                "1️⃣ Опишите потребность (AI Agent, Web, Автоматизация)\n"
                "2️⃣ Бесплатная консультация в WhatsApp\n"
                "3️⃣ Персональное предложение\n"
                "4️⃣ Старт проекта после одобрения\n\n"
                "Нажмите <b>🛒 Заказать</b> или напишите в WhatsApp."
            ),
            "hy": (
                "<b>Ինչպես պատվիրել?</b>\n\n"
                "1️⃣ Նկարագրեք կարիքը (AI Agent, Web, Ավտոմատացում)\n"
                "2️⃣ Անվճար խորհրդատվություն WhatsApp-ում\n"
                "3️⃣ Անհատական առաջարկ\n"
                "4️⃣ Նախագիծը սկսվում է հաստատումից հետո\n\n"
                "Սեղմեք <b>🛒 Պատվիրել</b> կամ գրեք WhatsApp-ում։"
            ),
            "es": (
                "<b>¿Cómo pedir?</b>\n\n"
                "1️⃣ Describe tu necesidad (AI Agent, Web, Automatización)\n"
                "2️⃣ Consulta gratuita por WhatsApp\n"
                "3️⃣ Propuesta personalizada\n"
                "4️⃣ Inicio del proyecto tras aprobación\n\n"
                "Pulsa <b>🛒 Pedir</b> o escribe por WhatsApp."
            ),
            "en": (
                "<b>How to Order?</b>\n\n"
                "1️⃣ Describe your need (AI Agent, Web, Automation)\n"
                "2️⃣ Free consultation via WhatsApp\n"
                "3️⃣ Custom proposal prepared\n"
                "4️⃣ Project starts after approval\n\n"
                "Tap <b>🛒 Place Order</b> or message on WhatsApp."
            ),
        },
    },
    {
        "id": "payment",
        "labels": {
            "tr": "💳 Ödeme",
            "ru": "💳 Оплата",
            "hy": "💳 Վճարում",
            "es": "💳 Pago",
            "en": "💳 Payment",
        },
        "keywords": [
            "ödeme", "odeme", "para", "transfer", "kredi kart", "payment", "pay",
            "оплат", "платёж", "деньги",
            "վճարում", "գումար",
            "pago", "pagar", "transferencia",
        ],
        "answers": {
            "tr": (
                "<b>Ödeme:</b>\n\n"
                "Ödeme yöntemleri proje bazında belirlenir. Genellikle:\n"
                "▸ Banka transferi\n"
                "▸ Kripto / uluslararası transfer\n"
                "▸ Aşamalı ödeme (büyük projelerde)\n\n"
                "Detaylar için WhatsApp'tan Gor ile görüşün."
            ),
            "ru": (
                "<b>Оплата:</b>\n\n"
                "Способы оплаты обсуждаются индивидуально:\n"
                "▸ Банковский перевод\n"
                "▸ Крипто / международный перевод\n"
                "▸ Поэтапная оплата\n\n"
                "Подробности в WhatsApp."
            ),
            "hy": (
                "<b>Վճարում:</b>\n\n"
                "Վճարման եղանակները քննարկվում են անհատական։\n"
                "▸ Բանկային փոխանցում\n"
                "▸ Կրիպտո / միջազգային փոխանցում\n"
                "▸ Փուլային վճարում\n\n"
                "Մանրամասներ՝ WhatsApp-ում։"
            ),
            "es": (
                "<b>Pago:</b>\n\n"
                "Métodos de pago según el proyecto:\n"
                "▸ Transferencia bancaria\n"
                "▸ Cripto / transferencia internacional\n"
                "▸ Pago por fases\n\n"
                "Detalles por WhatsApp."
            ),
            "en": (
                "<b>Payment:</b>\n\n"
                "Payment methods are set per project:\n"
                "▸ Bank transfer\n"
                "▸ Crypto / international transfer\n"
                "▸ Milestone-based payment\n\n"
                "Details via WhatsApp."
            ),
        },
    },
    {
        "id": "timeline",
        "labels": {
            "tr": "⏱️ Süre",
            "ru": "⏱️ Сроки",
            "hy": "⏱️ Ժամկետ",
            "es": "⏱️ Plazos",
            "en": "⏱️ Timeline",
        },
        "keywords": [
            "süre", "sure", "ne zaman", "teslimat", "kaç gün", "hafta", "timeline",
            "delivery", "deadline", "how long", "when",
            "срок", "когда", "доставк",
            "ժամկետ", "երբ",
            "plazo", "cuándo", "entrega",
        ],
        "answers": {
            "tr": (
                "<b>Teslim Süresi:</b>\n\n"
                "▸ <b>AI Agent / Bot:</b> 1–3 hafta\n"
                "▸ <b>Landing Page:</b> 1–2 hafta\n"
                "▸ <b>Kurumsal Otomasyon:</b> 2–6 hafta\n\n"
                "Süre proje kapsamına göre değişir. Kesin tarih için WhatsApp'tan teklif alın."
            ),
            "ru": (
                "<b>Сроки:</b>\n\n"
                "▸ <b>AI Agent / Bot:</b> 1–3 недели\n"
                "▸ <b>Landing Page:</b> 1–2 недели\n"
                "▸ <b>Автоматизация:</b> 2–6 недель\n\n"
                "Зависит от объёма. Точные сроки — в WhatsApp."
            ),
            "hy": (
                "<b>Ժամկետներ:</b>\n\n"
                "▸ <b>AI Agent / Bot:</b> 1–3 շաբաթ\n"
                "▸ <b>Landing Page:</b> 1–2 շաբաթ\n"
                "▸ <b>Ավտոմատացում:</b> 2–6 շաբաթ\n\n"
                "Կախված է նախագծի ծավալից։ WhatsApp-ում ճշտեք։"
            ),
            "es": (
                "<b>Plazos:</b>\n\n"
                "▸ <b>AI Agent / Bot:</b> 1–3 semanas\n"
                "▸ <b>Landing Page:</b> 1–2 semanas\n"
                "▸ <b>Automatización:</b> 2–6 semanas\n\n"
                "Depende del alcance. Plazos exactos por WhatsApp."
            ),
            "en": (
                "<b>Timeline:</b>\n\n"
                "▸ <b>AI Agent / Bot:</b> 1–3 weeks\n"
                "▸ <b>Landing Page:</b> 1–2 weeks\n"
                "▸ <b>Automation:</b> 2–6 weeks\n\n"
                "Depends on scope. Exact dates via WhatsApp."
            ),
        },
    },
    {
        "id": "consultation",
        "labels": {
            "tr": "📅 Görüşme",
            "ru": "📅 Консультация",
            "hy": "📅 Խորհրդատվություն",
            "es": "📅 Consulta",
            "en": "📅 Consultation",
        },
        "keywords": [
            "görüşme", "gorusme", "randevu", "toplantı", "demo", "consultation",
            "meeting", "appointment", "call", "ücretsiz",
            "консультац", "встреч", "звонок",
            "հանդիպում", "խորհրդատվություն",
            "consulta", "reunión", "cita", "gratis",
        ],
        "answers": {
            "tr": (
                "<b>Ücretsiz Görüşme:</b>\n\n"
                "Gor ile <b>ücretsiz ön görüşme</b> yapabilirsiniz.\n\n"
                "WhatsApp veya Telegram üzerinden ulaşın — ihtiyacınızı dinleyip "
                "size özel çözüm ve teklif sunar."
            ),
            "ru": (
                "<b>Бесплатная консультация:</b>\n\n"
                "Бесплатная консультация с Gor.\n\n"
                "Напишите в WhatsApp или Telegram."
            ),
            "hy": (
                "<b>Անվճար խորհրդատվություն:</b>\n\n"
                "Անվճար նախնական խորհրդատվություն Gor-ի հետ։\n\n"
                "Գրեք WhatsApp կամ Telegram-ում։"
            ),
            "es": (
                "<b>Consulta gratuita:</b>\n\n"
                "Consulta gratuita con Gor.\n\n"
                "Escribe por WhatsApp o Telegram."
            ),
            "en": (
                "<b>Free Consultation:</b>\n\n"
                "Free initial consultation with Gor.\n\n"
                "Message via WhatsApp or Telegram."
            ),
        },
    },
    {
        "id": "process",
        "labels": {
            "tr": "⚙️ Süreç",
            "ru": "⚙️ Процесс",
            "hy": "⚙️ Գործընթաց",
            "es": "⚙️ Proceso",
            "en": "⚙️ Process",
        },
        "keywords": [
            "süreç", "surec", "nasıl çalış", "adım", "process", "how it works", "workflow",
            "процесс", "как работает",
            "գործընթաց", "ինչպես է",
            "proceso", "cómo funciona",
        ],
        "answers": {
            "tr": (
                "<b>Çalışma Süreci:</b>\n\n"
                "1️⃣ <b>Analiz</b> — İhtiyaç ve hedef belirleme\n"
                "2️⃣ <b>Teklif</b> — Özel fiyat ve süre\n"
                "3️⃣ <b>Geliştirme</b> — AI çözümü inşa\n"
                "4️⃣ <b>Test</b> — Kalite kontrol\n"
                "5️⃣ <b>Teslimat</b> — Canlıya alma + destek"
            ),
            "ru": (
                "<b>Процесс работы:</b>\n\n"
                "1️⃣ Анализ → 2️⃣ Предложение → 3️⃣ Разработка → 4️⃣ Тест → 5️⃣ Запуск + поддержка"
            ),
            "hy": (
                "<b>Աշխատանքի գործընթաց:</b>\n\n"
                "1️⃣ Վերլուծություն → 2️⃣ Առաջարկ → 3️⃣ Զարգացում → 4️⃣ Փորձարկում → 5️⃣ Գործարկում"
            ),
            "es": (
                "<b>Proceso de trabajo:</b>\n\n"
                "1️⃣ Análisis → 2️⃣ Propuesta → 3️⃣ Desarrollo → 4️⃣ Prueba → 5️⃣ Lanzamiento + soporte"
            ),
            "en": (
                "<b>Work Process:</b>\n\n"
                "1️⃣ Analysis → 2️⃣ Proposal → 3️⃣ Development → 4️⃣ Testing → 5️⃣ Launch + support"
            ),
        },
    },
    {
        "id": "support",
        "labels": {
            "tr": "🛠️ Destek",
            "ru": "🛠️ Поддержка",
            "hy": "🛠️ Աջակցություն",
            "es": "🛠️ Soporte",
            "en": "🛠️ Support",
        },
        "keywords": [
            "destek", "yardım", "support", "help", "garanti", "bakım", "maintenance",
            "поддержк", "помощь", "гарант",
            "աջակցություն", "օգնություն",
            "soporte", "ayuda", "garantía",
        ],
        "answers": {
            "tr": (
                "<b>Destek & Garanti:</b>\n\n"
                "▸ Proje teslimi sonrası teknik destek\n"
                "▸ Bakım ve güncelleme paketleri\n"
                "▸ 7/24 AI Agent'lar kendi kendine çalışır\n\n"
                "Destek için WhatsApp: +7 922 091 82 18"
            ),
            "ru": (
                "<b>Поддержка:</b>\n\n"
                "▸ Техподдержка после сдачи\n"
                "▸ Пакеты обслуживания\n"
                "▸ AI Agents работают 24/7\n\n"
                "WhatsApp: +7 922 091 82 18"
            ),
            "hy": (
                "<b>Աջակցություն:</b>\n\n"
                "▸ Տեխնիկական աջակցություն\n"
                "▸ Սպասարկման փաթեթներ\n"
                "▸ AI Agents 24/7\n\n"
                "WhatsApp: +7 922 091 82 18"
            ),
            "es": (
                "<b>Soporte:</b>\n\n"
                "▸ Soporte técnico post-entrega\n"
                "▸ Paquetes de mantenimiento\n"
                "▸ AI Agents 24/7\n\n"
                "WhatsApp: +7 922 091 82 18"
            ),
            "en": (
                "<b>Support:</b>\n\n"
                "▸ Post-delivery technical support\n"
                "▸ Maintenance packages\n"
                "▸ AI Agents run 24/7\n\n"
                "WhatsApp: +7 922 091 82 18"
            ),
        },
    },
]

GREETING_KEYWORDS = [
    "merhaba", "selam", "slm", "günaydın", "gunaydin", "iyi akşam", "iyi günler",
    "hey", "hello", "hi", "good morning", "good evening", "howdy",
    "привет", "здравствуй", "добрый", "доброе",
    "բարև", "բարեւ", "ողջույն",
    "hola", "buenos", "buenas", "qué tal", "que tal",
]


def is_greeting(text: str) -> bool:
    lowered = text.lower().strip()
    return any(g in lowered for g in GREETING_KEYWORDS) and len(lowered.split()) <= 6


def find_faq_answer(text: str, lang: str) -> Optional[str]:
    lowered = text.lower().strip()
    for item in FAQ_ITEMS:
        if any(keyword in lowered for keyword in item["keywords"]):
            return item["answers"].get(lang, item["answers"]["en"])
    return None


def get_faq_by_id(item_id: str, lang: str) -> Optional[str]:
    for item in FAQ_ITEMS:
        if item["id"] == item_id:
            return item["answers"].get(lang, item["answers"]["en"])
    return None
