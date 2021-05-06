from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN_BOT = '1676501133:AAE3PILf55H9AWs0YvFCcFmpYdQuFuPnM6w'
ADMIN_CHAT_ID = 404942071
TG_API_URL = 'https://telegg.ru/orig/bot'

gender_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='пол: Мужчина (Man)'), KeyboardButton(text='пол: Женщина (Woman)'))

lvl_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='уровень: 1'),
        KeyboardButton(text='уровень: 2'),
        KeyboardButton(text='уровень: 3'),
        KeyboardButton(text='уровень: 4'),
        KeyboardButton(text='уровень: 5'),
        KeyboardButton(text='уровень: 6'),
        KeyboardButton(text='уровень: 7'),
        KeyboardButton(text='уровень: 8'),
        KeyboardButton(text='уровень: 9'),
        KeyboardButton(text='уровень: 10'),
        KeyboardButton(text='уровень: 12'),
        KeyboardButton(text='уровень: 13'),
        KeyboardButton(text='уровень: 14'),
        KeyboardButton(text='уровень: 15'),
        KeyboardButton(text='уровень: 16'),
        KeyboardButton(text='уровень: 17'),
        KeyboardButton(text='уровень: 18'),
        KeyboardButton(text='уровень: 19'),
        KeyboardButton(text='уровень: 20'))

race_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='раса: Лесной гном (Forest gnome)')).\
    add(KeyboardButton(text='раса: Скальный гном (Rock gnome)')).\
    add(KeyboardButton(text='раса: Горный дварф (Mountain dwarf)')).\
    add(KeyboardButton(text='раса: Холмовой дварф (Hill dwarf)')).\
    add(KeyboardButton(text='раса: Драконорожденный (Dragonborn)')).\
    add(KeyboardButton(text='раса: Полуорк (Half-orc)')).\
    add(KeyboardButton(text='раса: Коренастый полурослик (Chunky halfling)')).\
    add(KeyboardButton(text='раса: Легконогий полурослик (Lightfoot halfling)')).\
    add(KeyboardButton(text='раса: Полуэльф (Half-elf)')).\
    add(KeyboardButton(text='раса: Тифлинг (Tiefling)')).\
    add(KeyboardButton(text='раса: Человек (Human)')).\
    add(KeyboardButton(text='раса: Эльф (Elf)')).\
    add(KeyboardButton(text='раса: Высший эльф (High elf)')).\
    add(KeyboardButton(text='раса: Лесной эльф (Forest elf)')).\
    add(KeyboardButton(text='раса: Темный эльф (Dark elf)'))

class_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='класс: Бард (Bard)')).\
    add(KeyboardButton(text='класс: Варвар (Barbarian)')).\
    add(KeyboardButton(text='класс: Воин (Fighter)')).\
    add(KeyboardButton(text='класс: Волшебник (Wizard)')).\
    add(KeyboardButton(text='класс: Друид (Druid)')).\
    add(KeyboardButton(text='класс: Жрец (Cleric)')).\
    add(KeyboardButton(text='класс: Колдун (Warlock)')).\
    add(KeyboardButton(text='класс: Монах (Monk)')).\
    add(KeyboardButton(text='класс: Паладин (Paladin)')).\
    add(KeyboardButton(text='класс: Плут (Rogue)')).\
    add(KeyboardButton(text='класс: Следопыт (Ranger)')).\
    add(KeyboardButton(text='класс: Чародей (Sorcerer)'))

background_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='история: ПРИСЛУЖНИК (Servant)')).\
    add(KeyboardButton(text='история: ШАРЛАТАН (Charlatan)')).\
    add(KeyboardButton(text='история: ПРЕСТУПНИК (Criminal)')).\
    add(KeyboardButton(text='история: АРТИСТ (Artist)')).\
    add(KeyboardButton(text='история: НАРОДНЫЙ ГЕРОЙ (Folk hero)')).\
    add(KeyboardButton(text='история: ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК (Guild craftsmen)')).\
    add(KeyboardButton(text='история: ОТШЕЛЬНИК (Hermit)')).\
    add(KeyboardButton(text='история: БЛАГОРОДНЫЙ (Noble)')).\
    add(KeyboardButton(text='история: ЧУЖЕЗЕМЕЦ (Aliens)')).\
    add(KeyboardButton(text='история: МУДРЕЦ (Sage)')).\
    add(KeyboardButton(text='история: МОРЯК (Sailor)')).\
    add(KeyboardButton(text='история: СОЛДАТ (Soldier)')).\
    add(KeyboardButton(text='история: БЕСПРИЗОРНИК (Throwaway)'))

dice_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='dice:   D4'),
        KeyboardButton(text='dice:   D6'),
        KeyboardButton(text='dice:   D8'),
        KeyboardButton(text='dice:  D10'),
        KeyboardButton(text='dice:  D12'),
        KeyboardButton(text='dice:  D20'),
        KeyboardButton(text='dice: D100')).\
    add(KeyboardButton(text='/help')).\
    add(KeyboardButton(text='/new'))

perform_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).\
    add(KeyboardButton(text='показать лист персонажа'))
