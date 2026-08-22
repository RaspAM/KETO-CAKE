import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiohttp import web
from config import BOT_TOKEN
from handlers import start, catalog, keto_info, reviews

logging.basicConfig(level=logging.INFO)

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

    # Подключаем роутеры команд и кнопок
    dp.include_router(start.router)
    dp.include_router(catalog.router)
    dp.include_router(keto_info.router)
    dp.include_router(reviews.router)

    # Запускаем фоновый веб-сервер для Render
    await start_health_check_server()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())