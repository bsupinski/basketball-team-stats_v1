import constants
from state import distrubuted_teams
from helpers import enter_option, display_players, display_team_stats

def introduction():
    print("\n\nBasketball Team Stats Tool\n\n     --Menu--\n\n")


def menu_choice():
    print("\nHere are your choices: \nA) Display Team stats\nB) Show All Player\nC) Quit")
    user_menu_choice = enter_option()
    while user_menu_choice != "A" and user_menu_choice != "B" and user_menu_choice != "C":
        print("You entered an invalid entry. Please choose one of the following \nA) Display Team stats\nB) Show All Player\nC) Quit")
        user_menu_choice = enter_option()
    if user_menu_choice == "B":
        display_players(constants.PLAYERS)
        menu_choice()
    elif user_menu_choice == "C":
        quit()


def choose_team():
    print("Choose which team's stats to view\n\n1) Panthers\n2) Bandits\n3) Warriors\n4)Quit\n")
    user_menu_option = enter_option()
    while user_menu_option != "1" and user_menu_option != "2" and user_menu_option != "3" and user_menu_option != "4":
        print("""You entered an invalid entry. Please choose the following\n1) Panthers\n2) Bandits\n3) Warriors\n4) Quit\n""")
        user_menu_option = enter_option()
    user_menu_option = int(user_menu_option)
    if user_menu_option == 1 or user_menu_option == 2 or user_menu_option == 3:
        display_team_stats(constants.TEAMS[user_menu_option - 1], distrubuted_teams[user_menu_option - 1])
    elif user_menu_option == 4:
        quit()


def replay():
    users_input = input("If you would like choose more informaion to view hit 'Enter':   ")
    if users_input == "":
        menu_choice()
        choose_team()
        replay()
    else:
        quit()

if __name__ == "__main__":
    introduction()
    menu_choice()
    choose_team()
    replay()