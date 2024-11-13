import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import F, Router,  types

from aiogram.filters import Command, CommandStart
from aiogram.enums import ParseMode
from aiogram.utils import markdown
from keyboards.grades_keyboard import ButtonText, get_on_grades_kb
from keyboards.rules_keyboard import Btn, get_mas_kb
from aiogram.types import ReplyKeyboardRemove, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8012186305:AAEiaRxW2J-fIZ8wvUZncgOE2-6vX6w7wSQ"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
router = Router()

dp.include_router(router)

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://ftml.nau.edu.ua/wp-content/uploads/posv-ftml1.jpg"
    # Приветственное сообщение
    welcome_text = (
        f"{markdown.hide_link(url)}Привіт, {markdown.hbold(message.from_user.username)}!\n\n"
        "<b>Вас вітає Одеський національний технологічний університет (ОНТУ)!</b>\n\n"
        "Ми раді бачити Вас серед потенційних абітурієнтів. У нашому університеті діють численні інститути, які забезпечують якісну підготовку за різними напрямами. Нижче наведені основні інститути:\n\n"
        "1. Навчально-науковий інститут харчових технологій ім. М.О. Грішина\n"
        "2. Навчально-науковий інститут зернового, переробного і хлібопекарського бізнесу ім. К.А. Богомаза\n"
        "3. Навчально-науковий інститут комп'ютерної інженерії, автоматизації, роботехніки та програмування ім. П.М.Платонова\n"
        "4. Навчально-науковий інститут готельно-ресторанного і туристичного бізнесу та енології ім. О.О. Преображенського\n"
        "5. Навчально-науковий інститут економіки, управління і бізнесу ім. Г.Е. Вейнштейна\n"
        "6. Навчально-науковий інститут холоду, кріотехнології та екоенергетики ім. В.С. Мартиновського\n"
        "Для отримання додаткової інформації про конкретний інститут, оберіть відповідний розділ у меню."
    )

    # Отправка сообщения с приветствием и информацией о институтах
    await message.answer(

        text=welcome_text,
        parse_mode=ParseMode.HTML
    )

@dp.message(Command("grades", prefix="!/"))
async def handle_grades_command(message: types.Message):
    grades_file_btn = InlineKeyboardButton(
        text="Файл",
        url="https://pk.ontu.edu.ua/modules/Download/pub_dir/Dodatoki5igotovivstavitikoefipoipredmetam.pdf",
    )
    ch_depart_btn = InlineKeyboardButton(
        text="За вибором", callback_data="ch_depart"
    )
    row = [grades_file_btn, ch_depart_btn]
    rows = [row]
    markup =InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Натисніть 'Файл' для перегляду інформації по всім спеціальностям.Натисніть 'За вибором' для перегляду спеціальностей за вибором.",
        reply_markup=markup,
    )



@router.callback_query(lambda c: c.data == "ch_depart")
async def show_depart(callback_query: types.CallbackQuery):
    # Отправляем уже созданную клавиатуру get_on_grades_kb()
    await bot.send_message(
        callback_query.from_user.id,
        text="Оберіть номер спеціальності для отримання інформації:",
        reply_markup=get_on_grades_kb()
    )
    await callback_query.answer()

@dp.message(F.text == ButtonText.ONESEVENFOUR)
async def handle_o_message(message: types.Message):
    specialty_number = "174"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Автоматизація, комп'ютерно-інтегровані технології и робототехніка.\n"
        "*Освітня програма*: Комп'ютерні системи та програмна інженерія в автоматизації и робототехніці.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        46\n"
        "*Заочна форма навчання*:       6\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEFOURONE)
async def handle_n_message(message: types.Message):
    specialty_number = "141"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Електроенергетика, електротехніка та електромеханіка.\n"
        "*Освітня програма*:\n"
        "*1.*: Екоенергетика та інтелектуальна електромеханіка.\n"
        "*2.*: Нетрадиційні та відновлювальні джерела енергії.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        16\n"
        "*Заочна форма навчання*:       6\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROFIVEONE)
async def handle_e_message(message: types.Message):
    specialty_number = "051"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Економіка.\n"
        "*Освітня програма*:\n"
        "*1.* Економіка підприємства. \n"
        "*2.* Економічна та продовольча безпека.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        45\n"
        "*Заочна форма навчання*:       20\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROSEVENONE)
async def handle_on_message(message: types.Message):
    specialty_number = "071"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Облік і оподаткування.\n"
        "*Освітня програма*:\n"
        "*1.*  Облік і аудит. \n"
        "*2.* Облік і аудит в готельно-ресторанному бізнесі та торгівлі.\n"
        "*3.* Діджитал-облік і контроль.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        45\n"
        "*Заочна форма навчання*:       25\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROSEVENTWO)
async def handle_ne_message(message: types.Message):
    specialty_number = "072"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Фінанси, банківська справа, страхування та фондовий ринок.\n"
        "*Освітня програма*: Фінанси, банківська справа, страхування та фондовий ринок. \n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        15\n"
        "*Заочна форма навчання*:       10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.TWOFOURONE)
async def handle_one_message(message: types.Message):
    specialty_number = "241"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Готельно-ресторанна справа.\n"
        "*Освітня програма*: Готельно-ресторанна справа. \n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,4   \n"
        "Математика                    К2    0,3   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,5  \n"
        "Біологія                            К4    0,3   \n"
        "Фізика                               К4    0,25   \n"
        "Хімія                                  К4    0,3   \n"
        "Українська література  К4    0,3   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        100\n"
        "*Заочна форма навчання*:       75\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEEIGHTONE)
async def handle_t_message(message: types.Message):
    specialty_number = "181"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Харчові технології.\n"
        "*Освітня програма*: Технології ресторанного бізнесу та здорового харчування. \n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,3  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,5   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        120\n"
        "*Заочна форма навчання*:       21\n"
        "*Освітня програма*: Технології продуктів бродіння, напоїв та виноробства. \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        48\n"
        "*Заочна форма навчання*:       5\n"
        "*Освітня програма*:\n"
        "*1.* Технології зберігання і переробки зерна.\n"
        "*2.*Технології хліба, кондитерських, макаронних виробів та харчоконцентратів\n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        75\n"
        "*Заочна форма навчання*:       35\n"
        "*Освітня програма*:\n"
        "*1.* Технологічна експертиза та безпека харчової продукції.\n"
        "*2.* Технології м'ясних і рибних продуктів.\n"
        "*3.* Технології молока, жирів і продуктів для індустрії краси.\n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        85\n"
        "*Заочна форма навчання*:       35\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROTHREEFIVE)
async def handle_w_message(message: types.Message):
    specialty_number = "035"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Філологія.\n"
        "*Освітня програма*: Філологія: романські мови та літератури (переклад включно), перша - французька. \n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,4   \n"
        "Математика                    К2    0,3   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,4  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,4   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        15\n"
        "*Заочна форма навчання*:       15\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONETWOTWO)
async def handle_tw_message(message: types.Message):
    specialty_number = "122"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Комп'ютерні науки.\n"
        "*Освітня програма*:\n"
        "*1.* Інформаційні технології проектування.\n"
        "*2.* Інформаційні управляючі системи та технології.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,3  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,4   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        52\n"
        "*Заочна форма навчання*:       10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONETWOTHREE)
async def handle_wo_message(message: types.Message):
    specialty_number = "123"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Комп'ютерна інженерія.\n"
        "*Освітня програма*:\n"
        "*1.* Розробка ігор та інтерактивних медіа у віртуальній реальності.\n"
        "*2.* Мережеві технології та інтернет речей.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,3  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,4   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        55\n"
        "*Заочна форма навчання*:       10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROSEVENFIVE)
async def handle_two_message(message: types.Message):
    specialty_number = "075"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Маркетинг.\n"
        "*Освітня програма*: Маркетинг та digital-комунікації.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        43\n"
        "*Заочна форма навчання*:       20\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROSEVENTHREE)
async def handle_th_message(message: types.Message):
    specialty_number = "073"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Менеджмент.\n"
        "*Освітня програма*:\n"
        "*1.*: Менеджмент.\n"
        "*2.*: Управління персоналом.\n"
        "*3.*: Психологія управління.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        112\n"
        "*Заочна форма навчання*:       38\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.TWOEIGHTONE)
async def handle_hr_message(message: types.Message):
    specialty_number = "281"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Публічне управління та адміністрування.\n"
        "*Освітня програма*: Публічне управління та адміністрування.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,5  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        35\n"
        "*Заочна форма навчання*:       10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEFOURTWO)
async def handle_re_message(message: types.Message):
    specialty_number = "142"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Енергетичне машинобудування.\n"
        "*Освітня програма*: Холодильні машини, установки і кондиціювання повітря.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        52\n"
        "*Заочна форма навчання*:       15\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONETHREEONE)
async def handle_ree_message(message: types.Message):
    specialty_number = "131"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Прикладна механіка.\n"
        "*Освітня програма*: Інженерна механіка.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        17\n"
        "*Заочна форма навчання*:        5\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONETHREETHREE)
async def handle_hre_message(message: types.Message):
    specialty_number = "133"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Галузеве машинобудування.\n"
        "*Освітня програма*: Енергетичний менеджмент та ІТ-сервіс обладнання.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        12\n"
        "*Заочна форма навчання*:        -\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEZEROONE)
async def handle_hree_message(message: types.Message):
    specialty_number = "101"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Екологія.\n"
        "*Освітня програма*: Екологія.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,35   \n"
        "Історія України               К3    0,35   \n"
        "Іноземна мова               К4    0,3  \n"
        "Біологія                            К4    0,4   \n"
        "Фізика                               К4    0,35   \n"
        "Хімія                                  К4    0,4   \n"
        "Українська література  К4    0,3   \n"
        "Географія                         К4    0,4   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        20\n"
        "*Заочна форма навчання*:        9\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEEIGHTTHREE)
async def handle_three_message(message: types.Message):
    specialty_number = "183"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Технології захисту навколишнього середовища.\n"
        "*Освітня програма*: Технології захисту навколишнього середовища.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,5   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,5   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        10\n"
        "*Заочна форма навчання*:        6\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEEIGHTFIVE)
async def handle_thre_message(message: types.Message):
    specialty_number = "185"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Нафтогазова інженерія та технології.\n"
        "*Освітня програма*: Нафтогазова інженерія та технології.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,5   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,5   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        35\n"
        "*Заочна форма навчання*:        15\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEFOURFOUR)
async def handle_f_message(message: types.Message):
    specialty_number = "144"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Теплоенергетика.\n"
        "*Освітня програма*: Енергетичний інжиніринг та енергоаудит.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        10\n"
        "*Заочна форма навчання*:        4\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONEFOURFIVE)
async def handle_fr_message(message: types.Message):
    specialty_number = "145"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Відновлювальні джерела енергії та гідроенергетика.\n"
        "*Освітня програма*: Екоенергетика і теплотехнології.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,3   \n"
        "Математика                    К2    0,5   \n"
        "Історія України               К3    0,2   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,2   \n"
        "Географія                         К4    0,2   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        16\n"
        "*Заочна форма навчання*:        0\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.TWOFOURTWO)
async def handle_fo_message(message: types.Message):
    specialty_number = "242"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Туризм і рекреація.\n"
        "*Освітня програма*: Міжнародний туризм.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,4   \n"
        "Математика                    К2    0,3   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,5  \n"
        "Біологія                            К4    0,35   \n"
        "Фізика                               К4    0,25   \n"
        "Хімія                                  К4    0,25   \n"
        "Українська література  К4    0,3   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        80\n"
        "*Заочна форма навчання*:        20\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ZEROSEVENSIX)
async def handle_ou_message(message: types.Message):
    specialty_number = "076"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Підприємництво та торгівля.\n"
        "*Освітня програма*: Підприємництво і торгівля, товарознавство та експертиза в митній справі.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,4   \n"
        "Історія України               К3    0,25   \n"
        "Іноземна мова               К4    0,25  \n"
        "Біологія                            К4    0,2   \n"
        "Фізика                               К4    0,2   \n"
        "Хімія                                  К4    0,2   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,35   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        25\n"
        "*Заочна форма навчання*:        10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.TWOZEROFOUR)
