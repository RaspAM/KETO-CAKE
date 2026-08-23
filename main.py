import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiohttp import web
from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.catalog import router as catalog_router
from handlers.keto_info import router as keto_info_router
from handlers.feedback import router as feedback_router

logging.basicConfig(level=logging.INFO)

async def set_main_menu(bot: Bot):
    await bot.delete_my_commands()
    commands = [
        BotCommand(command="start", description="Торты Правильного Питания и КЕТО"),
        BotCommand(command="catalog", description="Образцы тортов и КЖБУ"),
        BotCommand(command="info", description="Узнать о пользе КЕТО и ПП"),
        BotCommand(command="custom", description="Создайте свой вкус"),
        BotCommand(command="feedback", description="Отзывы / Оставить отзыв"),
        BotCommand(command="contacts", description="Связаться со мной"),
    ]
    await bot.set_my_commands(commands)

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

    await set_main_menu(bot)

    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(keto_info_router)
    dp.include_router(feedback_router)

    await start_health_check_server()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
