import copy
import helpers
from constants import PLAYERS


teams =[],[],[]
player_list = helpers.clean_list(copy.deepcopy(PLAYERS)) 
sorted_teams = helpers.sort_players(player_list)
distrubuted_teams = helpers.distribute_player(sorted_teams, teams)


if __name__ == "__main__":
    print(helpers.display_team_stats(distrubuted_teams[0]))