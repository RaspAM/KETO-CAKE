import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiohttp import web
from config import BOT_TOKEN

# Прямой точечный импорт роутеров из модулей
from handlers.start import router as start_router
from handlers.catalog import router as catalog_router
from handlers.keto_info import router as keto_info_router
from handlers.reviews import router as reviews_router

logging.basicConfig(level=logging.INFO)

# Установка команд в левое синее меню Telegram
async def set_main_menu(bot: Bot):
    commands = [
        BotCommand(command="start", description="Главное меню / Перезапуск"),
        BotCommand(command="catalog", description="🍰 Каталог десертов и КБЖУ"),
        BotCommand(command="info", description="🌱 О КЕТО и ПП десертах"),
        BotCommand(command="reviews", description="💬 Отзывы и предложения"),
        BotCommand(command="contacts", description="📍 Контакты и Заказ"),
    ]
    await bot.set_my_commands(commands)

# Сервер проверки работоспособности для Render
async def handle_ping(request):
    return web.Response(text="Bot is alive!")

async def start_health_check_server():
    app = web.Application()
    app.router.add_get("/", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Регистрируем меню в Telegram
    await set_main_menu(bot)

    # Подключаем роутеры команд и кнопок напрямую
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(keto_info_router)
    dp.include_router(reviews_router)

    # Запускаем фоновый веб-сервер для Render
    await start_health_check_server()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
