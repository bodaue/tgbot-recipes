from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "recipe_categories" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS "recipes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "title" VARCHAR(255) NOT NULL UNIQUE,
    "description" TEXT NOT NULL,
    "ingredients" TEXT NOT NULL,
    "preparation_time" BIGINT NOT NULL,
    "category_id" INT NOT NULL REFERENCES "recipe_categories" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "sent_recipes" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "recipe_id" INT NOT NULL UNIQUE REFERENCES "recipes" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "users" (
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "username" VARCHAR(255)
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
