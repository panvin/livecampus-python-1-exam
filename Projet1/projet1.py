#########################################################################################
#                      Projet 1 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

from ModuleVincent.basic_user_interface import BasicUserInterface
from ModuleCedric.Module_Cédric import * 
from moduleAnne.classesPandas import JsonToDictionnary
from pprint import pprint
import time

def main():

    ui = BasicUserInterface()
    json_tool = JsonToDictionnary()

    data = {
        "Game": "",
        "Release date": "",
        "Category": "",
        "Leaderboard": [["Position", "Player", "Realgit add Time"]]
    }

    ui.start()
    # Récupération des informations du jeu
    json_game = SearchGame(ui.get_choice("game")).get_game()
    game_infos = json_tool.export_json_games(json_game)
    data["Game"] = game_infos["1"][0]
    data["Release date"] = game_infos["1"][1]

    # Récupération et choix des catégories
    game_categories = SearchCategory(ui.get_choice("game"))
    catogories_dict = json_tool.export_json_categories(game_categories.get_category())
    ui.set_categories(catogories_dict)
    
    ui.choose_category()

    for key,values in catogories_dict.items():
        if ui.get_choice("category") in values:
            data["Category"] = values [1]

    game_categories.set_category(ui.get_choice("category"))
    json_leaderboard = game_categories.get_leaderboard()

    leaderboard_dict = json_tool.export_json_leaderboard(json_leaderboard)

    # Choix du maximum de lignes
    ui.choose_maximum()
    leaderboard_with_pseudo = []
    
    for i in range(1, ui.get_choice("maximum") + 1):
        player_id = leaderboard_dict[str(i)][0]
        pseudo = json_tool.export_pseudo(Runner(player_id).get_runner())
        player_time = leaderboard_dict[str(i)][1]
        leaderboard_with_pseudo.append([str(i),pseudo, player_time[2:]])
        time.sleep(2)
    
    data["Leaderboard"].append(leaderboard_with_pseudo)
    pprint(data)

if __name__ == "__main__":
    main()
