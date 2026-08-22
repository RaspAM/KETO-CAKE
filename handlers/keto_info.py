from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

@router.message(Command("info"))
@router.callback_query(F.data == "info")
async def show_info(event: types.Message | types.CallbackQuery):
    text = (
        "<b>🌱 КЕТО и ПП (Правильное Питание)</b>\n\n"
        "Я готовлю десерты, которые помогают сохранять здоровье, стройность и отличное самочувствие без отказа от сладкого!\n\n"
        "<b>Главные принципы моих авторских сладостей:</b>\n"
        "• <b>Без сахара:</b> использую только натуральные безопасные подсластители с нулевым гликемическим индексом (стевия, монк фрукт).\n"
        "• <b>Без глютена:</b> основа — миндальная, кокосовая мука, мука из семян льна и чиа, псиллиум.\n"
        "• <b>Без трансжиров:</b> только натуральное сливочное масло, оливковое масло холодного отжима и масло какао.\n"
        "• <b>Идеально для КЕТО:</b> минимум чистых углеводов, максимум пользы и сытости.\n\n"
        "Каждое изделие рассчитывается по КБЖУ, чтобы вам было удобно планировать свой рацион!"
    )

    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML")
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML")