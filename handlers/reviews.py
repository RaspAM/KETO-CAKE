from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

async def send_reviews(event: types.Message | types.CallbackQuery):
    text = (
        "<b>💬 Отзывы и предложения</b>\n\n"
        "Обратная связь — лучшая награда за мою работу! Я делаю каждый десерт с любовью "
        "к вашему здоровью и всегда рад вашим отзывам и пожеланиям.\n\n"
        "<b>Вы можете:</b>\n"
        "• Почитать отзывы покупателей на моем сайте\n"
        "• Оставить свой отзыв или предложение мне лично\n\n"
        "📩 <b>Direct Email:</b> info@mersinwellness.com"
    )
    
    builder = InlineKeyboardBuilder()
    
    # 1. Посмотреть отзывы на сайте
    builder.row(
        types.InlineKeyboardButton(
            text="⭐️ Читать отзывы на сайте", 
            url="https://mersinwellness.com/reviews.html"
        )
    )
    
    # 2. Понятными и прямыми кнопками даем выбор связи
    builder.row(
        types.InlineKeyboardButton(
            text="✍️ Написать в Telegram", 
            url="https://t.me/Mersinwellness"
        ),
        types.InlineKeyboardButton(
            text="📧 Написать на Email", 
            url="mailto:info@mersinwellness.com"
        )
    )

    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())

# Обработчик команды /reviews из синего меню
@router.message(Command("reviews"))
async def cmd_reviews(message: types.Message):
    await send_reviews(message)

# Обработчик инлайн-кнопки
@router.callback_query(F.data == "reviews")
async def cb_reviews(callback: types.CallbackQuery):
    await send_reviews(callback)
