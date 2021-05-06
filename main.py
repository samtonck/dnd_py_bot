#!/usr/bin/python3

from random import randint

import requests
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

import game_background
import game_class
import game_race
import player
from config import TOKEN_BOT, ADMIN_CHAT_ID, gender_kb, lvl_kb, race_kb, class_kb, background_kb, dice_kb, perform_kb

bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


def mod_saving(saving_throws_strength, saving_throws_dexterity, saving_throws_constitution, saving_throws_intelligence,
               saving_throws_wisdom, saving_throws_charisma):
    player.saving_throws_strength = (player.strength - 10) // 2  # модификатор сила
    player.saving_throws_dexterity = (player.dexterity - 10) // 2  # модификатор ловкость
    player.saving_throws_constitution = (player.constitution - 10) // 2  # модификатор телосложение
    player.saving_throws_intelligence = (player.intelligence - 10) // 2  # модификатор интеллект
    player.saving_throws_wisdom = (player.wisdom - 10) // 2  # модификатор мудрость
    player.saving_throws_charisma = (player.charisma - 10) // 2  # модификатор харизма
    return (saving_throws_strength, saving_throws_dexterity, saving_throws_constitution, saving_throws_intelligence,
            saving_throws_wisdom, saving_throws_charisma)


def mod_stat(mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma):
    player.mod_strength = (player.strength - 10) // 2  # модификатор сила
    player.mod_dexterity = (player.dexterity - 10) // 2  # модификатор ловкость
    player.mod_constitution = (player.constitution - 10) // 2  # модификатор телосложение
    player.mod_intelligence = (player.intelligence - 10) // 2  # модификатор интеллект
    player.mod_wisdom = (player.wisdom - 10) // 2  # модификатор мудрость
    player.mod_charisma = (player.charisma - 10) // 2  # модификатор харизма
    return mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma


def mod_skill(acrobatics, perception, athletics, investigation, survival, performance, intimidation, history,
              sleight_of_hand, arcana, medicine, deception, nature, insight, religion, stealth, persuasion,
              animal_handling):
    player.acrobatics = (player.dexterity - 10) // 2  # акробатика
    player.perception = (player.intelligence - 10) // 2  # анализ
    player.athletics = (player.strength - 10) // 2  # атлетика
    player.investigation = (player.wisdom - 10) // 2  # внимательность
    player.survival = (player.wisdom - 10) // 2  # выживание
    player.performance = (player.charisma - 10) // 2  # выступление
    player.intimidation = (player.charisma - 10) // 2  # запугивание
    player.history = (player.intelligence - 10) // 2  # история
    player.sleight_of_hand = (player.dexterity - 10) // 2  # ловкость рук
    player.arcana = (player.intelligence - 10) // 2  # магия
    player.medicine = (player.wisdom - 10) // 2  # медицина
    player.deception = (player.charisma - 10) // 2  # обман
    player.nature = (player.intelligence - 10) // 2  # природа
    player.insight = (player.wisdom - 10) // 2  # проницательность
    player.religion = (player.intelligence - 10) // 2  # религия
    player.stealth = (player.dexterity - 10) // 2  # скрытность
    player.persuasion = (player.charisma - 10) // 2  # убеждение
    player.animal_handling = (player.wisdom - 10) // 2  # уход за животными
    return (acrobatics, perception, athletics, investigation, survival, performance, intimidation, history,
            sleight_of_hand, arcana, medicine, deception, nature, insight, religion, stealth, persuasion,
            animal_handling)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAECKGhgcaqXViLpRpVmQk1TUDeFpDHrvwAC1wIAAi8P8AY56kIpiVP1fh4E')
    await message.answer('Бот запущен!')


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAECKBdgcK4TUyM-udPnuXr6t_g4VyjaaAACEAADVh9JFSZILAM9dNiRHgQ')
    await message.answer('Кнопка /start запускает и проверяет запущен ли бот\n'
                         'Кнопка /help выводит подсказки по боту\n'
                         'Кнопка /new запускает создание нового персонажа\n'
                         'Кнопка /dice кидает кубик d20\n'
                         '\n'
                         'Если что-то не работает или есть ошибки пишем @SamTonck')


