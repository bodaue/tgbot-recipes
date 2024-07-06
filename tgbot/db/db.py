from tortoise import Tortoise

from tgbot.config import config

TORTOISE_ORM = {
    "connections": {"default": config.db.dsn},
    "apps": {
        "models": {
            "models": ["tgbot.db.models"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
