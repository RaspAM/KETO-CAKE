from aiogram import Router, F, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

# Исправлено "keto_info" на "info"
@router.callback_query(F.data == "info")
async def show_keto_info(callback: types.CallbackQuery):
    await callback.answer()
    
    text = (
        "<b>В чём польза КЕТО и Правильного Питания?</b>\n\n"
        "<b>1. Безопасность и здоровье</b>\n"
        "• <b>Здоровье зубов:</b> Мои десерты не провоцируют кариес.\n"
        "• <b>Комфорт ЖКТ:</b> Отсутствие сахара предотвращает рост патогенных бактерий, избавляя от изжоги и тяжести.\n"
        "• <b>Стабильный уровень сахара:</b> Без резких скачков глюкозы в крови после еды.\n\n"
        "<b>2. Долгое чувство сытости и контроль аппетита</b>\n"
        "Выпечка богата натуральной клетчаткой без крахмала, стимулирует выработку гормона сытости (GLP-1) "
        "и бутирата (масляной кислоты) — ключевого метаболита здоровья кишечника и защиты слизистой. "
        "Вы получаете ровную энергию и сытость без переедания.\n\n"
        "<b>3. Легкость и поддержка обмена веществ</b>\n"
        "Минимум нагрузки на метаболизм. Отказ от добавленного сахара — доказанный способ снизить риски ожирения, "
        "диабета 2 и 3 типа, а также сердечно-сосудистых заболеваний."
    )
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="📖 Читать статью на сайте", url="https://mersinwellness.com/keto-health.html"))
    builder.row(types.InlineKeyboardButton(text="⬅️ Главное меню", callback_data="main_menu"))

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=builder.as_markup())