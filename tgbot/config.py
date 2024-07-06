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


class Config(BaseModel):
    common: CommonConfig
    db: DBConfig


def create_app_config() -> Config:
    return Config(
        common=CommonConfig(),
        db=DBConfig(),
    )


config = create_app_config()
