#########################################################################################
#                      Projet 1 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

from ModuleVincent.basic_user_interface import BasicUserInterface
from ModuleCedric.Module_Cédric import * 
from moduleAnne.classesPandas import JsonToDictionnary
from pprint import pprint

def main():

    ui = BasicUserInterface()
    json_tool = JsonToDictionnary()

    data = {
        "Game": "",
        "Release date": "",
        "Category": "",
        "Leaderboard": [["Position", "Player", "Time"]]
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

    print(ui.get_choice("category"))
    game_categories.set_category(ui.get_choice("category"))
    json_leaderboard = game_categories.get_leaderboard()

    leaderboard_dict = json_tool.export_json_leaderboard(json_leaderboard)

    pprint(leaderboard_dict)



#    ui.choose_category(dict)    
    
    
#    game_category = SearchCategory("j1nem5x1")
#    json_category = game_category.get_category()

#    game_category.set_category("824r4wgd")
    
#    json_leaderboard = game_category.get_leaderboard() 

#    print(ui.get_choice("game"))
#    print(ui.get_choice("category"))

#    print(ui.get_choices())

if __name__ == "__main__":
    main()
