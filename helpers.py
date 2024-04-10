def enter_option():
    return input("Enter an option:  ").upper()

def change_to_bool(lst):
    """Change the yes/no of 'experience' value to True/False"""
    for player in lst:
        if player["experience"] == "True":
            player["experience"] = True
        else:
            player["experience"] = False


def get_guardians(lst):
    """Takes the 'guardians' value and changes it to a list of just full names"""
    for player in lst:
        player["guardians"] = player["guardians"].replace("and", "")
        if "  " in player["guardians"]:
            player["guardians"] = player["guardians"].split("  ")
        else: 
            player["guardians"] = [player["guardians"]]


def change_to_int(lst):
    """Change the height from a string to an integer"""
    for player in lst:
        player["height"] = int(player["height"].split(" ")[0])


def clean_list(lst):
    """Applies the seperate cleaning functions into one"""
    change_to_bool(lst) 
    get_guardians(lst)
    change_to_int(lst)
    return lst


def display_players(lst):
    for index, player in enumerate(lst, 1):
        print(f"{index}: {player['name']}\n{player['guardians']}\n{player['experience']}\n{player['height']}\n")