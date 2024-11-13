from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
router = Router(name=__name__)


class Btn:
    ONES="*174"
    ONEF="*141"
    ZERO="*051"
    ZEROS="*071"
    TWOF = "*241"
    ONEE = "*181"
    ONET = "*122"
    ONETW = "*123"
    ZEROSEV = "*075"
    SEVENTHREE = "*073"
    TWOE = "*281"
    ONEFO = "*142"
    ONE = "*131"
    ONETH = "*133"
    ONEZ = "*101"
    ONEEI = "*183"
    ONEEIG = "*185"
    ONEFOU = "*144"
    TWOFOO = "*242"
    ZE = "*076"

def get_mas_kb() -> ReplyKeyboardMarkup:
    btton_174 = KeyboardButton(text=Btn.ONES)
    btton_141 = KeyboardButton(text=Btn.ONEF)
    btton_051 = KeyboardButton(text=Btn.ZERO)
    btton_071 = KeyboardButton(text=Btn.ZEROS)

    btton_241 = KeyboardButton(text=Btn.TWOF)
    btton_181 = KeyboardButton(text=Btn.ONEE)
    btton_122 = KeyboardButton(text=Btn.ONET)
    btton_123 = KeyboardButton(text=Btn.ONETW)

    btton_075 = KeyboardButton(text=Btn.ZEROSEV)
    btton_073 = KeyboardButton(text=Btn.SEVENTHREE)
    btton_281 = KeyboardButton(text=Btn.TWOE)
    btton_142 = KeyboardButton(text=Btn.ONEFO)

    btton_131 = KeyboardButton(text=Btn.ONE)
    btton_133 = KeyboardButton(text=Btn.ONETH)
    btton_101 = KeyboardButton(text=Btn.ONEZ)
    btton_183 = KeyboardButton(text=Btn.ONEEI)

    btton_185 = KeyboardButton(text=Btn.ONEEIG)
    btton_144 = KeyboardButton(text=Btn.ONEFOU)
    btton_242 = KeyboardButton(text=Btn.TWOFOO)
    btton_076 = KeyboardButton(text=Btn.ZE)

    bttons_first_row = [btton_174, btton_141, btton_051, btton_071]
    bttons_second_row = [btton_241, btton_181, btton_122, btton_123]
    bttons_third_row = [btton_075, btton_073, btton_281, btton_142]
    bttons_fourth_row = [btton_131,btton_133, btton_101, btton_183]
    bttons_fifth_row = [btton_185, btton_144, btton_242, btton_076]


    keyboard = ReplyKeyboardMarkup(
        keyboard=[bttons_first_row, bttons_second_row, bttons_third_row, bttons_fourth_row, bttons_fifth_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard
