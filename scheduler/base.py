from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.base import BaseScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler_di import ContextSchedulerDecorator
from tzlocal import get_localzone

from scheduler.tasks import notify_users_about_recipe
from tgbot.config import config
from tgbot.db.db import init_db


def schedule_tasks(scheduler: BaseScheduler):
    scheduler.add_job(func=notify_users_about_recipe,
                      trigger=CronTrigger(day_of_week='mon', hour=9, minute=0))


async def setup_scheduler():
    bot = Bot(token=config.common.bot_token.get_secret_value(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    scheduler = ContextSchedulerDecorator(
        AsyncIOScheduler(timezone=str(get_localzone()))
    )
    scheduler.ctx.add_instance(bot, declared_class=Bot)

    await init_db()

    return scheduler
