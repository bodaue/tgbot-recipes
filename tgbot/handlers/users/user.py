from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.handlers.users.recipes import recipe_router
from tgbot.keyboards.reply.start import start_keyboard

user_router = Router()
user_router.message.filter(F.chat.type == "private")
user_router.callback_query.filter(F.message.chat.type == "private")

user_router.include_routers(recipe_router)


@user_router.message(CommandStart(), flags={"throttling_key": "default"})
async def user_start(message: Message, state: FSMContext):
    name = message.from_user.first_name
    await message.answer(
        text=f"<b>Привет, {name}!</b>\n" f"Используй клавиатуру для работы с ботом ⬇️",
        reply_markup=start_keyboard(),
    )
    await state.clear()
