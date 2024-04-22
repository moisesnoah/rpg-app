import os

player_characters = []


def show_app_name():
    print("""
    
    █▄─▄▄▀█▄─▄▄─█─▄▄▄▄███▀▀▀▀▀████─▄─▄─█─▄▄─█─▄▄▄▄██▀▄─██
    ██─▄─▄██─▄▄▄█─██▄─██████████████─███─██─█─██▄─██─▀─██
    ▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
    """)


def show_options():
    print('1. Create Player Player_character')
    print('2. List active PCs ')
    print('3. List inactive PCs ')
    print('4. Activate PC')
    print('5. Exit\n')


def invalid_option():
    print('Invalid option!\n')
    input('Type any key to go back to main menu: ')
    main()


def create_pc():
    subtitle('Creating new Characters: ')
    pc_name = input('Enter your character name: ')
    pc_class = input(f'Enter {pc_name} heroic class: ')
    pc_sheet = {'name': pc_name, 'class': pc_class, 'active': False}
    player_characters.append(pc_sheet)
    print(f'The character {pc_name} was successfully created.')
    input('Press any key to go back to main menu: ')
    main()


def list_all_active_pcs():
    subtitle('Here are the available characters:')
    for character in player_characters:
        if character['active']:
            print(f'{character["name"]} | {character["class"]} | {character["active"]}')
    input('press any key to go back to main menu: ')
    main()

def list_all_inactive_pcs():
    subtitle('Here are the available characters:')
    for character in player_characters:
        if not character['active']:
            print(f'{character["name"]} | {character["class"]} | {character["active"]}')
    input('press any key to go back to main menu: ')
    main()


def subtitle(param):
    os.system('cls')
    line = '*' * (len(param))
    print(line)
    print(param)
    print(line)
    print()


def active_character():
    subtitle('Activate characters:')
    character_name = input('Enter the name of the character: ')
    for character in player_characters:
        if character['name'] == character_name:
            character['active'] = True
    print(f'The character {character_name} was successfully activated')
    input('press any key to go back to main')
    main()


def choose_option():
    try:
        option = int(input('Choose an option: '))
        if option == 1:
            create_pc()
        elif option == 2:
            list_all_active_pcs()
        elif option == 3:
            list_all_inactive_pcs()
        elif option == 4:
            active_character()
        elif option == 5:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()


def end_app():
    os.system('cls')
    print('Closing application!\n')


def main():
    os.system('cls')
    show_app_name()
    show_options()
    choose_option()


if __name__ == '__main__':
    main()