async def handle_our_message(message: types.Message):
    specialty_number = "204"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Технологія виробництва і переробки продукції тваринництва.\n"
        "*Освітня програма*: Технологія виробництва і переробки продукції тваринництва.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,4   \n"
        "Математика                    К2    0,3   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,35  \n"
        "Біологія                            К4    0,5   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,5   \n"
        "Українська література  К4    0,3   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  +\n"
        "\n*Ліцензії на кількість місць*\n"
        "*Денна форма навчання*:        25\n"
        "*Заочна форма навчання*:        10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == ButtonText.ONESIXTWO)
async def handle_ur_message(message: types.Message):
    specialty_number = "162"
    specialty_info = (
        f"Код: {specialty_number}\n"
        "*Назва спеціальності*: Біотехнології та біоінженерія.\n"
        "*Освітня програма*: Біотехнології та біоінженерія.\n"
        "*Конкурсні предмети*   *Вага предметів*\n"
        "Українська мова            K1    0,35   \n"
        "Математика                    К2    0,35   \n"
        "Історія України               К3    0,3   \n"
        "Іноземна мова               К4    0,3  \n"
        "Біологія                            К4    0,5   \n"
        "Фізика                               К4    0,5   \n"
        "Хімія                                  К4    0,5   \n"
        "Українська література  К4    0,25   \n"
        "Географія                         К4    0,3   \n"
        "*Бал за підготовчі курси ОУ*:  -\n"
        "\n*Ліцензії на кількість місць*\n" 
        "*Денна форма навчання*:        25\n"
        "*Заочна форма навчання*:        10\n"
    )
    await message.answer(
        text=specialty_info,
        reply_markup=get_navigation_buttons(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )


@router.callback_query(lambda c: c.data == "see_more")
async def see_more_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        callback_query.from_user.id,
        text="Виберіть номер спеціальності:",
        reply_markup=get_on_grades_kb()
    )
    await callback_query.answer()

@dp.message(Command("rules", prefix="!/"))
async def handle_rules(message: types.Message):
    rul_bac_btn = InlineKeyboardButton(
        text="Бакалавр",
        callback_data="rul_bac",
    )
    rul_mas_btn = InlineKeyboardButton(
        text="2-га освіта: Бакалавр та Магістр",
        callback_data="master_two",
    )
    rul_more_btn = InlineKeyboardButton(
        text="Більше інформації тут",
        url="https://pk.ontu.edu.ua/_pravila.html#file_1202",
    )
    rows = [
        [rul_bac_btn],
        [rul_mas_btn],
        [rul_more_btn],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Правила прийому для здобуття вищої освіти",
        reply_markup=markup,
    )


