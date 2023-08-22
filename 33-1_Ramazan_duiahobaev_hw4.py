from enum import Enum
from random import randint, choice


class Ability(Enum):
    BOOST = 6
    HEAL = 0
    CRITICAL_DAMAGE = 1
    BLOCK_DAMAGE_AND_REVERT = 5


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

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
        return f'{self.__name} HEALTH: {self.__health} DAMAGE: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self):
        abilities_list = [e for e in Ability]
        self.__defence = choice(abilities_list)

    def attack(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                if type(hero) == Berserk:
                    hero.blocked_damage = self.damage // hero.super_ability.value
                    hero.health -= self.damage - hero.blocked_damage
                else:
                    hero.health -= self.damage

    def __str__(self):
        return 'BOSS ' + super().__str__() + f' DEFENCE: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if type(super_ability) == Ability:
            self.__super_ability = super_ability
        else:
            raise ValueError('Data type of attribute super_ability must be enum Ability')

    @property
    def super_ability(self):
        return self.__super_ability

    def attack(self, boss):
        boss.health -= self.damage

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        # Warrior applies CRIT
        coeff = randint(2, 6)
        boss.health -= coeff * self.damage
        print(f'Warrior {self.name} hits critically {coeff * self.damage}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BOOST)
        self.boost_active = False  # Флаг, показывающий, активирован ли BOOST в текущем раунде

    def apply_super_power(self, boss, heroes):
        if not self.boost_active:
            boost_amount = 10  # Замените на нужное значение
            for hero in heroes:
                hero.damage += boost_amount
            self.boost_active = True

    def after_round(self, boss):
        self.boost_active = False

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.used_ability = False

    def apply_super_power(self, boss, heroes):
        if not self.used_ability:
            boss_damage = boss.damage
            boss.damage = 0
            self.used_ability = True
        else:
            print(f"{self.name} оглушил босса!")

    def after_round(self, boss):
        if self.used_ability:
            boss.damage = boss_damage
            self.used_ability = False

class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.used_ability = False

    def apply_super_power(self, boss, heroes):
        if not self.used_ability:
            boss.damage = 0
            self.used_ability = True

    def after_round(self):
        if self.used_ability:
            self.used_ability = False


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, Ability.BLOCK_DAMAGE_AND_REVERT)
        self.__blocked_damage = 0

    @property
    def blocked_damage(self):
        return self.__blocked_damage

    @blocked_damage.setter
    def blocked_damage(self, value):
        self.__blocked_damage = value

    def apply_super_power(self, boss, heroes):
        # Berserk revert blocked damage
        boss.health -= self.__blocked_damage
        print(f'Berserk {self.name} blocked and reverted {self.blocked_damage}')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, Ability.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        # Medic heals
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health += self.__heal_points


round_number = 0


def start():
    boss = Boss('Gargarab', 5000, 200)

    warrior_1 = Warrior('Rudolf', 290, 10)
    warrior_2 = Warrior('Guts', 260, 15)
    doc = Medic('Haus', 250, 5, 15)
    magic = Magic('Petr', 270, 20)
    berserk_1 = Berserk('Conan', 260, 10)
    assistant = Medic('Marty', 300, 5, 5)
    thor = Thor("Chris", 280, 25)
    witcher = Witcher("Lambert", 280, 15)
    heroes_list = [warrior_1, warrior_2, doc, magic, berserk_1, assistant,thor,witcher]

    show_statistics(boss, heroes_list)
    while not is_game_over(boss, heroes_list):
        play_round(boss, heroes_list)


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss.choose_defence()
    boss.attack(heroes)
    for hero in heroes:
        if hero.health > 0 and boss.health > 0 and hero.super_ability != boss.defence:
            hero.attack(boss)
            hero.apply_super_power(boss, heroes)
    show_statistics(boss, heroes)


def show_statistics(boss, heroes):
    print(f'ROUND {round_number} -------------')
    print(boss)
    for hero in heroes:
        print(hero)


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


start()
