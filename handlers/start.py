from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="🍰 Образцы кето-тортов и КБЖУ", callback_data="catalog"))
    builder.row(types.InlineKeyboardButton(text="🌱 КЕТО и ПП (Правильное Питание)", callback_data="info"))
    builder.row(types.InlineKeyboardButton(text="🛠 Добавьте ингредиенты", callback_data="custom"))
    builder.row(types.InlineKeyboardButton(text="⭐ Отзывы / Оставить отзыв", callback_data="reviews"))
    builder.row(types.InlineKeyboardButton(text="📞 Связаться со мной", callback_data="contacts"))
    return builder.as_markup()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "Заказать торты, пирожные и пироги "
        "для Правильного Питания и КЕТО.\n\n"
        "В моих тортах нет добавленного сахара, глютена и маргарина (трансжиров). Я использую "
        "только полезные жиры — цельное сливочное и оливковое масло холодного отжима, масло какао. "
        "Качественную кокосовую и миндальную муку, муку из семян льна и чиа, псиллиум, "
        "свежие сезонные ягоды, фрукты, орехи, натуральные подсластители (стевия и монк фрукт), ароматные специи.\n\n"
        "Всегда готовлю с душой и любовью для вашего доброго здоровья.\n\n"
        "<b>Выберите интересующий раздел в «Меню»:</b>"
    )
    
    await message.answer(text, parse_mode="HTML", reply_markup=get_start_keyboard())

# Обработка раздела Контакты (как через команду /contacts, так и по кнопке)
@router.message(Command("contacts"))
@router.callback_query(F.data == "contacts")
async def show_contacts(event: types.Message | types.CallbackQuery):
    text = (
        "<b>Контакты и заказ:</b>\n\n"
        "📍 <b>Локация:</b> Mersin Mezitli Davultepe Soray-2 \n"
        "📱 <b>WhatsApp:</b> +90 520 592 88\n"
        "🌐 <b>Сайт:</b> mersinwellness.com\n\n"
        "Для расчета заказа и консультации звоните или напишите через WhatsApp в телеграм:"
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="📲 Написать в WhatsApp", url="https://wa.me/9052059288"))
    
    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())