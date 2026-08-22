from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def get_reviews_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="⭐️ Читать отзывы на сайте", 
            url="https://mersinwellness.com/reviews.html"
        )
    )
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
    return builder.as_markup()

REVIEWS_TEXT = (
    "<b>💬 Отзывы и предложения</b>\n\n"
    "Обратная связь — лучшая награда за мою работу! Я делаю каждый десерт с любовью "
    "к вашему здоровью и всегда рад вашим отзывам и пожеланиям.\n\n"
    "<b>Вы можете:</b>\n"
    "• Почитать отзывы покупателей на моем сайте\n"
    "• Оставить свой отзыв или предложение мне лично\n\n"
    "📩 <b>Direct Email:</b> info@mersinwellness.com"
)

# 1. Отдельный хэндлер для команды из меню /reviews
@router.message(Command("reviews"))
async def cmd_reviews(message: types.Message):
    await message.answer(
        text=REVIEWS_TEXT, 
        parse_mode="HTML", 
        reply_markup=get_reviews_keyboard()
    )

# 2. Отдельный хэндлер для нажатия на инлайн-кнопку
@router.callback_query(F.data == "reviews")
async def cb_reviews(callback: types.CallbackQuery):
    await callback.message.answer(
        text=REVIEWS_TEXT, 
        parse_mode="HTML", 
        reply_markup=get_reviews_keyboard()
    )
    await callback.answer()
