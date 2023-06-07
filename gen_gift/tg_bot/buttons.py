from tg_bot.Globals import TEXTS
from tg_bot.models import *
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def btns(type=None, ctg=None, age=None, situation=None, interests=None, cash=None, human=None, lang=1):
    btn = []
    if type == "menu":
        btn = [
            [KeyboardButton(TEXTS['SOVGA'][lang]), KeyboardButton(TEXTS["Settings"][lang])],
        ]
    elif type == "contact":
        btn = [
            [KeyboardButton(TEXTS['CON'][lang], request_contact=True)]
        ]
    elif type == "ctg":
        btn = []
        ctgs = Category.objects.all()
        for i in range(1, len(ctgs), 2):
            btn1 = ctgs[i - 1].name_uz if lang == 1 else ctgs[i - 1].name_ru
            btn2 = ctgs[i].name_uz if lang == 1 else ctgs[i].name_ru

            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(ctgs) % 2:
            btn1 = ctgs[len(ctgs) - 1].name_uz if lang == 1 else ctgs[len(ctgs) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "human":
        btn = []

        human = Human.objects.filter(ctg=ctg)
        if not human:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(human), 2):
            btn1 = human[i - 1].name_uz if lang == 1 else human[i - 1].name_ru
            btn2 = human[i].name_uz if lang == 1 else human[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(human) % 2:
            btn1 = human[len(human) - 1].name_uz if lang == 1 else human[len(human) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "situation":
        btn = []
        situate = Situation.objects.filter(human=human)
        if not situate:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(situate), 2):
            btn1 = situate[i - 1].name_uz if lang == 1 else situate[i - 1].name_ru
            btn2 = situate[i].name_uz if lang == 1 else situate[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(situate) % 2:
            btn1 = situate[len(situate) - 1].name_uz if lang == 1 else situate[len(situate) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "interests":
        btn = []
        interests = Interests.objects.filter(situation=situation)
        print("interests", interests)
        if not interests:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(interests), 2):
            btn1 = interests[i - 1].name_uz if lang == 1 else interests[i - 1].name_ru
            btn2 = interests[i].name_uz if lang == 1 else interests[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(interests) % 2:
            btn1 = interests[len(interests) - 1].name_uz if lang == 1 else interests[len(interests) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "cash":
        btn = []
        cash = Cash.objects.filter(interests=interests)
        if not cash:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(cash), 2):
            btn1 = cash[i - 1].name_uz if lang == 1 else cash[i - 1].name_ru
            btn2 = cash[i].name_uz if lang == 1 else cash[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(cash) % 2:
            btn1 = cash[len(cash) - 1].name_uz if lang == 1 else cash[len(cash) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "age":
        btn = []
        age = Agee.objects.filter(cash=cash)
        if not age:
            return ReplyKeyboardMarkup([], resize_keyboard=True)
        for i in range(1, len(age), 2):
            btn1 = age[i - 1].name_uz if lang == 1 else age[i - 1].name_ru
            btn2 = age[i].name_uz if lang == 1 else age[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(age) % 2:
            btn1 = age[len(age) - 1].name_uz if lang == 1 else age[len(age) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])

    elif type == "product":
        btn = []
        lan = 'uz' if lang == 1 else 'ru'
        filter = {
            f'name_{lan}': age
        }
        age = Agee.objects.filter(**filter).first()

        products = Product.objects.filter(age=age)

        for i in range(1, len(products), 2):
            btn1 = products[i - 1].name_uz if lang == 1 else products[i - 1].name_ru
            btn2 = products[i].name_uz if lang == 1 else products[i].name_ru
            btn.append([
                KeyboardButton(btn1), KeyboardButton(btn2)
            ])
        if len(products) % 2:
            btn1 = products[len(products) - 1].name_uz if lang == 1 else products[len(products) - 1].name_ru
            btn.append([KeyboardButton(btn1)])
        btn.append([KeyboardButton(TEXTS['Back'][lang]),
                    KeyboardButton(TEXTS['BackTOP'][lang])])
    elif type == "lang":
        btn = [
            [KeyboardButton("🇺🇿Uz"), KeyboardButton("🇷🇺Ru")],
            [KeyboardButton(TEXTS['Back'][lang])]
        ]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline_btn(type, page=1, ctg_id=0, data=None, nta=1, user_id=0):
    btn = []
    if type == "savat":
        btn.append([
            InlineKeyboardButton("◀️Orqaga", callback_data="◀️Orqaga"),
            InlineKeyboardButton("🚕 Buyurtma berish", callback_data="🚕 Buyurtma berish")
        ])
        btn.append([
            InlineKeyboardButton("⏰ Yetkazib berish vaqti", callback_data="⏰ Yetkazib berish vaqti"),
        ])
        savat = Savat.objects.filter(user_id=user_id)
        if not savat:
            return InlineKeyboardMarkup([])
        for i in range(len(savat)):
            btn.append([
                InlineKeyboardButton(f"❌{savat[i].product}", callback_data=f"{savat[i].slug}")
            ])
        btn.append([

            InlineKeyboardButton("🧹 Savatni tozalash", callback_data="🧹 Savatni tozalash")
        ])
    if type == "prod":
        # btn.append([
        #     InlineKeyboardButton("-", callback_data="-"),
        #     InlineKeyboardButton(f"{nta}", callback_data=f"{nta}"),
        #     InlineKeyboardButton("+", callback_data="+"),
        # ])
        btn.append([
            InlineKeyboardButton("📥 Savatga qo'shish", callback_data="savat"),
        ])

    return InlineKeyboardMarkup(btn)