@dp.message_handler(commands=['dice'])
async def process_start_command(message: types.Message):
    await message.answer('Какую кость ты хочешь кинуть?', reply_markup=dice_kb)


@dp.message_handler(commands=['new'])
async def process_start_command(message: types.Message):
    await message.answer_sticker(r'CAACAgIAAxkBAAECKGVgcamHv_9M5oeWoldOKGrUnneb-wACpwADKK4eF2KKILdTVHJJHgQ')
    await message.answer(f'давай выберем пол будущего персонажа', reply_markup=gender_kb)
    player.name_player = str(f'{message.from_user.first_name} {message.from_user.last_name}')


@dp.message_handler(lambda message: message.text[:3] == 'пол')
async def action_cancel(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=lvl_kb)
    player.game_gender = str(f'{message.text}')
    await message.answer('За персонажа какого уровня вы будете играть?')


@dp.message_handler(lambda message: message.text[:7] == 'уровень')
async def action_cancel(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=race_kb)
    player.level = int(message.text[9:])

    if player.level == 1:
        player.experience_point = 0
        player.proficiency_bonus = 2
    elif player.level == 2:
        player.experience_point = 300
        player.proficiency_bonus = 2
    elif player.level == 3:
        player.experience_point = 900
        player.proficiency_bonus = 2
    elif player.level == 4:
        player.experience_point = 2700
        player.proficiency_bonus = 2
    elif player.level == 5:
        player.experience_point = 6500
        player.proficiency_bonus = 3
    elif player.level == 6:
        player.experience_point = 14000
        player.proficiency_bonus = 3
    elif player.level == 7:
        player.experience_point = 23000
        player.proficiency_bonus = 3
    elif player.level == 8:
        player.experience_point = 34000
        player.proficiency_bonus = 3
    elif player.level == 9:
        player.experience_point = 48000
        player.proficiency_bonus = 4
    elif player.level == 10:
        player.experience_point = 64000
        player.proficiency_bonus = 4
    elif player.level == 11:
        player.experience_point = 85000
        player.proficiency_bonus = 4
    elif player.level == 12:
        player.experience_point = 100000
        player.proficiency_bonus = 4
    elif player.level == 13:
        player.experience_point = 120000
        player.proficiency_bonus = 5
    elif player.level == 14:
        player.experience_point = 140000
        player.proficiency_bonus = 5
    elif player.level == 15:
        player.experience_point = 165000
        player.proficiency_bonus = 5
    elif player.level == 16:
        player.experience_point = 195000
        player.proficiency_bonus = 5
    elif player.level == 17:
        player.experience_point = 225000
        player.proficiency_bonus = 6
    elif player.level == 18:
        player.experience_point = 265000
        player.proficiency_bonus = 6
    elif player.level == 19:
        player.experience_point = 305000
        player.proficiency_bonus = 6
    elif player.level == 20:
        player.experience_point = 355000
        player.proficiency_bonus = 6
    await message.answer('За персонажа какой рассы вы будете играть?')


@dp.message_handler(lambda message: message.text[:4] == 'раса')
async def action_cancel(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=class_kb)
    player.race = str(f'{message.text}')
    if message.text == 'раса: Лесной гном (Forest gnome)':  # Лесной гном
        game_race.forest_gnome()
    elif message.text == 'раса: Скальный гном (Rock gnome)':  # Скальный гном
        game_race.rock_gnome()
    elif message.text == 'раса: Горный дварф (Mountain dwarf)':  # Горный дворф
        game_race.mountain_dwarf()
    elif message.text == 'раса: Холмовой дварф (Hill dwarf)':  # Холмовой дворф
        game_race.hill_dwarf()
    elif message.text == 'раса: Драконорожденный (Dragonborn)':  # Драконорожденнй
        game_race.dragonborn()
    elif message.text == 'раса: Полуорк (Half-orc)':  # Полуорк
        game_race.half_orc()
    elif message.text == 'раса: Коренастый полурослик (Chunky halfling)':  # Коренастый полурослик
        game_race.chunky_halfling()
    elif message.text == 'раса: Легконогий полурослик (Lightfoot halfling)':  # Легконогий полурослик
        game_race.lightfoot_halfling()
    elif message.text == 'раса: Полуэльф (Half-elf)':  # Полуэльф
        game_race.half_elf()
    elif message.text == 'раса: Тифлинг (Tiefling)':  # Тифлинг
        game_race.tiefling()
    elif message.text == 'раса: Человек (Human)':  # Человек
        game_race.human()
    elif message.text == 'раса: Эльф (Elf)':  # Эльф
        game_race.elf()
    elif message.text == 'раса: Высший эльф (High elf)':  # Высший эльф
        game_race.high_elf()
    elif message.text == 'раса: Лесной эльф (Forest elf)':  # Лесной эльф
        game_race.forest_elf()
    elif message.text == 'раса: Темный эльф (Dark elf)':  # Темный эльф
        game_race.dark_elf()
    await message.answer('За персонажа какой класс вы будете играть?')


