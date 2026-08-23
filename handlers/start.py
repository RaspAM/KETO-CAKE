from aiogram import Router, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "<b>Заказать торты, пирожные и пироги</b>\n"
        "Правильного Питания и КЕТО.\n\n"
        "Без сахара, глютена и маргарина. "
        "Только натуральные ингредиенты: сливочное и оливковое масло, "
        "масло какао, миндальная и кокосовая мука, семена льна и чиа, "
        "свежие ягоды, фрукты, орехи, стевия и монк-фрукт.\n\n"
        "Готовлю с душой и любовью для вашего доброго здоровья. ❤️\n\n"
        "<b>Выберите интересующий раздел в синем «Меню» 👇</b>"
    )
    await message.answer(text, parse_mode="HTML")