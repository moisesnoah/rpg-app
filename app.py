from app.Items.weapon_class import WeaponClass
from app.player_character import PlayerCharacter
from app.Items.shield import Shield
from app.Items.leader_armor import LeaderArmor
from app.Items.chainmail import Chainmail
from app.Items.armor_class import ArmorClass


escudo_pesado = Shield('Escudo ORC', 5, 'Heavy-Armor', 'Iron forged Shield', 'IRON', 10)
chainmail = Chainmail('Faery Chainmail', 25, 'Heavy-Armor', 'Faery Forged Armor', 10)
leader_armor = LeaderArmor('Couraça Temperada', 8, 'Light Armor', 'Leader made Armor', 10)

sword = WeaponClass('Sword', 'Big sword', 2, 10)


armor_list1 = [chainmail, escudo_pesado, sword]
armor_list2 = [leader_armor]

bardo_humano = PlayerCharacter('Rufus Cave', 'Paladino', 10, sword, armor_list1)
barbaro_humano = PlayerCharacter('Ruprest Ruprestson', 'Barbaro', 10, sword, armor_list2)
bardo_humano.deactivate_activate()
def main():

    PlayerCharacter.list_characters()
    print()
    ArmorClass.list_armors()
    print()
    barbaro_humano.attack(bardo_humano)
    bardo_humano.attack(barbaro_humano)
    print()
    PlayerCharacter.list_characters()
    print()
    ArmorClass.list_armors()

if __name__ == '__main__':
    main()