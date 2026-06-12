import asyncio
import logging
import os
import re
import sys
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv
from telegram import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from ai_chat import check_ai_rate_limit, get_ai_response, is_ai_enabled
from faq import FAQ_ITEMS, find_faq_answer, get_faq_by_id, is_greeting
from translations import (
    EMAIL,
    LANG_BUTTONS,
    TELEGRAM_CONTACT,
    TRANSLATIONS,
    TWITTER,
    WHATSAPP_NUMBER,
)

load_dotenv()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

AVATAR_PATH = Path(__file__).resolve().parent.parent / "Gor" / "avatar.jpg"
AWAITING_PHONE = "awaiting_phone"
CHAT_HISTORY = "chat_history"


def get_lang(context: ContextTypes.DEFAULT_TYPE) -> str:
    return context.user_data.get("lang", "tr")


def get_t(lang: str) -> dict:
    return TRANSLATIONS.get(lang, TRANSLATIONS["tr"])


def whatsapp_url(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def build_profile_text(lang: str) -> str:
    t = get_t(lang)
    return (
        f"<b>{t['fullName']}</b>\n"
        f"<a href=\"{TWITTER}\">{t['social']}</a>\n\n"
        f"{t['welcome']}\n\n"
        f"<b>{t['headline']}</b>\n"
        f"<i>{t['subtitle']}</i>\n\n"
        f"📍 {t['footer']}"
    )


def build_services_text(lang: str) -> str:
    t = get_t(lang)
    return (
        f"<b>{t['servicesTitle']}</b>\n\n"
        f"▸ <b>{t['service1Title']}</b>\n{t['service1Desc']}\n\n"
        f"▸ <b>{t['service2Title']}</b>\n{t['service2Desc']}\n\n"
        f"▸ <b>{t['service3Title']}</b>\n{t['service3Desc']}"
    )


def language_keyboard() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(label, callback_data=f"lang:{code}")] for code, label in LANG_BUTTONS]
    return InlineKeyboardMarkup(rows)


def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = get_t(lang)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t["btnOrder"], callback_data="menu:order")],
        [InlineKeyboardButton(t["btnServices"], callback_data="menu:services")],
        [
            InlineKeyboardButton(t["btnFAQ"], callback_data="menu:faq"),
            InlineKeyboardButton(t["btnAI"], callback_data="menu:ai"),
        ],
        [
            InlineKeyboardButton(t["btnWhatsApp"], url=whatsapp_url(t["whatsappCTAMsg"])),
            InlineKeyboardButton(t["btnTelegram"], url=TELEGRAM_CONTACT),
        ],
        [
            InlineKeyboardButton(t["btnEmail"], callback_data="menu:email"),
            InlineKeyboardButton(t["btnGuide"], callback_data="menu:guide"),
        ],
        [InlineKeyboardButton(t["btnLang"], callback_data="menu:lang")],
    ])


def faq_keyboard(lang: str) -> InlineKeyboardMarkup:
    rows = []
    row = []
    for item in FAQ_ITEMS:
        row.append(InlineKeyboardButton(item["labels"][lang], callback_data=f"faq:{item['id']}"))
        if len(row) == 2:
            rows.append(row)
            row = []
    if row:
        rows.append(row)
    t = get_t(lang)
    rows.append([InlineKeyboardButton(t["btnBack"], callback_data="menu:home")])
    return InlineKeyboardMarkup(rows)


def back_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = get_t(lang)
    return InlineKeyboardMarkup([[InlineKeyboardButton(t["btnBack"], callback_data="menu:home")]])


def order_keyboard(lang: str) -> InlineKeyboardMarkup:
    t = get_t(lang)
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t["btnWhatsApp"], url=whatsapp_url(t["whatsappOrderMsg"]))],
        [InlineKeyboardButton(t["btnBack"], callback_data="menu:home")],
    ])


