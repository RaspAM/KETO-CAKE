from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.message(Command("info"))
@router.callback_query(F.data == "info")
async def show_info(event: types.Message | types.CallbackQuery):
    text = (
        "<b>КЕТО и Правильное Питание</b>\n\n"
         "Вкусные лакомства которые помогают сохранять здоровье, стройность и отличное самочувствие без отказа от сладкого!\n\n"
        "<b>1. Польза вшему здоровью</b>\n"
        "• <b>Здоровье зубов:</b> Мои десерты не провоцируют кариес.\n"
        "• <b>Комфорт ЖКТ:</b> Отсутствие сахара предотвращает рост патогенных бактерий, избавляя от изжоги и тяжести.\n"
        "• <b>Стабильный уровень сахара:</b> Без резких скачков глюкозы в крови после еды.\n\n"
        "<b>2. Долгое чувство сытости и контроль аппетита</b>\n"
        "Выпечка богата натуральной клетчаткой без крахмала, стимулирует выработку гормона сытости (GLP-1) "
        "и бутирата — ключевого метаболита здоровья кишечника и защиты слизистой. "
        "Вы получаете ровную энергию и сытость без переедания.\n\n"
        "<b>3. Легкость и поддержка обмена веществ</b>\n"
        "Минимум нагрузки на метаболизм. Отказ от добавленного сахара — доказанный способ снизить риски ожирения, "
        "диабета 2 и 3 типа (Альцгеймер, Деменция), а также сердечно-сосудистых заболеваний и системных заболеваний"
    )
    
    # Кнопка со ссылкой на статью на вашем сайте
    builder = InlineKeyboardBuilder()
    builder.row(
        types.InlineKeyboardButton(
            text="📖 Подробнее о КЕТО и ПП на сайте", 
            url="https://mersinwellness.com/keto-health.html"
        )
    )

    if isinstance(event, types.CallbackQuery):
        await event.message.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
        await event.answer()
    else:
        await event.answer(text, parse_mode="HTML", reply_markup=builder.as_markup())
