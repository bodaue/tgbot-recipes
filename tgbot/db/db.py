from tortoise import Tortoise


def get_tortoise_orm_config(host: str) -> dict:
    return {
        "connections": {"default": host},
        "apps": {
            "models": {
                "models": ["tgbot.db.models"],
                "default_connection": "default",
            },
        },
    }


async def init_db(host: str) -> None:
    await Tortoise.init(config=get_tortoise_orm_config(host=host))
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()
