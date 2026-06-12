import logging
import os
from time import time
from typing import Dict, List

from openai import OpenAI

from translations import BOT_LINK, EMAIL, WHATSAPP_NUMBER

logger = logging.getLogger(__name__)

_user_last_ai: Dict[int, float] = {}
AI_COOLDOWN_SEC = 3.0

LANG_NAMES = {
    "tr": "Turkish",
    "ru": "Russian",
    "hy": "Armenian",
    "es": "Spanish",
    "en": "English",
}

SYSTEM_PROMPT = """You are the AI assistant for Gor Sargsyan's digital business card bot on Telegram.

Profile:
- Name: Gor Sargsyan
- Title: AI Agent & Bot Expert, AI Engineer & Economist
- Experience: 15 years of strategic business experience
- Services: Autonomous Sales Agents (AI Agents), Conversion-focused Web & Landing Pages, Economic Automation & Data Analysis
- Value proposition: Data-driven solutions that can reduce business costs by up to 30%

Contact:
- WhatsApp: +{whatsapp}
- Telegram: @SargsyanOfLife
- Email: {email}
- Spain Office: +34 678 27 66 26
- Twitter/X: @laguataa
- Bot: {bot_link}

Order process:
1. Customer describes their need (AI Agent, Web, Automation)
2. Free consultation via WhatsApp
3. Custom proposal with price and timeline
4. Project starts after approval

Typical timelines: AI Agent/Bot 1-3 weeks, Landing Page 1-2 weeks, Automation 2-6 weeks
Payment: bank transfer, crypto, milestone-based — discussed per project

Rules:
- Always respond in {language}
- Be professional, concise, and persuasive
- Help customers place orders — guide them to WhatsApp or /order command
- Answer questions about services, pricing, timeline, payment, support, consultation
- Greet warmly when user says hello
- Guide users to WhatsApp (+{whatsapp}) for orders and custom quotes
- Mention the free 15-Year Savings Guide when relevant
- Do not invent specific prices — say projects are customized
- Keep answers under 200 words
- Use plain text, no HTML or markdown
"""


def build_system_prompt(lang: str) -> str:
    return SYSTEM_PROMPT.format(
        whatsapp=WHATSAPP_NUMBER,
        email=EMAIL,
        bot_link=BOT_LINK,
        language=LANG_NAMES.get(lang, "English"),
    )


def is_ai_enabled() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def check_ai_rate_limit(user_id: int) -> bool:
    now = time()
    last = _user_last_ai.get(user_id, 0)
    if now - last < AI_COOLDOWN_SEC:
        return False
    _user_last_ai[user_id] = now
    return True


async def get_ai_response(user_message: str, lang: str, history: List[dict]) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    messages = [{"role": "system", "content": build_system_prompt(lang)}]
    messages.extend(history[-6:])
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=400,
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()
