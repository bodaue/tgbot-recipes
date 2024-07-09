from pydantic import SecretStr, BaseModel
from pydantic_settings import SettingsConfigDict, BaseSettings as _BaseSettings


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore", env_file='.env', env_file_encoding="utf-8"
    )


class CommonConfig(BaseSettings, env_prefix="COMMON_"):
    bot_token: SecretStr
    admins: list[int]


class DBConfig(BaseSettings, env_prefix="DB_"):
    username: str
    password: SecretStr
    name: str
    host: str
    port: str
    driver: str

    def build_dsn(self) -> str:
        return f"{self.driver}://{self.username}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"


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
