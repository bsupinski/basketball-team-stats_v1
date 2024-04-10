import constants
from helpers import clean_list, enter_option

def introduction():
    print("\n\nBasketball Team Stats Tool\n\n     --Menu--\n\n")
    print("\nHere are your choices: \nA) Display Team stats\nB) Quit")


def menu_choice():
    user_menu_choice = enter_option()
    print(user_menu_choice)
    while user_menu_choice != "A" and user_menu_choice != "B":
        user_menu_choice = enter_option()
    if user_menu_choice == "B":
        quit()


def choose_team():
    print("Choose which team's stats to view\n\nA) Panthers\nB) Bandits\nC) Warriors\n\n")
    return enter_option()

if __name__ == "__main__":
    player_list = clean_list(constants.PLAYERS)
    introduction()
    menu_choice()
    choose_team()