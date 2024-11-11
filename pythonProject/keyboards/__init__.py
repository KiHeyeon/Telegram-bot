__all__=("router", )
from aiogram import Router
from .grades_keyboard import router as grades_keyboard_router
router = Router()
router.include_router(grades_keyboard_router)