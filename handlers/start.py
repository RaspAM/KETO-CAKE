from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "Здравствуйте! Я готовлю на заказ кето-торты, пирожные и пироги "
        "для Правильного Питания.\n\n"
        "В моих тортах нет добавленного сахара, глютена. Я использую "
        "только полезные жиры -> цельное сливочное и оливковое масло холодного отжима и масло какао. "
        "Качественную кокосовую и миндальную муку, муку из семян льна и чиа, псиллиум. "
        "свежие сезонные ягоды, фрукты, орехи, натуральные подсластители стевия и монк фрукт, ароматные специи.\n\n"
        "Всё это даёт богатство вкуса, пользу витаминов, клетчатки и полифенолов.\n\n"
        "<b>Выберите интересующий раздел ниже:</b>"
    )
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🍰 Посмотреть образцы и КБЖУ", callback_data="catalog"))
    builder.row(types.InlineKeyboardButton(text="📝Узнать о пользе КЕТО - Правильного Питания", callback_data="custom"))
    builder.row(types.InlineKeyboardButton(text="⭐ Отзовы", callback_data="Reviews"))
    builder.row(types.InlineKeyboardButton(text="💬 Контакты", url="https://t.me/ваш_username"))

    await message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
