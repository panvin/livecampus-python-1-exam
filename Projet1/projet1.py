#########################################################################################
#                      Projet 1 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

from ModuleVincent.basic_user_interface import BasicUserInterface
from ModuleCedric.Module_Cédric import * 

def main():

#    ui = BasicUserInterface()
#    ui.start()
    # Il faut que la liste des catégorie soit retournées sous le format
#    {
#        "1": ["id", "name"],
#        "2": ["id", "name"],
#        etc...
#        }
#   puis on peux appeler la méthode suivante
#   ui.choose_category(dict)    

#    json_game = SearchGame(ui.get_choice("game")).get_game()
    json_game = SearchGame("j1nem5x1").get_game()
    
    game_category = SearchCategory("j1nem5x1")
    json_category = game_category.get_category()

    game_category.set_category("824r4wgd")
    
    json_leaderboard = game_category.get_leaderboard() 

#    print(ui.get_choice("game"))
#    print(ui.get_choice("category"))

#    print(ui.get_choices())

if __name__ == "__main__":
    main()
