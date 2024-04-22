from app.Items.armor_class import ArmorClass


class Chainmail(ArmorClass):
    def __init__(self, name, defense_points, armor_type, description, durability):
        super().__init__(name, defense_points, armor_type, description, durability)

    def __str__(self):
        return f'{self._name}'

    def damage_armor(self, damage):
        self._durability -= round(damage/4)

    def amend_armor(self, price):
        self._durability += price >= 10 if self._durability + 4 else self._durability + 1

