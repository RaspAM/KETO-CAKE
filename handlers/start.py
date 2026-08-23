from aiogram import Router, types, F
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# 1. Приветствие по /start — чистый текст БЕЗ инлайн-кнопок
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    text = (
        "Здесь вы можете заказать вкусняшки без сахара!\n\n"
        "<b>Выберите интересующий раздел в синем «Меню» 👇</b>"
    )
    
    await message.answer(text, parse_mode="HTML")

# 2. Обработка раздела Контакты (команда /contacts из синего меню)
@router.message(Command("contacts"))
@router.callback_query(F.data == "contacts")
async def show_contacts(event: types.Message | types.CallbackQuery):
    text = (
        "<b>Контакты и заказ:</b>\n\n"
        "📍 <b>Локация:</b> Mersin Mezitli Davultepe Soray-2\n"
        "📱 <b>WhatsApp / Тел:</b> +90 520 592 88\n"
        "🌐 <b>Сайт:</b> mersinwellness.com\n\n"
        "Для расчета заказа и консультации звоните мне или напишите в WhatsApp или Telegram:"
    )
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="📲 Написать в WhatsApp", url="https://wa.me/9052059288"))
    
    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
