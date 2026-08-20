from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

CATALOG_ITEMS = [
    {
        "title": "🍰 Кето Чизкейк",
        "params": "Ø 24 см | высота 5 см | ~1,5 кг",
        "kbzhu": (
            "• Калории: 3000–3200 ккал\n"
            "• Белки: ~110 г\n"
            "• Жиры: ~255 г\n"
            "• Углеводы (чистые): ~45 г"
        )
    },
    {
        "title": "🍫 Шоколадный Кето-Торт",
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
        "params": "Ø 24 см | высота 8 см | ~2 кг",
        "kbzhu": (
            "• Калории: 2700–3100 ккал\n"
            "• Белки: 90–100 г\n"
            "• Жиры: 230–250 г\n"
            "• Углеводы (чистые): 45–60 г"
        )
    },
    {
        "title": "🎃 Ореховый Тыквенный Латте",
        "params": "Ø 24 см | высота 8 см | ~1.8 кг",
        "kbzhu": (
            "• Калории: ≈ 6200 ккал\n"
            "• Белки: ≈ 121 г\n"
            "• Жиры: ≈ 542 г\n"
            "• Углеводы (чистые): ≈ 130 г"
        )
    }
]

@router.callback_query(F.data == "catalog")
async def show_catalog(callback: types.CallbackQuery):
    await callback.answer()
    
    for item in CATALOG_ITEMS:
        text = (
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
        
        await callback.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
