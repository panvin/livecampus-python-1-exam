#########################################################################################
#                      Projet 1 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

# Projet Github: https://github.com/panvin/livecampus-python-1-exam

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
        "Leaderboard": [["Position", "Player", "RealTime"]]
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
    print(leaderboard_dict)

    # Choix du maximum de lignes
    ui.choose_maximum()
    leaderboard_with_pseudo = []

    # Récupération de la valeur max en input et on la remplace si elle est supérieure au nombre de données présentes
    max_range = ui.get_choice("maximum")
    if len(leaderboard_dict) < max_range:
        max_range = len(leaderboard_dict)
    
    # Création de notre lot de donnée du leaderboard
    for i in range(1, max_range + 1):
        player_id = leaderboard_dict[str(i)][0]
        if "guest =" in player_id:
            pseudo = player_id[8:]
        else:
            pseudo = json_tool.export_pseudo(Runner(player_id).get_runner())
        player_time = leaderboard_dict[str(i)][1][2:].replace("H", " h ").replace("M"," min ").replace("S", " sec ")
        leaderboard_with_pseudo.append([str(i),pseudo, player_time])
        
        # Attente entre chaque requête pour éviter de surcharger le serveur 
        time.sleep(1)
    
    data["Leaderboard"].append(leaderboard_with_pseudo)
    pprint(data)

if __name__ == "__main__":
    main()
