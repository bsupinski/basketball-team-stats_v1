from operator import itemgetter

def clean_list(lst):
    """Applies the seperate cleaning functions into one"""
    change_to_bool(lst) 
    get_guardians(lst)
    change_to_int(lst)
    return lst


def enter_option():
    return input("Enter an option:  ").upper()


def change_to_bool(lst):
    """Change the yes/no of 'experience' value to True/False"""
    for player in lst:
        if player["experience"] == "YES":
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


def display_players(lst):
    for index, player in enumerate(lst, 1):
        print(f"{index}: {player['name']}\nGuardians: {player['guardians']}\nExperience: {player['experience']}\nHeight: {player['height']}\n")


def distribute_player(lst, newlst):
    for player in lst:
        if (lst.index(player) + 1) % 3 == 0:
            newlst[0].append(player)
        elif (lst.index(player) + 1) % 2 == 0:
            newlst[1].append(player)
        else:
            newlst[2].append(player)
    return newlst


def sort_players(lst):
    return sorted(lst, key=itemgetter("experience"))


def get_average_height(lst):
    return round(sum(player["height"] for player in lst) / len(lst), 2)


def list_players(lst):
    names = []
    for players in lst:
        names.append(players["name"])
    return ", ".join(names)


def display_team_guardians(lst):
    team_guardians =[]
    [team_guardians.extend(player["guardians"]) for player in lst]
    return ", ".join(team_guardians)


def get_total_experience(lst, experienced):
    total = 0
    for player in lst:
        if player["experience"] == experienced:
            total+=1
    return total


def display_team_stats(team_name, team):
    print(f"""
Team: {team_name}
==================
Total Players: {len(team)}
Total experienced: {get_total_experience(team, True)}
Total inexperienced: {get_total_experience(team, False)} 
Average height: {get_average_height(team)}
Players Name:
    {list_players(team)}
Guardians: 
    {display_team_guardians(team)}
""")


# if __name__ == "__main__":
