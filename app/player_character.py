from app.Items.armor_class import ArmorClass
from app.defense_level import DefenseLevel


class PlayerCharacter:
    characters = []
    armor_items = []

    def __init__(self, name, heroic_class, hp, weapon, armors):
        self._name = name
        self._heroic_class = heroic_class
        self._hp = hp
        self._active = False
        self. _weapon = weapon
        self._armor_items = armors
        self._defense_level = self.set_defense_level
        PlayerCharacter.characters.append(self)

    def __str__(self):
        return f'{self._name}, {self._heroic_class}'

    @classmethod
    def list_characters(cls):
        print(
            f'{"Characters name".ljust(25)} | {"Heroic Class".ljust(25)} | {"HP".ljust(25)} | {"Weapon".ljust(25)} | {"Defense Level".ljust(25)} | {"Equipped Items".ljust(25)} | {"Status".ljust(25)}')
        for character in PlayerCharacter.characters:
            armor_names = ', '.join(armor._name for armor in character._armor_items)
            print(
                f'{character._name.ljust(25)} | {character._heroic_class.ljust(25)} | {str(character._hp).ljust(25)} | {str(character._weapon._name).ljust(25)} | {str(character._defense_level).ljust(25)} | {armor_names.ljust(25)} | {character.active}')

    @property
    def active(self):
        return '⌧' if self._active else '☐'

    def attack(self, enemy):
        if self._weapon._attack_points > enemy._defense_level:
            print(f'{self._name} successfully attack {enemy._name}' )
            enemy._hp -= self._weapon._damage_points
            for armor in enemy._armor_items:
                armor.damage_armor(self._weapon._damage_points)
        else:
            print(f'{self._name} You miss!')
    def deactivate_activate(self):
        self._active = not self._active

    def equip_armor(self, armor_items):
        defense_level = []

        for armor in armor_items:
            if isinstance(armor, ArmorClass):
                defense_level.append(self.define_defense_level(armor))
            else:
                self._armor_items.remove(armor)
                print(f'{armor._name} isn\'t an ArmorClass, {self._name} cannot equip it as a defense item')
        return defense_level

    def define_defense_level(self, armor):
        defense_level = DefenseLevel(armor._armor_type, armor._defense_points)
        return defense_level

    @property
    def set_defense_level(self):
        defense_levels = self.equip_armor(self._armor_items)
        if not defense_levels:
            return 0
        sum_defense = sum(defense_level.points for defense_level in defense_levels)
        return sum_defense