@router.callback_query(F.data.in_({"rul_bac"}))
async def handle_degree_choice(callback_query: CallbackQuery):
    rul_type = callback_query.data
    full_time_btn = InlineKeyboardButton(
        text="Денна форма навчання",
        callback_data=f"{rul_type}_full_time"
    )
    part_time_btn = InlineKeyboardButton(
        text="Заочна форма навчання",
        callback_data=f"{rul_type}_part_time",
    )
    rows = [
        [full_time_btn],
        [part_time_btn],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await callback_query.message.answer(
        text="Виберіть форму навчання:",
        reply_markup=markup,
    )
    await callback_query.answer()

@router.callback_query(
    F.data.in_({"rul_bac_full_time", "rul_bac_part_time"}))
async def handle_study_form(callback_query: CallbackQuery):
    if callback_query.data == "rul_bac_full_time":
        text = ("Ви обрали: <b>Бакалавр, Денна форма навчання</b>.\n"
        "Скорочений термін навчання - 1 рік 10 місяців:\n"
         "<b>І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб.</b>\n"
        "1. Мотиваційний лист.\n"
        "2. НМТ 2024 року з чотирьох конкурсних предметів (перший, другий, третій, четвертий предмети) або НМТ 2023 року, або НМТ 2022 року з трьох конкурсних предметів (перший, другий, третій предмети) або ЗНО 2021 року з двох конкурсних предметів (перший, другий предмети) або матурального іспиту з двох основних предметів (польська мова, математика) та двох додаткових предметів (історія, іноземна мова, або біологія, або фізика та астрономія, або хімія за вибором вступника) для громадян Республіки Польща\n"
        "\n\n<b>Скорочений термін навчання - 2 роки 10 місяців:</b>\n"
        "<b>І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб.</b>\n"
        "1. Мотиваційний лист.\n"
        "2. НМТ 2024 року з чотирьох конкурсних предметів (перший, другий, третій, четвертий предмети) або НМТ 2023 року, або НМТ 2022 року з трьох конкурсних предметів (перший, другий, третій предмети) або ЗНО 2021 року з двох конкурсних предметів (перший, другий предмети) або матурального іспиту з двох основних предметів (польська мова, математика) та двох додаткових предметів (історія, іноземна мова, або біологія, або фізика та астрономія, або хімія за вибором вступника) для громадян Республіки Польща\n"
        )
    elif callback_query.data == "rul_bac_part_time":
        text = ("Ви обрали: <b>Бакалавр, Заочна форма навчання.</b>\n"
        "Скорочений термін навчання - 1 рік 10 місяців:\n"
        "<b>І. Участь у конкурсному відборі при вступі на навчання за кошти фізичних та/або юридичних осіб.</b>\n"
        "1. Мотиваційний лист.\n"
        "2. НМТ 2024 року з чотирьох конкурсних предметів (перший, другий, третій, четвертий предмети) або НМТ 2023 року, або НМТ 2022 року з трьох конкурсних предметів (перший, другий, третій предмети) або ЗНО 2021 року з двох конкурсних предметів (перший, другий предмети) або матурального іспиту з двох основних предметів (польська мова, математика) та двох додаткових предметів (історія, іноземна мова, або біологія, або фізика та астрономія, або хімія за вибором вступника) для громадян Республіки Польща\n"
        "\n\n<b>Скорочений термін навчання - 2 роки 10 місяців:</b>\n"
        "<b>І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб.</b>\n"
        "1. Мотиваційний лист.\n"
        "2. НМТ 2024 року з чотирьох конкурсних предметів (перший, другий, третій, четвертий предмети) або НМТ 2023 року, або НМТ 2022 року з трьох конкурсних предметів (перший, другий, третій предмети) або ЗНО 2021 року з двох конкурсних предметів (перший, другий предмети) або матурального іспиту з двох основних предметів (польська мова, математика) та двох додаткових предметів (історія, іноземна мова, або біологія, або фізика та астрономія, або хімія за вибором вступника) для громадян Республіки Польща\n"
        )

    await callback_query.message.answer(
        text=text,
        parse_mode=ParseMode.HTML
    )
    await callback_query.answer()



@dp.message(F.text == Btn.ONES)
async def handle_info_command(message: types.Message):
    sp_num = "*174"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 17 Електроніка, автоматизація та електронні комунікації *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Автоматизація та комп'ютерно-інтегровані технології та робототехніка\n"
        "\n*Освітня програма*\n"
        "Комп'ютерні системи та програмна інженерія в автоматизації і робототехніці (ОНП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 10 місяців\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Комп'ютерні системи та програмна інженерія в автоматизації і робототехніці (ОНП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 10 місяців (ОНП)\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEF)
async def handle_info_command(message: types.Message):
    sp_num = "*141"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 14 Електрична інженерія *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Електроенергетика, електротехніка та електромеханіка\n"
        "\n*Освітня програма*\n"
        "Еконергетика та інтелектуальна електромеханіка (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Електроенергетика та інтелектуальна електромеханіка (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ZERO)
async def handle_info_command(message: types.Message):
    sp_num = "*051"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 05 Соціальні та поведінкові науки *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Економіка\n"
        "\n*Освітня програма*\n"
        "1. Економіка підприємства (ОНП).\n"
        "2. Фінансово-економічна безпека (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Економіка підприємства (ОПП).\n"
        "2. Фінансово-економічна безпека (ОПП)\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ZEROS)
async def handle_info_command(message: types.Message):
    sp_num = "*071"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 07 Управління та адміністрування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Облік і оподаткування\n"
        "\n*Освітня програма*\n"
        "1. Облік і аудит (ОПП).\n"
        "2. Діджитал-облік і контроль (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Облік і аудит (ОПП).\n"
        "2. Діджитал-облік і контроль (ОПП)\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == Btn.TWOF)
async def handle_info_command(message: types.Message):
    sp_num = "*241"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 24 Сфери обслуговування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Готельно-ресторанна справа\n"
        "\n*Освітня програма*\n"
        "Готельно-ресторанна справа (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Готельно-ресторанна справа (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEE)
async def handle_info_command(message: types.Message):
    sp_num = "*181"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 18 Виробництво та технології *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Харчові технології\n"
        "\n*Освітня програма*\n"
        "1. Технологічна експертиза та безпека харчової продукції (ОПП).\n"
        "2. Технології м'ясних і рибних продуктів (ОПП).\n"
        "3. Технології молока, жирів і продуктів для індустрії краси (ОПП).\n"
        "4. Контроль якості та безпечності у харчовій промисловості та в індустрії краси (ОПП).\n"
        "Інноваційні технології ресторанного бізнесу та здорового харчування (ОПП).\n"
        "1. Технології продуктів бродіння і виноробства (ОПП).\n"
        "1. Технології зберігання і переробки зерна (ОПП).\n"
        "2. Технології хліба, кондитерських, макаронних виробівта харчоконцентратів (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "2. Сенсорний аналіз в харчових технологіях (ОНП).\n"
        "*Термін*\n"
        "1 рік 10 місяців (ОНП)\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Технологічна експертиза та безпека харчової продукції (ОПП).\n"
        "2. Технології м'ясних і рибних продуктів (ОПП).\n"
        "3. Технології молока, жирів і продуктів для індустрії краси (ОПП).\n"
        "4. Контроль якості та безпечності у харчовій промисловості та в індустрії краси (ОПП).\n"
        "Інноваційні технології ресторанного бізнесу та здорового харчування (ОПП).\n"
        "1. Технології продуктів бродіння, напоїв і виноробства (ОПП).\n"
        "1. Технології зберігання і переробки зерна (ОПП).\n"
        "2. Технології хліба, кондитерських, макаронних виробівта харчоконцентратів (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == Btn.ONET)
async def handle_info_command(message: types.Message):
    sp_num = "*122"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 12 Інформаційні технології *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Комп'ютерні науки\n"
        "\n*Освітня програма*\n"
        "1. Інформаційні управляючі системи та технології (ОПП).\n"
        "2. Інформаційні технології проектування (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Інформаційні управляючі системи та технології (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONETW)
async def handle_info_command(message: types.Message):
    sp_num = "*123"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 12 Інформаційні технології *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Комп'ютерна інженерія\n"
        "\n*Освітня програма*\n"
        "1. Комп'ютерні системи та мережі (ОПП).\n"
        "2. Спеціалізовані комп'ютерні системи (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Комп'ютерні системи та мережі (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ZEROSEV)
async def handle_info_command(message: types.Message):
    sp_num = "*075"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 07 Управління та адміністрування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Маркетинг\n"
        "\n*Освітня програма*\n"
        "Маркетинг (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Маркетинг (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.SEVENTHREE)
async def handle_info_command(message: types.Message):
    sp_num = "*073"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 07 Управління та адміністрування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Менеджмент\n"
        "\n*Освітня програма*\n"
        "1. Менеджмент (ОПП).\n"
        "1. Логістика (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Менеджмент (ОПП).\n"
        "1. Логістика (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.TWOE)
async def handle_info_command(message: types.Message):
    sp_num = "*281"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 28 Публічне управління та адміністрування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Публічне управління та адміністрування\n"
        "\n*Освітня програма*\n"
        "Публічне управління та адміністрування (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Публічне управління та адміністрування (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEFO)
async def handle_info_command(message: types.Message):
    sp_num = "*142"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 14 Електрична інженерія *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Енергетичне машинобудування\n"
        "\n*Освітня програма*\n"
        "1. Холодильні машини, установки і кондиціювання повітря (ОПП).\n"
        "2. Кріогенні технології виробництва, зрідження і транспортування природних газів (ОПП).\n"
        "3. Холодильні машини і установки і кондиціювання повітря (ОНП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 10 місяців (ОНП)\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "1. Холодильні машини, установки і кондиціювання повітря (ОПП).\n"
        "2. Кріогенні технології виробництва, зрідження і транспортування природних газів (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONE)
async def handle_info_command(message: types.Message):
    sp_num = "*131"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 13 Механічна інженерія *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Прикладна механіка\n"
        "\n*Освітня програма*\n"
        "Машини і технології пакування (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Машини і технології пакування (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONETH)
async def handle_info_command(message: types.Message):
    sp_num = "*133"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 13 Механічна інженерія *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Галузеве машинобудування\n"
        "\n*Освітня програма*\n"
        "Системний інжиніринг промислових виробництв (ОНП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 10 місяців (ОНП)\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "ІТ-сервіс обладнання (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEZ)
async def handle_info_command(message: types.Message):
    sp_num = "*101"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 10 Природничі науки *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Екологія\n"
        "\n*Освітня програма*\n"
        "Екологічний контроль та аудит (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Екологічний контроль та аудит (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEEI)
async def handle_info_command(message: types.Message):
    sp_num = "*183"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 18 Виробництво та технології *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Технології захисту навколишнього середовища\n"
        "\n*Освітня програма*\n"
        "Технології захисту навколишнього середовища (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Технології захисту навколишнього середовища (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEEIG)
async def handle_info_command(message: types.Message):
    sp_num = "*185"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 18 Виробництво та технології *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Нафтогазова інженерія та технології\n"
        "\n*Освітня програма*\n"
        "Газонафтопроводи та газонафтосховища (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Газонафтопроводи та газонафтосховища (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ONEFOU)
async def handle_info_command(message: types.Message):
    sp_num = "*144"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 14 Електрична інженерія *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Теплоенергетика\n"
        "\n*Освітня програма*\n"
        "Теплоенергетика та енергоефективні технології (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Теплоенергетика та енергоефективні технології (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. Фаховий іспит\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )

@dp.message(F.text == Btn.TWOFOO)
async def handle_info_command(message: types.Message):
    sp_num = "*242"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*:\n\n"
        "Спеціальності галузі знань 24 Сфера обслуговування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Туризм і рекреація\n"
        "\n*Освітня програма*\n"
        "Міжнародний туризм (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*I. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Міднародний туризм (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )
@dp.message(F.text == Btn.ZE)
async def handle_info_command(message: types.Message):
    sp_num = "*076"
    sp_info = (
        f"Код: {sp_num}\n"
        "*Денна, Магістр*\n"
        "Спеціальності галузі знань 07 Управління та адміністрування *Вступ на основі СВО Бакалавр*\n"
        "Спеціальності усіх галузей знань. *Вступ на основі СВО Магістр (або ОКР Спеціаліст)*\n"
        "Інші (вступ на основі здобутого рівня вищої освіти в інших галузях знань), вступ на основі СВО Бакалавр*\n"
        "\n*Назва спеціальності*\n"
        "Підприємництво і торгівля\n"
        "\n*Освітня програма*\n"
        "Підприємництво і торгівля (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
        "\n\n*Заочна, Магістр*\n"
        "\n*Освітня програма*\n"
        "Підприємництво, торгівля, товарознавство та експертиза в митній справі (ОПП).\n"
        "\n*Вступні випробування*\n"
        "*І. Участь у конкурсному відборі при вступі на навчання за державним замовленням та/або за кошти фізичних та/або юридичних осіб:*\n"
        "1. Мотиваційний лист\n"
        "2. ЄВІ 2023 або 2024 років\n"
        "3. ЄФВВ 2024\n"
        "*Термін*\n"
        "1 рік 4 місяці\n"
       )
    await message.answer(
        text=sp_info,
        reply_markup=get_navigation(),
        reply_keyboard=ReplyKeyboardRemove(),
        parse_mode="Markdown"
    )


@router.callback_query(lambda c: c.data == "master_two")
async def show_btn(callback_query: types.CallbackQuery):
    await bot.send_message(
        callback_query.from_user.id,
        text="Оберіть номер спеціальності для отримання інформації:",
        reply_markup=get_mas_kb()
    )
    await callback_query.answer()

@router.callback_query(lambda c: c.data == "seemore")
async def seemore_handler(callback_query: types.CallbackQuery):
    await bot.send_message(
        callback_query.from_user.id,
        text="Виберіть номер спеціальності:",
        reply_markup=get_mas_kb()
    )
    await callback_query.answer()

def get_navigation_buttons():
    see_more_btn = InlineKeyboardButton(text="Подивитися ще", callback_data="see_more")
    return InlineKeyboardMarkup(inline_keyboard=[[see_more_btn]])

def get_navigation():
    see_more = InlineKeyboardButton(text="Подивитися ще", callback_data="seemore")
    return InlineKeyboardMarkup(inline_keyboard=[[see_more]])


@dp.message(Command("cost", prefix="!/"))
async def handle_cost_command(message: types.Message):
    cost_bac_btn = InlineKeyboardButton(
        text="Перейти",
        url="https://pk.ontu.edu.ua/_price.html",
    )
    rows = [
        [cost_bac_btn],
    ]
    markup =InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Вартість за навчання грн/семестр",
        reply_markup=markup,
    )

