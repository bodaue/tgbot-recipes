from tortoise import Tortoise

from tgbot.config import config

TORTOISE_ORM = {
    "connections": {"default": config.db.build_dsn()},
    "apps": {
        "models": {
            "models": ["tgbot.db.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db() -> None:
    await Tortoise.init(config=TORTOISE_ORM)
    # await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()
