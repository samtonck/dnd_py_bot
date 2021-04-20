
def mod_saving():
    saving_throws_strength = (strength - 10) // 2  # модификатор сила
    saving_throws_dexterity = (dexterity - 10) // 2  # модификатор ловкость
    saving_throws_constitution = (constitution - 10) // 2  # модификатор телосложение
    saving_throws_intelligence = (intelligence - 10) // 2  # модификатор интеллект
    saving_throws_wisdom = (wisdom - 10) // 2  # модификатор мудрость
    saving_throws_charisma = (charisma - 10) // 2  # модификатор харизма
    return (saving_throws_strength, saving_throws_dexterity, saving_throws_constitution, saving_throws_intelligence,
            saving_throws_wisdom, saving_throws_charisma)


def mod_stat():
    mod_strength = (strength - 10) // 2  # модификатор сила
    mod_dexterity = (dexterity - 10) // 2  # модификатор ловкость
    mod_constitution = (constitution - 10) // 2  # модификатор телосложение
    mod_intelligence = (intelligence - 10) // 2  # модификатор интеллект
    mod_wisdom = (wisdom - 10) // 2  # модификатор мудрость
    mod_charisma = (charisma - 10) // 2  # модификатор харизма
    return mod_strength, mod_dexterity, mod_constitution, mod_intelligence, mod_wisdom, mod_charisma


def mod_skill():
    acrobatics = (dexterity - 10) // 2  # акробатика
    perception = (intelligence - 10) // 2  # анализ
    athletics = (strength - 10) // 2  # атлетика
    investigation = (wisdom - 10) // 2  # внимательность
    survival = (wisdom - 10) // 2  # выживание
    performance = (charisma - 10) // 2  # выступление
    intimidation = (charisma - 10) // 2  # запугивание
    history = (intelligence - 10) // 2  # история
    sleight_of_hand = (dexterity - 10) // 2  # ловкость рук
    arcana = (intelligence - 10) // 2  # магия
    medicine = (wisdom - 10) // 2  # медицина
    deception = (charisma - 10) // 2  # обман
    nature = (intelligence - 10) // 2  # природа
    insight = (wisdom - 10) // 2  # проницательность
    religion = (intelligence - 10) // 2  # религия
    stealth = (dexterity - 10) // 2  # скрытность
    persuasion = (charisma - 10) // 2  # убеждение
    animal_handling = (wisdom - 10) // 2  # уход за животными
    return (acrobatics, perception, athletics, investigation, survival, performance, intimidation, history,
            sleight_of_hand, arcana, medicine, deception, nature, insight, religion, stealth, persuasion,
            animal_handling)


name_player = ''

name = ''  # имя персонажа
game_gender = ''  # пол персонажа
age = 0  # возраст персонажа
height = 0  # рост персонажа
weight = 0  # вес персонажа

race = ''  # раса
game_class = ''  # класс
background = ''  # предыстория
alignment = ''  # мировоззрение

like_mechanics = ''  # призвание/гильдия/судьбоносное происшествие
personality_traits = ''  # черты характера
ideals = ''  # идеалы
bonds = ''  # привязанности
flaws = ''  # слабости

level = 0  # уровень
experience_point = 0  # опыт
proficiency_bonus = 0  # бонус мастерства


strength = 0  # сила
dexterity = 0  # ловкость
constitution = 0  # телосложение
intelligence = 0  # интеллект
wisdom = 0  # мудрость
charisma = 0  # харизма

mod_strength = 0  # модификатор сила
mod_dexterity = 0  # модификатор ловкость
mod_constitution = 0  # модификатор телосложение
mod_intelligence = 0  # модификатор интеллект
mod_wisdom = 0  # модификатор мудрость
mod_charisma = 0  # модификатор харизма

check_saving_throws_strength = False  # знание спас бросок сила
check_saving_throws_dexterity = False  # знание  спас бросок ловкость
check_saving_throws_constitution = False  # знание  спас бросок телосложение
check_saving_throws_intelligence = False  # знание  спас бросок интеллект
check_saving_throws_wisdom = False  # знание  спас бросок мудрость
check_saving_throws_charisma = False  # знание  спас бросок харизма

saving_throws_strength = mod_strength  # спас бросок сила
saving_throws_dexterity = mod_dexterity  # спас бросок ловкость
saving_throws_constitution = mod_constitution  # спас бросок телосложение
saving_throws_intelligence = mod_intelligence  # спас бросок интеллект
saving_throws_wisdom = mod_wisdom  # спас бросок мудрость
saving_throws_charisma = mod_charisma  # спас бросок харизма

check_acrobatics = False  # знание акробатика
check_perception = False  # знание анализ
check_athletics = False  # знание атлетика
check_investigation = False  # знание внимательность
check_survival = False  # знание выживание
check_performance = False  # знание выступление
check_intimidation = False  # знание запугивание
check_history = False  # знание история
check_sleight_of_hand = False  # знание ловкость рук
check_arcana = False  # знание магия
check_medicine = False  # знание медицина
check_deception = False  # знание обман
check_nature = False  # знание природа
check_insight = False  # знание проницательность
check_religion = False  # знание религия
check_stealth = False  # знание скрытность
check_persuasion = False  # знание убеждение
check_animal_handling = False  # знание уход за животными

acrobatics = mod_dexterity  # акробатика
perception = mod_intelligence  # анализ
athletics = mod_strength  # атлетика
investigation = mod_wisdom  # внимательность
survival = mod_wisdom  # выживание
performance = mod_charisma  # выступление
intimidation = mod_charisma  # запугивание
history = mod_intelligence  # история
sleight_of_hand = mod_dexterity  # ловкость рук
arcana = mod_intelligence  # магия
medicine = mod_wisdom  # медицина
deception = mod_charisma  # обман
nature = mod_intelligence  # природа
insight = mod_wisdom  # проницательность
religion = mod_intelligence  # религия
stealth = mod_dexterity  # скрытность
persuasion = mod_charisma  # убеждение
animal_handling = mod_wisdom  # уход за животными

passive_wisdom = 10 + mod_wisdom  # пассивная мудрость (внимательность)

armor_class = 0  # КД (класс доспеха)
initiative = dexterity  # инициатива
speed = 0  # скорость

hit_point_maximum = 0  # максимальное кол-во очков жизни
hit_dise = ''  # кубик жизни

dark_vision = ''  # темное зрение
language = ''  # языки
other = ''  # другие умения
skills = ''  # навыки
equipment = ''  # снаряжение
