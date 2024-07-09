from tortoise import Tortoise


def get_tortoise_orm_config(dsn: str) -> dict:
    return {
        "connections": {"default": dsn},
        "apps": {
            "models": {
                "models": ["tgbot.db.models"],
                "default_connection": "default",
            },
        },
    }


async def init_db(dsn: str) -> None:
    await Tortoise.init(config=get_tortoise_orm_config(dsn=dsn))
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