@dp.message_handler(lambda message: message.text[:5] == 'класс')
async def action_cancel(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=background_kb)
    player.game_class = str(f'{message.text}')

    if message.text == 'класс: Бард (Bard)':  # Бард
        game_class.bard()
        await message.answer('Рекомендуемая предыстория АРТИСТ')
    elif message.text == 'класс: Варвар (Barbarian)':  # Варвар
        game_class.barbarian()
        await message.answer('Рекомендуемая предыстория Чужеземец')
    elif message.text == 'класс: Воин (Fighter)':  # Воин
        game_class.fighter()
        await message.answer('Рекомендуемая предыстория Солдат')
    elif message.text == 'класс: Волшебник (Wizard)':  # Волшебник
        game_class.wizard()
        await message.answer('Рекомендуемая предыстория МУДРЕЦ')
    elif message.text == 'класс: Друид (Druid)':  # Друид
        game_class.druid()
        await message.answer('Рекомендуемая предыстория ОТШЕЛЬНИК')
    elif message.text == 'класс: Жрец (Cleric)':  # Жрец
        game_class.cleric()
        await message.answer('Рекомендуемая предыстория ПРИСЛУЖНИК')
    elif message.text == 'класс: Колдун (Warlock)':  # Колдун
        game_class.warlock()
        await message.answer('Рекомендуемая предыстория ШАРЛАТАН')
    elif message.text == 'класс: Монах (Monk)':  # Монах
        game_class.monk()
        await message.answer('Рекомендуемая предыстория ОТШЕЛЬНИК')
    elif message.text == 'класс: Паладин (Paladin)':  # Паладин
        game_class.paladin()
        await message.answer('Рекомендуемая предыстория БЛАГОРОДНЫЙ')
    elif message.text == 'класс: Плут (Rogue)':  # Плут
        game_class.rogue()
        await message.answer('Рекомендуемая предыстория ШАРЛАТАН')
    elif message.text == 'класс: Следопыт (Ranger)':  # Следопыт
        game_class.ranger()
        await message.answer('Рекомендуемая предыстория ЧУЖЕЗЕМЕЦ')
    elif message.text == 'класс: Чародей (Sorcerer)':  # Чародей
        game_class.sorcerer()
        await message.answer('Рекомендуемая предыстория ОТШЕЛЬНИК')
    await message.answer('Выберите предысторию')


