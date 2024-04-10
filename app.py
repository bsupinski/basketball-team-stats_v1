import constants
import copy
from helpers import clean_list, enter_option, display_players

players_list = clean_list(copy.deepcopy(constants.PLAYERS))

def introduction():
    print("\n\nBasketball Team Stats Tool\n\n     --Menu--\n\n")


def menu_choice():
    print("\nHere are your choices: \nA) Display Team stats\nB) Show All Player\nC) Quit")
    user_menu_choice = enter_option()
    print(user_menu_choice)
    while user_menu_choice != "A" and user_menu_choice != "B" and user_menu_choice != "C":
        user_menu_choice = enter_option()
    if user_menu_choice == "B":
        display_players(constants.PLAYERS)
        menu_choice()
    elif user_menu_choice == "C":
        quit()

def choose_team():
    print("Choose which team's stats to view\n\nA) Panthers\nB) Bandits\nC) Warriors\n\n")
    return enter_option()

if __name__ == "__main__":
    introduction()
    menu_choice()
    choose_team()