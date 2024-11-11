from aiogram import Router
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
router = Router(name=__name__)

class ButtonText:
    ONESEVENFOUR="174"
    ONEFOURONE="141"
    ZEROFIVEONE="051"
    ZEROSEVENONE="071"
    ZEROSEVENTWO ="072"
    TWOFOURONE = "241"
    ONEEIGHTONE = "181"
    ZEROTHREEFIVE = "035"
    ONETWOTWO = "122"
    ONETWOTHREE = "123"
    ZEROSEVENFIVE = "075"
    ZEROSEVENTHREE = "073"
    TWOEIGHTONE = "281"
    ONEFOURTWO = "142"
    ONETHREEONE = "131"
    ONETHREETHREE = "133"
    ONEZEROONE = "101"
    ONEEIGHTTHREE = "183"
    ONEEIGHTFIVE = "185"
    ONEFOURFOUR = "144"
    ONEFOURFIVE = "145"
    TWOFOURTWO = "242"
    ZEROSEVENSIX = "076"
    TWOZEROFOUR = "204"
    ONESIXTWO = "162"

def get_on_grades_kb() -> ReplyKeyboardMarkup:
    button_174 = KeyboardButton(text=ButtonText.ONESEVENFOUR)
    button_141 = KeyboardButton(text=ButtonText.ONEFOURONE)
    button_051 = KeyboardButton(text=ButtonText.ZEROFIVEONE)
    button_071 = KeyboardButton(text=ButtonText.ZEROSEVENONE)

    button_072 = KeyboardButton(text=ButtonText.ZEROSEVENTWO)
    button_241 = KeyboardButton(text=ButtonText.TWOFOURONE)
    button_181 = KeyboardButton(text=ButtonText.ONEEIGHTONE)
    button_035 = KeyboardButton(text=ButtonText.ZEROTHREEFIVE)

    button_122 = KeyboardButton(text=ButtonText.ONETWOTWO)
    button_123 = KeyboardButton(text=ButtonText.ONETWOTHREE)
    button_075 = KeyboardButton(text=ButtonText.ZEROSEVENFIVE)
    button_073 = KeyboardButton(text=ButtonText.ZEROSEVENTHREE)

    button_281 = KeyboardButton(text=ButtonText.TWOEIGHTONE)
    button_142 = KeyboardButton(text=ButtonText.ONEFOURTWO)
    button_131 = KeyboardButton(text=ButtonText.ONETHREEONE)
    button_133 = KeyboardButton(text=ButtonText.ONETHREETHREE)

    button_101 = KeyboardButton(text=ButtonText.ONEZEROONE)
    button_183 = KeyboardButton(text=ButtonText.ONEEIGHTTHREE)
    button_185 = KeyboardButton(text=ButtonText.ONEEIGHTFIVE)
    button_144 = KeyboardButton(text=ButtonText.ONEFOURFOUR)

    button_145 = KeyboardButton(text=ButtonText.ONEFOURFIVE)
    button_242 = KeyboardButton(text=ButtonText.TWOFOURTWO)
    button_076 = KeyboardButton(text=ButtonText.ZEROSEVENSIX)
    button_204 = KeyboardButton(text=ButtonText.TWOZEROFOUR)

    button_162 = KeyboardButton(text=ButtonText.ONESIXTWO)

    buttons_first_row = [button_174, button_141, button_051, button_071, button_072]
    buttons_second_row = [button_241, button_181, button_035, button_122, button_123]
    buttons_third_row = [button_075, button_073, button_281, button_142, button_131]
    buttons_fourth_row = [button_133, button_101, button_183, button_185, button_144]
    buttons_fifth_row = [button_145, button_242, button_076, button_204, button_162]


    keyboard = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row, buttons_third_row, buttons_fourth_row, buttons_fifth_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return keyboard


