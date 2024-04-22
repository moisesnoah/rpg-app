from abc import ABC, abstractmethod


class ArmorClass(ABC):
    armors = []

    def __init__(self, name, defense_points, armor_type, description, durability):
        self._name = name
        self._defense_points = defense_points
        self._armor_type = armor_type
        self._description = description
        self._durability = durability
        ArmorClass.armors.append(self)

    def __str__(self):
        return f'{self._name}, {self._defense_points}, {self._armor_type}, {self._description}'

    @classmethod
    def list_armors(cls):
        print(
            f'{'Armors name'.ljust(25)} | {'Defense Points'.ljust(25)} | {'Type'.ljust(25)} | {'Description'.ljust(25)} | {'Durability'.ljust(25)}')
        for armor in ArmorClass.armors:
            print(
                f'{armor._name.ljust(25)} | {str(armor._defense_points).ljust(25)} | {armor._armor_type.ljust(25)} | {armor._description.ljust(25)} | {str(armor._durability).ljust(25)}')

    @abstractmethod
    def damage_armor(self, damage):
        pass

    @abstractmethod
    def amend_armor(self, price):
        pass
