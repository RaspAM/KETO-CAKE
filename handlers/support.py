from aiogram import Router, F, Bot
from aiogram.types import Message
from config import ADMIN_ID

router = Router()

# Преобразуем ID в число на месте, если в config он приходит строкой
ADMIN_ID_INT = int(ADMIN_ID) if ADMIN_ID else None

# 1. Сообщение от клиента -> пересылаем вам
@router.message(F.text & ~F.text.startswith("/"))
async def forward_to_admin(message: Message, bot: Bot):
    if message.from_user.id == ADMIN_ID_INT:
        return

    await bot.forward_message(
        chat_id=ADMIN_ID_INT,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

    await message.answer(
    "✉️ <b>Ваше сообщение передано в личку!</b>\n"
    "Спасибо за обращение, я отвечу вам в ближайшее время.",
    parse_mode="HTML"
)

# 2. Ваш ответ на пересланное сообщение -> отправляем клиенту
@router.message(F.reply_to_message & (F.from_user.id == ADMIN_ID_INT))
async def reply_to_user(message: Message, bot: Bot):
    if message.reply_to_message.forward_from:
        target_user_id = message.reply_to_message.forward_from.id
        await bot.send_message(
            chat_id=target_user_id,
            text=f"👩‍🍳 <b>Ответ кондитера:</b>\n\n{message.text}"
        )
        await message.answer("✅ Ответ успешно отправлен клиенту!")
    else:
        await message.answer("⚠️ Не удалось определить получателя (возможно, у пользователя скрыт профиль).")