@dp.message(Command("submission", prefix="!/"))
async def handle_rules(message: types.Message):
    rul_bac_btn = InlineKeyboardButton(
        text="Бакалавру",
        url="https://pk.ontu.edu.ua/Page_344.html",
    )
    rul_mas_btn = InlineKeyboardButton(
        text="Випускнику колледжу",
        url="https://pk.ontu.edu.ua/Page_343.html",
    )
    rul_st_btn = InlineKeyboardButton(
        text="Випускнику школи",
        url="https://pk.ontu.edu.ua/Page_342.html",
    )
    rows = [
        [rul_bac_btn],
        [rul_mas_btn],
        [rul_st_btn],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    await message.answer(
        text="Правила прийому для здобуття вищої освіти",
        reply_markup=markup,
    )

@dp.message(Command("contact"))
async def handle_contact_command(message: types.Message):
    main_pk_btn = InlineKeyboardButton(
        text="Дізнайтеся більше",
        url="https://pk.ontu.edu.ua/index.html",
    )
    rows = [
        [main_pk_btn],]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    pk=(
        "<b>Контактна інформація:</b>\n"
        "📞 Телефон 1: +38 (048) 712-40-88\n"
        "📞 Телефон 2: +38 (048) 718-97-09\n"
        "📞 Телефон 3: +38 (048) 722-80-99\n"
        "🏢 Адреса: м. Одеса, вул. Канатна, 112\n"
        "Приймальна комісія, А-105\n"
        "\n<b>Графік роботи приймальної комісії\n"
        "\nПротягом навчального року</b>\n"
        "Понеділок:  9:00-17:15\n"
        "Вівторок:    9:00-17:15\n"
        "Середа:       9:00-17:15\n"
        "Четвер:       9:00-17:15\n"
        "П'ятниця:    9:00-17:15\n"
        "\n<b>Протягом вступної кампанії</b>\n"
        "Понеділок:  8:00-18:00\n"
        "Вівторок:    8:00-18:00\n"
        "Середа:       8:00-18:00\n"
        "Четвер:       8:00-18:00\n"
        "П'ятниця:    8:00-18:00\n"
        "Зв'яжіться з нами за цими контактами для додаткової інформації."
    )
    await message.answer(
        text=pk,
        reply_markup = markup,
        parse_mode=ParseMode.HTML
        )


valid_commands = ['start', 'grades', 'rules', 'submission', 'cost', 'contact']

# Обработчик сообщений
@dp.message()
async def echo_message(message: types.Message):
    # Проверка на команду
    if message.text and message.text.startswith('/'):
        command = message.text[1:].split(' ')[0]  # Получаем команду без "/"
        if command not in valid_commands:
            await message.reply("Такої команди немає. Виберіть одну з доступних команд.")
        else:
            await message.answer(f"Ви вибрали команду: {command}", parse_mode=ParseMode.MARKDOWN)
    else:
        # Проверка, если сообщение - стикер
        if message.sticker:
            await message.answer("Ви відправили стікер. Бот не обробляє стикери.")
        # Проверка, если сообщение - фото
        elif message.photo:
            await message.answer("Ви відправили фото. Бот не обробляє зображення.")
        # Проверка, если сообщение содержит текст
        elif message.text and message.text.strip():
            await message.answer(f"Ви відправили повідомлення: {message.text}")
        # Обработка пустого текста или других типов сообщений
        else:
            await message.reply("Бот поки що не обробляє цей тип повідомлень.")

async def main():

    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=BOT_TOKEN,
    )
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())