@dp.message_handler(lambda message: message.text[:7] == 'история')
async def action_cancel(message: Message):
    await message.answer(f"Вы выбрали {message.text}", reply_markup=perform_kb)
    player.background = str(f'{message.text}')

    if message.text == 'история: ПРИСЛУЖНИК (Servant)':  # ПРИСЛУЖНИК
        game_background.servant()
        # game_background.servant_background()
    elif message.text == 'история: ШАРЛАТАН (Charlatan)':  # ШАРЛАТАН
        game_background.charlatan()
        # game_background.charlatan_background()
    elif message.text == 'история: ПРЕСТУПНИК (Criminal)':  # ПРЕСТУПНИК
        game_background.criminal()
        # game_background.criminal_background()
    elif message.text == 'история: АРТИСТ (Artist)':  # АРТИСТ
        game_background.artist()
        # game_background.artist_background()
    elif message.text == 'история: НАРОДНЫЙ ГЕРОЙ (Folk hero)':  # НАРОДНЫЙ ГЕРОЙ
        game_background.folk_hero()
        # game_background.folk_hero_background()
    elif message.text == 'история: ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК (Guild craftsmen)':  # ГИЛЬДЕЙСКИЙ РЕМЕСЛЕННИК
        game_background.guild_craftsmen()
        # game_background.guild_craftsmen_background()
    elif message.text == 'история: ОТШЕЛЬНИК (Hermit)':  # ОТШЕЛЬНИК
        game_background.hermit()
        # game_background.hermit_background()
    elif message.text == 'история: БЛАГОРОДНЫЙ (Noble)':  # БЛАГОРОДНЫЙ
        game_background.noble()
        # game_background.noble_background()
    elif message.text == 'история: ЧУЖЕЗЕМЕЦ (Aliens)':  # ЧУЖЕЗЕМЕЦ
        game_background.aliens()
        # game_background.aliens_background()
    elif message.text == 'история: МУДРЕЦ (Sage)':  # МУДРЕЦ
        game_background.sage()
        # game_background.sage_background()
    elif message.text == 'история: МОРЯК (Sailor)':  # МОРЯК
        game_background.sailor()
        # game_background.sailor_background()
    elif message.text == 'история: СОЛДАТ (Soldier)':  # СОЛДАТ
        game_background.soldier()
        # game_background.soldier_background()
    elif message.text == 'история: БЕСПРИЗОРНИК (Throwaway)':  # БЕСПРИЗОРНИК
        game_background.throwaway()
        # game_background.throwaway_background()

    await message.answer_sticker(r'CAACAgIAAxkBAAECKA5gcJNH2NteoVF3gNLLFaI1yipw4QACNgAD2-w5FNyAoNnqHintHgQ')
    await message.answer('Вы создали персонажа =)')


