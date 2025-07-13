from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import generate
import os
from dotenv import load_dotenv

load_dotenv()

router = Router()

RID = int(os.getenv("RID"))
LID = int(os.getenv("LID"))

class Gen(StatesGroup):
    wait = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    await message.answer("Привет 😎, \nя 🐋💨")

@router.message(Gen.wait)
async def stop_flood(message: Message):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    await message.answer("Дожитесь выполнения запроса😡")

@router.message(Command("ask"))
async def generating(message: Message, state: FSMContext):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    await state.set_state(Gen.wait)
    await message.answer("Мяу генерирую 🐾😊🐾")
    response = await generate.ai_generate(message.text.removeprefix("/ask").strip())
    await message.answer(response, parse_mode='Markdown') #markdown
    await state.clear()

@router.message(Command("context"))
async def cmd_context(message: Message):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    await message.answer(generate.user_context)

@router.message(Command("default_context"))
async def cmd_context(message: Message):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    generate.make_default_context()
    await message.answer(generate.user_context)

@router.message(Command("edit_context"))
async def cmd_context(message: Message):
    if message.from_user.id != RID and message.from_user.id != LID:
        return
    success = generate.edit_context(message.text.removeprefix("/edit_context").strip())
    if success:
        await message.answer("✅ Контекст обновлён.")
    else:
        await message.answer("❌ Новый контекст слишком длинный.\n" + str(generate.lctx) + " > 256")

    await message.answer(generate.user_context)
