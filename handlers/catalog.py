import logging
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# Прямые веб-ссылки на фото с вашего сайта
BASE_IMG_URL = "https://mersinwellness.com/images/"

CATALOG_ITEMS = [
    {
        "title": "🍰 Кето Чизкейк",
        "image": BASE_IMG_URL + "cake1.jpg",
        "params": "Ø 24 см | высота 5 см | ~1,5 кг",
        "kbzhu": (
            "• Калории: ~3100 ккал\n"
            "• Белки: ~110 г\n"
            "• Жиры: ~255 г\n"
            "• Углеводы (чистые): ~45 г"
        )
    },
    {
        "title": "🍫 Шоколадный Кето-Торт",
        "image": BASE_IMG_URL + "cake2.jpg",
        "params": "Ø 24 см | высота 5 см | ~1,7 кг",
        "kbzhu": (
            "• Калории: ~6500 ккал\n"
            "• Белки: ~130 г\n"
            "• Жиры: ~615 г\n"
            "• Углеводы (чистые): ~65 г"
        )
    },
    {
        "title": "👑 Фирменный Кето-Торт",
        "image": BASE_IMG_URL + "cake3.jpg",
        "params": "Ø 24 см | высота 8 см | ~2 кг",
        "kbzhu": (
            "• Калории: ~2900 ккал\n"
            "• Белки: ~95 г\n"
            "• Жиры: ~240 г\n"
            "• Углеводы (чистые): ~50 г"
        )
    },
    {
        "title": "🎃 Ореховый Тыквенный Латте",
        "image": BASE_IMG_URL + "cake4.jpg",
        "params": "Ø 24 см | высота 8 см | ~1,8 кг",
        "kbzhu": (
            "• Калории: ~6200 ккал\n"
            "• Белки: ~121 г\n"
            "• Жиры: ~542 г\n"
            "• Углеводы (чистые): ~130 г"
        )
    }
]

async def send_catalog_item(message: types.Message, item: dict):
    caption = (
        f"<b>{item['title']}</b>\n"
        f"📏 {item['params']}\n\n"
        f"<b>КБЖУ на весь торт:</b>\n"
        f"{item['kbzhu']}"
    )
    
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(text="💬 Написать в Telegram", url="https://t.me/Mersinwellness"),
        types.InlineKeyboardButton(text="📱 WhatsApp", url="https://wa.me/9052059288")
    )
    
    try:
        await message.answer_photo(
            photo=item["image"],
            caption=caption,
            parse_mode="HTML",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        logging.error(f"Ошибка отправки фото {item['image']}: {e}")
        await message.answer(
            text=caption,
            parse_mode="HTML",
            reply_markup=builder.as_markup()
        )

@router.message(Command("catalog"))
async def cmd_catalog(message: types.Message):
    for item in CATALOG_ITEMS:
        await send_catalog_item(message, item)

@router.callback_query(F.data == "catalog")
async def cb_catalog(callback: types.CallbackQuery):
    await callback.answer()
    for item in CATALOG_ITEMS:
        await send_catalog_item(callback.message, item)