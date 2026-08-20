from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

REVIEWS_LIST = [
    {
        "author": "Ирина",
        "text": "Заказывала кето-чизкейк на день рождения. Это просто восторг! Нежный, абсолютно без приторности, и главное — никакой тяжести в животе."
    },
    {
        "author": "Мария",
        "text": "Шоколадный торт превзошел все ожидания! Семья даже не поняла, что он без сахара и муки. Теперь за десертами только к Андрею."
    }
]

@router.callback_query(F.data == "reviews")
async def show_reviews(callback: types.CallbackQuery):
    await callback.answer()
    
    text = "<b>⭐ Отзывы наших клиентов:</b>\n\n"
    for item in REVIEWS_LIST:
        text += f"💬 <i>«{item['text']}»</i>\n— <b>{item['author']}</b>\n\n"
        
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🍰 Посмотреть образцы и КБЖУ", callback_data="catalog"))
    builder.row(types.InlineKeyboardButton(text="💬 Написать в Telegram", url="https://t.me/Mersinwellness"))

    await callback.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
