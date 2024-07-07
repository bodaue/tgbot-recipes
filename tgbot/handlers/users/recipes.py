from aiogram import Router, F, html
from aiogram.types import Message, CallbackQuery

from tgbot.db.models.recipe import Recipe
from tgbot.keyboards.inline.recipes import recipe_categories_keyboard, RecipeCategoryCallbackData, recipes_keyboard, \
    RecipeCallbackData, current_recipe_keyboard

recipe_router = Router()


@recipe_router.message(F.text == 'Рецепты')
async def get_recipe_categories(message: Message):
    await message.answer(text=html.bold('Выберите категорию рецептов'),
                         reply_markup=await recipe_categories_keyboard())


@recipe_router.callback_query(RecipeCategoryCallbackData.filter())
async def get_recipes(callback: CallbackQuery,
                      callback_data: RecipeCategoryCallbackData):
    await callback.message.edit_text(
        text=html.bold('Выберите рецепт'),
        reply_markup=await recipes_keyboard(callback_data.category_id)
    )


@recipe_router.callback_query(RecipeCallbackData.filter())
async def get_recipe_details(callback: CallbackQuery,
                             callback_data: RecipeCallbackData):
    recipe = await Recipe.get(id=callback_data.recipe_id)
    await callback.message.edit_text(
        text=recipe.get_full_description(),
        reply_markup=await current_recipe_keyboard(recipe=recipe)
    )
