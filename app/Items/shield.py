from app.Items.armor_class import ArmorClass


class Shield(ArmorClass):
    def __init__(self, name, defense_points, armor_type, description, shield_type, durability):
        super().__init__(name, defense_points, armor_type, description, durability)
        self.shield_type = shield_type

    def __str__(self):
        return f'{self._name}'

    def damage_armor(self, damage):
        self._durability -= round(damage / 3)

    def amend_armor(self, price):
        self._durability += price >= 5 if self._durability + 4 else self._durability + 1
