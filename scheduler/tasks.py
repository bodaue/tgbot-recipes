import logging

from aiogram import Bot
from aiogram.exceptions import TelegramAPIError

from tgbot.db.models import Recipe, User
from tgbot.db.models.recipe import SentRecipe


async def notify_users_about_recipe(bot: Bot) -> None:
    recipe = await Recipe.filter(sent__isnull=True).first()
    if not recipe:
        return

    users = await User.all()
    text = "<b>Уведомление о рецепте!</b>\n\n" "" "{}".format(recipe.get_details())
    for user in users:
        try:
            await bot.send_message(chat_id=user.id, text=text)
        except TelegramAPIError as e:
            logging.error(f"Error sending message to user {user.id}: {e}")

    await SentRecipe.create(recipe=recipe)
