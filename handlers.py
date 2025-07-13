from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from generate import ai_generate
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
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode='Markdown') #markdown
    await state.clear()