#                  ==//== Вывод информации о персонаже ==//==
@dp.message_handler(lambda message: message.text == 'показать лист персонажа')
async def action_cancel(message: Message):
    await message.answer(f'Имя грока = {player.name_player}\n'
                         f'имя персонажа = {player.name}\n'
                         f'пол персонажа = {player.game_gender}\n'
                         f'возраст персонажа = {player.age}\n'
                         f'рост персонажа = {player.height}\n'
                         f'вес персонажа = {player.weight}')
    await message.answer_sticker(r'CAACAgIAAxkBAAECKBVgcK24VXruRnGCWotMGOKcEj-XSwACBAADVh9JFbnThjb5WO_1HgQ')
    await message.answer(f'{player.race}\n'
                         f'{player.game_class}\n'
                         f'{player.background}\n'
                         f'мировоззрение ={player.alignment}')
    await message.answer(f'призвание/гильдия/судьбоносное происшествие = {player.like_mechanics}\n'
                         f'черты характера = {player.personality_traits}\n'
                         f'идеалы = {player.ideals}\n'
                         f'привязанности = {player.bonds}\n'
                         f'слабости = {player.flaws}')
    await message.answer(f'уровень = {player.level}\n'
                         f'опыт = {player.experience_point}\n'
                         f'бонус мастерства = {player.proficiency_bonus}')
    await message.answer(f'сила = {player.strength}\n'
                         f'ловкость = {player.dexterity}\n'
                         f'телосложение = {player.constitution}\n'
                         f'интеллект = {player.intelligence}\n'
                         f'мудрость = {player.wisdom}\n'
                         f'харизма = {player.charisma}')

    mod_saving(player.mod_strength, player.mod_dexterity, player.mod_constitution,
               player.mod_intelligence, player.mod_wisdom, player.mod_charisma)

    mod_stat(player.saving_throws_strength, player.saving_throws_dexterity, player.saving_throws_constitution,
             player.saving_throws_intelligence, player.saving_throws_wisdom, player.saving_throws_charisma)

    mod_skill(player.acrobatics, player.perception, player.athletics, player.investigation, player.survival,
              player.performance, player.intimidation, player.history, player.sleight_of_hand, player.arcana,
              player.medicine, player.deception, player.nature, player.insight, player.religion, player.stealth,
              player.persuasion, player.animal_handling)

    await message.answer(f'модификатор сила = {player.mod_strength}\n'
                         f'модификатор ловкость = {player.mod_dexterity}\n'
                         f'модификатор телосложение = {player.mod_constitution}\n'
                         f'модификатор интеллект = {player.mod_intelligence}\n'
                         f'модификатор мудрость = {player.mod_wisdom}\n'
                         f'модификатор харизма = {player.mod_charisma}')

    if player.check_saving_throws_strength is True:
        player.saving_throws_strength += player.proficiency_bonus
        await message.answer(f'знание спас броска сила = {player.check_saving_throws_strength}')
    if player.check_saving_throws_dexterity is True:
        player.saving_throws_dexterity += player.proficiency_bonus
        await message.answer(f'знание спас броска ловкость = {player.check_saving_throws_dexterity}')
    if player.check_saving_throws_constitution is True:
        player.saving_throws_constitution += player.proficiency_bonus
        await message.answer(f'знание спас броска телосложение = {player.check_saving_throws_constitution}')
    if player.check_saving_throws_intelligence is True:
        player.saving_throws_intelligence += player.proficiency_bonus
        await message.answer(f'знание спас броска интеллект = {player.check_saving_throws_intelligence}')
    if player.check_saving_throws_wisdom is True:
        player.saving_throws_wisdom += player.proficiency_bonus
        await message.answer(f'знание спас броска мудрость = {player.check_saving_throws_wisdom}')
    if player.check_saving_throws_charisma is True:
        player.saving_throws_charisma += player.proficiency_bonus
        await message.answer(f'знание спас броска харизма = {player.check_saving_throws_charisma}')

    await message.answer(f'спас бросок сила = {player.saving_throws_strength}\n'
                         f'спас бросок ловкость = {player.saving_throws_dexterity}\n'
                         f'спас бросок телосложение = {player.saving_throws_constitution}\n'
                         f'спас бросок интеллект = {player.saving_throws_intelligence}\n'
                         f'спас бросок мудрость = {player.saving_throws_wisdom}\n'
                         f'спас бросок харизма = {player.saving_throws_charisma}')

    if player.check_acrobatics is True:
        player.acrobatics += player.proficiency_bonus
        await message.answer(f'знание акробатика = {player.check_acrobatics}')
    if player.check_perception is True:
        player.perception += player.proficiency_bonus
        await message.answer(f'знание анализ = {player.check_perception}')
    if player.check_athletics is True:
        player.athletics += player.proficiency_bonus
        await message.answer(f'знание атлетика = {player.check_athletics}')
    if player.check_investigation is True:
        player.investigation += player.proficiency_bonus
        await message.answer(f'знание внимательность = {player.check_investigation}')
    if player.check_survival is True:
        player.survival += player.proficiency_bonus
        await message.answer(f'знание выживание = {player.check_survival}')
    if player.check_performance is True:
        player.performance += player.proficiency_bonus
        await message.answer(f'знание выступление = {player.check_performance}')
    if player.check_intimidation is True:
        player.intimidation += player.proficiency_bonus
        await message.answer(f'знание запугивание = {player.check_intimidation}')
    if player.check_history is True:
        player.history += player.proficiency_bonus
        await message.answer(f'знание история = {player.check_history}')
    if player.check_sleight_of_hand is True:
        player.sleight_of_hand += player.proficiency_bonus
        await message.answer(f'знание ловкость рук = {player.check_sleight_of_hand}')
    if player.check_arcana is True:
        player.arcana += player.proficiency_bonus
        await message.answer(f'знание магия = {player.check_arcana}')
    if player.check_medicine is True:
        player.medicine += player.proficiency_bonus
        await message.answer(f'знание медицина = {player.check_medicine}')
    if player.check_deception is True:
        player.deception += player.proficiency_bonus
        await message.answer(f'знание обман = {player.check_deception}')
    if player.check_nature is True:
        player.nature += player.proficiency_bonus
        await message.answer(f'знание природа = {player.check_nature}')
    if player.check_insight is True:
        player.insight += player.proficiency_bonus
        await message.answer(f'знание проницательность = {player.check_insight}')
    if player.check_religion is True:
        player.religion += player.proficiency_bonus
        await message.answer(f'знание религия = {player.check_religion}')
    if player.check_stealth is True:
        player.stealth += player.proficiency_bonus
        await message.answer(f'знание скрытность = {player.check_stealth}')
    if player.check_persuasion is True:
        player.persuasion += player.proficiency_bonus
        await message.answer(f'знание убеждение = {player.check_persuasion}')
    if player.check_animal_handling is True:
        player.animal_handling += player.proficiency_bonus
        await message.answer(f'знание уход за животными = {player.check_animal_handling}')

    await message.answer(f'акробатика = {player.acrobatics}\n'
                         f'анализ = {player.perception}\n'
                         f'атлетика = {player.athletics}\n'
                         f'внимательность = {player.investigation}\n'
                         f'выживание = {player.survival}\n'
                         f'выступление = {player.performance}\n'
                         f'запугивание = {player.intimidation}\n'
                         f'история = {player.history}\n'
                         f'ловкость рук = {player.sleight_of_hand}\n'
                         f'магия = {player.arcana}\n'
                         f'медицина = {player.medicine}\n'
                         f'обман = {player.deception}\n'
                         f'природа = {player.nature}\n'
                         f'проницательность = {player.insight}\n'
                         f'религия = {player.religion}\n'
                         f'скрытность = {player.stealth}\n'
                         f'убеждение = {player.persuasion}\n'
                         f'уход за животными = {player.animal_handling}')
    player.passive_wisdom = 10 + player.mod_wisdom
    await message.answer(f'пассивная мудрость (внимательность) = {player.passive_wisdom}')
    player.armor_class = 10 + player.mod_dexterity
    await message.answer(f'КД (класс доспеха) = {player.armor_class}')
    player.initiative = player.mod_dexterity
    await message.answer(f'инициатива = {player.initiative}')
    await message.answer(f'скорость = {player.speed}\n'
                         f'максимальное кол-во очков жизни = {player.hit_point_maximum}\n'
                         f'кубик жизни = {player.hit_dise}')

    await message.answer(f'темное зрение = {player.dark_vision}')
    await message.answer(f'языки = {player.language}')
    await message.answer(f'другие умения = {player.other}')
    await message.answer(f'снаряжение = {player.equipment}')

    if len(player.skills) > 8000:
        await message.answer(f'навыки = {player.skills[:4000]} =>')
        await message.answer(f' =>{player.skills[4000:8000]} =>')
        await message.answer(f' =>{player.skills[8000:]}')
    elif len(player.skills) > 4000:
        await message.answer(f'навыки = {player.skills[:4000]} =>')
        await message.answer(f' =>{player.skills[4000:]} =>')
    else:
        await message.answer(f'навыки = {player.skills}')

    await message.answer_sticker(r'CAACAgIAAxkBAAECKAxgcJLAGoEn_1FSiYsgrDgQ-NfnxgACFgAD2-w5FOz7E9BOxgJaHgQ')

    player.name_player = ''

    player.name = ''  # имя персонажа
    player.game_gender = ''  # пол персонажа
    player.age = ''  # возраст персонажа
    player.height = ''  # рост персонажа
    player.weight = ''  # вес персонажа

    player.race = ''  # раса
    player.game_class = ''  # класс
    player.background = ''  # предыстория
    player.alignment = ''  # мировоззрение

    player.like_mechanics = ''  # призвание/гильдия/судьбоносное происшествие
    player.personality_traits = ''  # черты характера
    player.ideals = ''  # идеалы
    player.bonds = ''  # привязанности
    player.flaws = ''  # слабости

    player.level = 0  # уровень
    player.experience_point = 0  # опыт
    player.proficiency_bonus = 0  # бонус мастерства

    player.strength = 0  # сила
    player.dexterity = 0  # ловкость
    player.constitution = 0  # телосложение
    player.intelligence = 0  # интеллект
    player.wisdom = 0  # мудрость
    player.charisma = 0  # харизма

    player.mod_strength = 0  # модификатор сила
    player.mod_dexterity = 0  # модификатор ловкость
    player.mod_constitution = 0  # модификатор телосложение
    player.mod_intelligence = 0  # модификатор интеллект
    player.mod_wisdom = 0  # модификатор мудрость
    player.mod_charisma = 0  # модификатор харизма

    player.check_saving_throws_strength = False  # знание спас бросок сила
    player.check_saving_throws_dexterity = False  # знание  спас бросок ловкость
    player.check_saving_throws_constitution = False  # знание  спас бросок телосложение
    player.check_saving_throws_intelligence = False  # знание  спас бросок интеллект
    player.check_saving_throws_wisdom = False  # знание  спас бросок мудрость
    player.check_saving_throws_charisma = False  # знание  спас бросок харизма

    player.saving_throws_strength = player.mod_strength  # спас бросок сила
    player.saving_throws_dexterity = player.mod_dexterity  # спас бросок ловкость
    player.saving_throws_constitution = player.mod_constitution  # спас бросок телосложение
    player.saving_throws_intelligence = player.mod_intelligence  # спас бросок интеллект
    player.saving_throws_wisdom = player.mod_wisdom  # спас бросок мудрость
    player.saving_throws_charisma = player.mod_charisma  # спас бросок харизма

    player.check_acrobatics = False  # знание акробатика
    player.check_perception = False  # знание анализ
    player.check_athletics = False  # знание атлетика
    player.check_investigation = False  # знание внимательность
    player.check_survival = False  # знание выживание
    player.check_performance = False  # знание выступление
    player.check_intimidation = False  # знание запугивание
    player.check_history = False  # знание история
    player.check_sleight_of_hand = False  # знание ловкость рук
    player.check_arcana = False  # знание магия
    player.check_medicine = False  # знание медицина
    player.check_deception = False  # знание обман
    player.check_nature = False  # знание природа
    player.check_insight = False  # знание проницательность
    player.check_religion = False  # знание религия
    player.check_stealth = False  # знание скрытность
    player.check_persuasion = False  # знание убеждение
    player.check_animal_handling = False  # знание уход за животными

    player.acrobatics = player.mod_dexterity  # акробатика
    player.perception = player.mod_intelligence  # анализ
    player.athletics = player.mod_strength  # атлетика
    player.investigation = player.mod_wisdom  # внимательность
    player.survival = player.mod_wisdom  # выживание
    player.performance = player.mod_charisma  # выступление
    player.intimidation = player.mod_charisma  # запугивание
    player.history = player.mod_intelligence  # история
    player.sleight_of_hand = player.mod_dexterity  # ловкость рук
    player.arcana = player.mod_intelligence  # магия
    player.medicine = player.mod_wisdom  # медицина
    player.deception = player.mod_charisma  # обман
    player.nature = player.mod_intelligence  # природа
    player.insight = player.mod_wisdom  # проницательность
    player.religion = player.mod_intelligence  # религия
    player.stealth = player.mod_dexterity  # скрытность
    player.persuasion = player.mod_charisma  # убеждение
    player.animal_handling = player.mod_wisdom  # уход за животными

    player.passive_wisdom = 10 + player.mod_wisdom  # пассивная мудрость (внимательность)

    player.armor_class = 0  # КД (класс доспеха)
    player.initiative = player.dexterity  # инициатива
    player.speed = 0  # скорость

    player.hit_point_maximum = 0  # максимальное кол-во очков жизни
    player.hit_dise = ''  # кубик жизни

    player.dark_vision = ''  # темное зрение
    player.language = ''  # языки
    player.other = ''  # другие умения
    player.skills = ''  # навыки
    player.equipment = ''  # снаряжение


