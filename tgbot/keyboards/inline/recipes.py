from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.db.models.recipe import RecipeCategory, Recipe


class RecipeCategoryCallbackData(CallbackData, prefix='recipe_category'):
    category_id: int


def recipe_categories_keyboard(categories: list[RecipeCategory]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for category in categories:
        builder.row(
            InlineKeyboardButton(text=category.name,
                                 callback_data=RecipeCategoryCallbackData(category_id=category.id).pack())
        )
    return builder.as_markup()


class RecipeCallbackData(CallbackData, prefix='recipe'):
    recipe_id: int


def recipes_keyboard(recipes: list[Recipe]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for recipe in recipes:
        builder.row(
            InlineKeyboardButton(text=recipe.title,
                                 callback_data=RecipeCallbackData(recipe_id=recipe.id).pack())
        )
    builder.row(
        InlineKeyboardButton(text="Назад",
                             callback_data="back_to_recipe_categories")
    )
    return builder.as_markup()


def current_recipe_keyboard(recipe: Recipe) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    # maybe error: recipe.category is not int
    builder.row(
        InlineKeyboardButton(text="Назад",
                             callback_data=RecipeCategoryCallbackData(category_id=recipe.category_id).pack())
    )
    return builder.as_markup()
