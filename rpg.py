from enum import Enum
from random import randint, choice, random


class SuperAbility(Enum):
    HEAL = 1
    CRITICAL_DAMAGE = 2
    BOOST = 3
    BLOCK_DAMAGE_REVERT = 4
    TRAUMA = 5
    INVISIBLE = 6
    SUMMON = 7
    STUN = 8
    FEIGN_DEATH = 9
    SIZE_CHANGE = 10
    RANDOM_BUFF = 11
    STUN_BOSS = 12
    RANDOM_SIZE = 13
    VIRUS_VACCINE = 14
    EXPLOSION = 15
    REAPER = 16
    AGGRESSION = 17
    ONE_HIT_KO = 18
    GAMBLE = 19
    SACRIFICE = 20
    SHURIKEN = 21
    EXTRA_DAMAGE = 22
    SUMMON_SAITAMA = 23
    LUCKY_GAMBLER = 24


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__damage = damage
        self.__health = health

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        self.__defence = hero.ability

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if (hero.ability == SuperAbility.BLOCK_DAMAGE_REVERT and
                        self.defence != SuperAbility.BLOCK_DAMAGE_REVERT):
                    coef = randint(1, 2)
                    hero.blocked_damage = int(self.damage / (coef * 5))
                    hero.health -= (self.damage - hero.blocked_damage)
                else:
                    hero.health -= self.damage

    def __str__(self):
        return f'BOSS {super().__str__()} defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, ability):
        super().__init__(name, health, damage)
        self.__ability = ability

    @property
    def ability(self):
        return self.__ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coef = randint(2, 5)
        boss.health -= self.damage * coef
        print(f'Warrior {self.name} hit critically {self.damage * coef}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        pass


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.BLOCK_DAMAGE_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage,
                         SuperAbility.HEAL)
        self.__heal_points = heal_points

    @property
    def heal_points(self):
        return self.__heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


class Chikatilo(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Hanzhik(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Shakal(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health * 2, damage // 2,
                         SuperAbility.TRAUMA)

    def apply_super_power(self, boss, heroes):
        pass


class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.INVISIBLE)
        self.__invisible_count = 0

    def apply_super_power(self, boss, heroes):
        pass


class Druid(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.SUMMON)

    def apply_super_power(self, boss, heroes):
        pass


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        pass


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.FEIGN_DEATH)

    def apply_super_power(self, boss, heroes):
        pass


class Antman(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.SIZE_CHANGE)
        self.__original_health = health
        self.__original_damage = damage

    def apply_super_power(self, boss, heroes):
        pass


class Deku(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.RANDOM_BUFF)

    def apply_super_power(self, boss, heroes):
        pass


class Kamikadze(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health * 2, damage // 2,
                         SuperAbility.SACRIFICE)

    def apply_super_power(self, boss, heroes):
        pass


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.SHURIKEN)

    def apply_super_power(self, boss, heroes):
        pass


class Bomber(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.EXPLOSION)

    def apply_super_power(self, boss, heroes):
        pass


class Reaper(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.REAPER)

    def apply_super_power(self, boss, heroes):
        pass


class Spitfire(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.AGGRESSION)

    def apply_super_power(self, boss, heroes):
        pass


class King(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.ONE_HIT_KO)

    def apply_super_power(self, boss, heroes):
        pass


class Ludoman(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage,
                         SuperAbility.LUCKY_GAMBLER)

    def apply_super_power(self, boss, heroes):
        pass


round_number = 0


def start_game():
    boss = Boss('Tanos', 1000, 50)

    warrior_1 = Warrior('Ahiles', 280, 5)
    warrior_2 = Warrior('Sponge Bob', 270, 10)
    magic = Magic('Hendolf', 180, 20)
    berserk = Berserk('Gatz', 220, 20)
    doc = Medic('Haus', 250, 5, 15)
    junior = Medic('Zolo', 290, 5, 5)
    chikatilo = Chikatilo('Andrei', 200, 15, None)
    hanzhik_1 = Hanzhik('Oleg', 230, 10)
    hanzhik_2 = Hanzhik('Ivan', 200, 15)
    shakal_1 = Shakal('Vlad', 200, 5)
    shakal_2 = Shakal('Sergey', 200, 5)
    shakal_3 = Shakal('Nikolay', 200, 5)
    golem_1 = Golem('Golem1', 400, 10)
    golem_2 = Golem('Golem2', 400, 10)
    avrora = Avrora('Avrora', 250, 15)
    druid = Druid('Druid', 300, 10)
    thor = Thor('Thor', 220, 15)
    tricky_bastard = TrickyBastard('TrickyBastard', 240, 15)
    antman = Antman('Antman', 240, 20)
    deku = Deku('Deku', 250, 15)
    kamikadze = Kamikadze('Kamikadze', 400, 0)
    samurai = Samurai('Samurai', 260, 20)
    bomber = Bomber('Bomber', 280, 15)
    reaper = Reaper('Reaper', 300, 20)
    spitfire = Spitfire('Spitfire', 280, 20)
    king = King('King', 300, 0)
    ludoman = Ludoman('Ludoman', 270, 15)

    heroes_list = [warrior_1, warrior_2, magic, berserk, doc, junior, chikatilo, hanzhik_1, hanzhik_2,
                   shakal_1, shakal_2, shakal_3, golem_1, golem_2, avrora, druid, thor, tricky_bastard,
                   antman, deku, kamikadze, samurai, bomber, reaper, spitfire, king, ludoman]
    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def is_game_over(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print('Boss won!!!')
    return all_heroes_dead


def show_statistics(boss, heroes):
    print(f'ROUND: {round_number} ----------')
    print(boss)
    for hero in heroes:
        print(hero)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence(heroes)
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


start_game()