from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "Заказать торты, пирожные и пироги "
        "для Правильного Питания и КЕТО.\n\n"
        "В моих тортах нет добавленного сахара, глютена и маргарина(трансжиров). Я использую "
        "только полезные жиры — цельное сливочное и оливковое масло холодного отжима, масло какао. "
        "Качественную кокосовую и миндальную муку, муку из семян льна и чиа, псиллиум, "
        "свежие сезонные ягоды, фрукты, орехи, натуральные подсластители (стевия и монк фрукт), ароматные специи.\n\n"
        "Всегда готовлю с душой и любовью для вашего доброго здоровья.\n\n"
        "<b>Выберите интересующий раздел в "Меню":</b>"
    )
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Образцы кето-тортов и КЖБУ", callback_data="catalog"))
    builder.row(types.InlineKeyboardButton(text="КЕТО и ПП (Правильное Питание)", callback_data="info"))
    builder.row(types.InlineKeyboardButton(text="добавьте ингредиенты", callback_data="custom"))
    builder.row(types.InlineKeyboardButton(text="Отзывы / Оставить отзыв", callback_data="reviews"))
    builder.row(types.InlineKeyboardButton(text="Связаться со мной", callback_data="contacts"))

    await message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
