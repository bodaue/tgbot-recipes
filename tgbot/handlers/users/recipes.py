from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery

from tgbot.db.models.recipe import Recipe, RecipeCategory
from tgbot.keyboards.inline.recipes import (recipe_categories_keyboard, RecipeCategoryCallbackData, recipes_keyboard,
                                            RecipeCallbackData, current_recipe_keyboard)

recipe_router = Router()


@recipe_router.message(F.text == 'Рецепты')
async def get_recipe_categories(message: Message):
    recipe_categories = await RecipeCategory.all()
    if not recipe_categories:
        return await message.answer(text='Список рецептов пуст.')

    await message.answer(
        text=html.bold('Выберите категорию рецептов'),
        reply_markup=recipe_categories_keyboard(recipe_categories)
    )


@recipe_router.callback_query(F.data == 'back_to_recipe_categories')
async def back_to_recipe_categories(call: CallbackQuery):
    recipe_categories = await RecipeCategory.all()
    if not recipe_categories:
        return await call.answer(text='Список рецептов пуст.')

    await call.message.edit_text(
        text=html.bold('Выберите категорию рецептов'),
        reply_markup=recipe_categories_keyboard(categories=recipe_categories)
    )


@recipe_router.callback_query(RecipeCategoryCallbackData.filter())
async def get_recipes(call: CallbackQuery,
                      callback_data: RecipeCategoryCallbackData):
    recipes = await Recipe.filter(category_id=callback_data.category_id).all()
    if not recipes:
        return await call.answer(text='Рецепты в этой категории отсутствуют.')

    await call.message.edit_text(
        text=html.bold('Выберите рецепт'),
        reply_markup=recipes_keyboard(recipes=recipes)
    )


@recipe_router.callback_query(RecipeCallbackData.filter())
async def get_recipe_details(call: CallbackQuery,
                             callback_data: RecipeCallbackData):
    recipe = await Recipe.get(id=callback_data.recipe_id)
    await call.message.edit_text(
        text=recipe.get_details(),
        reply_markup=current_recipe_keyboard(recipe=recipe)
    )
