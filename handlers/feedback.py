from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def get_feedback_keyboard():
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
        )
    )
    return builder.as_markup()

FEEDBACK_TEXT = (
    "<b>💬 Отзывы и предложения</b>\n\n"
    "Обратная связь — лучшая награда за мою работу! Я делаю каждый десерт с заботой "
    "о вашем здоровье и всегда рад вашим отзывам и пожеланиям.\n\n"
    "<b>Вы можете:</b>\n"
    "• Почитать отзывы покупателей на моем сайте\n"
    "• Оставить свой отзыв или предложение мне лично\n\n"
    "📩 <b>Direct Email:</b> info@mersinwellness.com"
)

# Слушаем /feedback, /reviews и тексты
@router.message(Command("feedback"))
@router.message(Command("reviews"))
@router.message(F.text.in_({"/feedback", "/reviews", "feedback", "reviews", "Отзывы"}))
async def cmd_feedback(message: types.Message):
    await message.answer(
        text=FEEDBACK_TEXT, 
        parse_mode="HTML", 
        reply_markup=get_feedback_keyboard()
    )

@router.callback_query(F.data.in_({"feedback", "reviews"}))
async def cb_feedback(callback: types.CallbackQuery):
    await callback.message.answer(
        text=FEEDBACK_TEXT, 
        parse_mode="HTML", 
        reply_markup=get_feedback_keyboard()
    )
    await callback.answer()
