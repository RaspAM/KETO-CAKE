import logging
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

BASE_IMG_URL = "https://mersinwellness.com/images/"

CATALOG_ITEMS = [
    {
        "title": '"Смаковница" Кето-Чизкейк',
        "image": BASE_IMG_URL + "cake1_1.jpg",
        "params": "Ø 18 см | высота 6 см | ~1,1 кг",
        "price": "Базовый от 900 ₺",
        "highlight": "✨ Свежесть спелого инжира, мята и киви — яркая нотка удовольствия.",
        "kbzhu": (
            "• Калории: ~2800 ккал\n"
            "• Белки: ~95 г\n"
            "• Жиры: ~233 г\n"
            "• Углеводы (чистые): ~60 г"
        )
    },
    {
        "title": '🍫 Шоколадный торт "Море Какао"',
        "image": BASE_IMG_URL + "cake2_1.jpg",
        "params": "Ø 18 см | высота 6 см | ~1,2 кг",
        "price": "Базовый от 800 ₺",
        "highlight": "✨ Настоящее какао дарит насыщенный шоколадный вкус.",
        "kbzhu": (
            "• Калории: ~2890 ккал\n"
            "• Белки: ~90 г\n"
            "• Жиры: ~220 г\n"
            "• Углеводы (чистые): ~58 г"
        )
    },
    {
        "title": '🌊 Пудинг - бисквит "Морской"',
        "image": BASE_IMG_URL + "cake3.jpg",
        "params": "Ø 18 см | высота 6 см | ~1,1 кг",
        "price": "Базовый от 800 ₺",
        "highlight": "✨ Желе экстракт голубики, бисквит тыква — заряд здоровья.",
        "kbzhu": (
            "• Калории: 1750–2000 ккал\n"
            "• Белки: 58–65 г\n"
            "• Жиры: 150–162 г\n"
            "• Углеводы (чистые): 29–39 г"
        )
    },
    {
        "title": "🎃 Ореховый Тыквенный Латте",
        "image": BASE_IMG_URL + "cake4.jpg",
        "params": "Ø 18 см | высота 6 см | ~1,3 кг",
        "price": "Базовый от 950 ₺",
        "highlight": "✨ Изюминка в орехах и тыквенных семечках — забота о сердце.",
        "kbzhu": (
            "• Калории: ≈ 4370 ккал\n"
            "• Белки: ≈ 125 г\n"
            "• Жиры: ≈ 350 г\n"
            "• Углеводы (чистые): ≈ 654 г"
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

# Отдельный обработчик для команды из меню /catalog
@router.message(Command("catalog"))
async def cmd_catalog(message: types.Message):
    for item in CATALOG_ITEMS:
        await send_catalog_item(message, item)

# Отдельный обработчик для нажатия инлайн-кнопки
@router.callback_query(F.data == "catalog")
async def cb_catalog(callback: types.CallbackQuery):
    await callback.answer()
    for item in CATALOG_ITEMS:
        await send_catalog_item(callback.message, item)