#                  ==//== Кубики ==//==
@dp.message_handler(lambda message: message.text[:4] == 'dice')
async def action_cancel(message: Message):
    # await message.answer(f"Вы выбрали {message.text[-4:]}", reply_markup=dice_kb)
    if message.text[-4:] == '  D4':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 4))}', reply_markup=dice_kb)
    elif message.text[-4:] == '  D6':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 6))}', reply_markup=dice_kb)
    elif message.text[-4:] == '  D8':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 8))}', reply_markup=dice_kb)
    elif message.text[-4:] == ' D10':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 10))}', reply_markup=dice_kb)
    elif message.text[-4:] == ' D12':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 12))}', reply_markup=dice_kb)
    elif message.text[-4:] == ' D20':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 20))}', reply_markup=dice_kb)
    elif message.text[-4:] == 'D100':
        await message.answer(f'Вы выбрали{message.text[-4:]} 🎲 = итого {str(randint(1, 100))}', reply_markup=dice_kb)


if __name__ == "__main__":
    #  при старте в консоль выводится статус подключения а админу приходит сообщение о старте бота
    print(requests.get(f'https://api.telegram.org/bot{TOKEN_BOT}/sendMessage?chat_id={ADMIN_CHAT_ID}&text=бот_start'))

    executor.start_polling(dp)
