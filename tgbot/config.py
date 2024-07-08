from pydantic import SecretStr, BaseModel
from pydantic_settings import BaseSettings as _BaseSettings, SettingsConfigDict


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8"
    )


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr
    admins: list[int]


class DBConfig(BaseSettings, env_prefix="DB_"):
    host: str

    @property
    def dsn(self):
        return self.host


class RedisConfig(BaseSettings, env_prefix='REDIS_'):
    use_redis: bool = False

    host: str
    port: int
    password: str


class Config(BaseModel):
    common: CommonConfig
    db: DBConfig
    redis: RedisConfig


def create_app_config() -> Config:
    return Config(
        common=CommonConfig(),
        db=DBConfig(),
        redis=RedisConfig()
    )


config = create_app_config()