async def reply_text(update: Update, text: str, lang: str, *, keyboard=None) -> None:
    await update.effective_message.reply_text(
        text,
        reply_markup=keyboard or main_menu_keyboard(lang),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


async def replace_message(query, text: str, reply_markup, *, show_photo: bool = False) -> None:
    """Fotoğraflı mesajlarda edit_message_text çalışmaz; mesajı değiştirir veya yeniden gönderir."""
    message = query.message
    chat = message.chat

    try:
        if show_photo and AVATAR_PATH.exists():
            await message.delete()
            with AVATAR_PATH.open("rb") as photo:
                await chat.send_photo(
                    photo=photo,
                    caption=text,
                    reply_markup=reply_markup,
                    parse_mode="HTML",
                )
            return

        if message.photo:
            await message.delete()
            await chat.send_message(
                text=text,
                reply_markup=reply_markup,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
            return

        await query.edit_message_text(
            text=text,
            reply_markup=reply_markup,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )
    except Exception:
        logger.exception("Mesaj güncellenemedi, yeni mesaj gönderiliyor")
        await chat.send_message(
            text=text,
            reply_markup=reply_markup,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )


async def send_profile(update: Update, context: ContextTypes.DEFAULT_TYPE, *, edit: bool = False) -> None:
    lang = get_lang(context)
    text = build_profile_text(lang)
    keyboard = main_menu_keyboard(lang)

    if edit and update.callback_query:
        await replace_message(update.callback_query, text, keyboard, show_photo=True)
        return

    message = update.effective_message
    if AVATAR_PATH.exists():
        with AVATAR_PATH.open("rb") as photo:
            await message.reply_photo(
                photo=photo,
                caption=text,
                reply_markup=keyboard,
                parse_mode="HTML",
            )
    else:
        await message.reply_text(
            text=text,
            reply_markup=keyboard,
            parse_mode="HTML",
            disable_web_page_preview=True,
        )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    context.user_data.pop(AWAITING_PHONE, None)
    if context.user_data.get("lang"):
        await send_profile(update, context)
        return
    t = get_t(get_lang(context))
    await update.message.reply_text(t["chooseLang"], reply_markup=language_keyboard())


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    await reply_text(update, get_t(lang)["helpText"], lang)


async def cmd_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    t = get_t(lang)
    await reply_text(update, f"<b>{t['orderTitle']}</b>\n\n{t['orderText']}", lang, keyboard=order_keyboard(lang))


async def cmd_services(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    await reply_text(update, build_services_text(lang), lang, keyboard=back_keyboard(lang))


async def cmd_contact(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    answer = get_faq_by_id("contact", lang)
    await reply_text(update, answer or get_t(lang)["emailText"].format(email=EMAIL), lang)


async def cmd_faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    t = get_t(lang)
    await reply_text(update, t["faqTitle"], lang, keyboard=faq_keyboard(lang))


async def cmd_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    await reply_text(update, get_t(lang)["chooseLang"], lang, keyboard=language_keyboard())


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("lang:"):
        context.user_data["lang"] = data.split(":")[1]
        context.user_data.pop(AWAITING_PHONE, None)
        context.user_data.pop(CHAT_HISTORY, None)
        await query.message.delete()
        await send_profile(update, context)
        return

    lang = get_lang(context)
    t = get_t(lang)

    if data == "menu:home":
        context.user_data.pop(AWAITING_PHONE, None)
        await send_profile(update, context, edit=True)
        return

    if data == "menu:order":
        await replace_message(
            query,
            f"<b>{t['orderTitle']}</b>\n\n{t['orderText']}",
            order_keyboard(lang),
        )
        return

    if data == "menu:services":
        await replace_message(query, build_services_text(lang), back_keyboard(lang))
        return

    if data == "menu:faq":
        await replace_message(query, t["faqTitle"], faq_keyboard(lang))
        return

    if data == "menu:ai":
        context.user_data.pop(AWAITING_PHONE, None)
        await replace_message(query, t["aiPrompt"], back_keyboard(lang))
        return

    if data.startswith("faq:"):
        item_id = data.split(":")[1]
        answer = get_faq_by_id(item_id, lang)
        if answer:
            await replace_message(query, answer, faq_keyboard(lang))
        return

    if data == "menu:email":
        await replace_message(
            query,
            t["emailText"].format(email=EMAIL),
            back_keyboard(lang),
        )
        return

    if data == "menu:guide":
        context.user_data[AWAITING_PHONE] = True
        await replace_message(
            query,
            f"{t['formTitle']}\n\n{t['formDesc']}",
            back_keyboard(lang),
        )
        return

    if data == "menu:lang":
        context.user_data.pop(AWAITING_PHONE, None)
        await replace_message(query, t["chooseLang"], language_keyboard())


async def notify_admin(context: ContextTypes.DEFAULT_TYPE, text: str) -> None:
    admin_id = os.getenv("ADMIN_CHAT_ID")
    if not admin_id:
        return
    try:
        await context.bot.send_message(chat_id=int(admin_id), text=text, parse_mode="HTML")
    except Exception:
        logger.exception("Admin bildirimi gönderilemedi")


async def handle_phone_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    lang = get_lang(context)
    t = get_t(lang)
    phone = update.message.text.strip()

    if not re.search(r"\d{6,}", phone):
        await update.message.reply_text(t["phoneInvalid"])
        return

    context.user_data.pop(AWAITING_PHONE, None)
    message = t["whatsappFormMsg"].format(phone=phone)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(t["phoneOpenWhatsApp"], url=whatsapp_url(message))],
        [InlineKeyboardButton(t["btnBack"], callback_data="menu:home")],
    ])
    await update.message.reply_text(t["phoneThanks"], reply_markup=keyboard)
    user = update.effective_user
    username = f"@{user.username}" if user.username else user.full_name
    await notify_admin(
        context,
        f"📞 <b>Yeni rehber talebi</b>\n\n"
        f"👤 {username}\n"
        f"📱 {phone}\n"
        f"🆔 ID: {user.id}",
    )


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.user_data.get(AWAITING_PHONE):
        await handle_phone_input(update, context)
        return

    lang = get_lang(context)
    t = get_t(lang)
    text = update.message.text.strip()

    if is_greeting(text):
        await reply_text(update, t["greetReply"], lang)
        return

    faq_answer = find_faq_answer(text, lang)
    if faq_answer:
        await update.message.reply_text(
            faq_answer,
            reply_markup=main_menu_keyboard(lang),
            parse_mode="HTML",
        )
        return

    if is_ai_enabled():
        user_id = update.effective_user.id
        if not check_ai_rate_limit(user_id):
            await update.message.reply_text(
                "⏳ " + ("Lütfen birkaç saniye bekleyin." if lang == "tr" else "Please wait a few seconds."),
                reply_markup=main_menu_keyboard(lang),
            )
            return
        thinking = await update.message.reply_text(t["aiThinking"])
        try:
            history = context.user_data.setdefault(CHAT_HISTORY, [])
            reply = await get_ai_response(text, lang, history)
            history.append({"role": "user", "content": text})
            history.append({"role": "assistant", "content": reply})
            context.user_data[CHAT_HISTORY] = history[-8:]
            await thinking.edit_text(reply, reply_markup=main_menu_keyboard(lang))
        except Exception:
            logger.exception("AI response failed")
            await thinking.edit_text(t["aiError"], reply_markup=main_menu_keyboard(lang))
        return

    await update.message.reply_text(
        f"{t['textFallback']}\n\n{t['aiUnavailable']}",
        reply_markup=main_menu_keyboard(lang),
    )


async def post_init(app: Application) -> None:
    await app.bot.set_my_commands([
        BotCommand("start", "Başlat / Start"),
        BotCommand("menu", "Ana menü / Main menu"),
        BotCommand("order", "Sipariş ver / Place order"),
        BotCommand("services", "Hizmetler / Services"),
        BotCommand("faq", "SSS / FAQ"),
        BotCommand("contact", "İletişim / Contact"),
        BotCommand("help", "Yardım / Help"),
        BotCommand("lang", "Dil / Language"),
    ])


def run_bot(app: Application, token: str) -> None:
    webhook_url = os.getenv("WEBHOOK_URL", "").strip()
    if webhook_url:
        port = int(os.getenv("PORT", "8080"))
        full_webhook = f"{webhook_url.rstrip('/')}/{token}"
        logger.info("Webhook modu: port=%s", port)
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=token,
            webhook_url=full_webhook,
            allowed_updates=Update.ALL_TYPES,
        )
        return

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.run_polling(allowed_updates=Update.ALL_TYPES)


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("TELEGRAM_BOT_TOKEN bulunamadı. .env dosyasını kontrol edin.")

    app = (
        Application.builder()
        .token(token)
        .post_init(post_init)
        .build()
    )
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("order", cmd_order))
    app.add_handler(CommandHandler("services", cmd_services))
    app.add_handler(CommandHandler("contact", cmd_contact))
    app.add_handler(CommandHandler("faq", cmd_faq))
    app.add_handler(CommandHandler("lang", cmd_lang))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))

    ai_status = "aktif" if is_ai_enabled() else "pasif (OPENAI_API_KEY eksik)"
    mode = "webhook" if os.getenv("WEBHOOK_URL") else "polling"
    logger.info("Gor kartvizit botu başlatılıyor... mod=%s AI=%s", mode, ai_status)
    run_bot(app, token)


if __name__ == "__main__":
    main()
