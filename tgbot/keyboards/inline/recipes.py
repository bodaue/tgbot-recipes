from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.db.models.recipe import RecipeCategory, Recipe


class RecipeCategoryCallbackData(CallbackData, prefix='recipe_category'):
    category_id: int


async def recipe_categories_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    categories = await RecipeCategory.all()
    for category in categories:
        builder.row(
            InlineKeyboardButton(text=category.name,
                                 callback_data=RecipeCategoryCallbackData(category_id=category.id).pack())
        )
    return builder.as_markup()


class RecipeCallbackData(CallbackData, prefix='recipe'):
    recipe_id: int


async def recipes_keyboard(category_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    recipes = await Recipe.filter(category_id=category_id).all()
    for recipe in recipes:
        builder.row(
            InlineKeyboardButton(text=recipe.title,
                                 callback_data=RecipeCallbackData(recipe_id=recipe.id).pack())
        )
    # todo: back to categories list

    return builder.as_markup()


async def current_recipe_keyboard(recipe: Recipe) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    # maybe error: recipe.category is not int
    builder.row(
        InlineKeyboardButton(text="Назад",
                             callback_data=RecipeCategoryCallbackData(category_id=recipe.category).pack())
    )
    return builder.as_markup()
