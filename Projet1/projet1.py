#########################################################################################
#                      Projet 1 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

from ModuleVincent.basic_user_interface import BasicUserInterface

def main():

    ui = BasicUserInterface()
    ui.start()
    # Il faut que la liste des catégorie soit ajoutées sous le format
#    {
#        "1": ["id", "name"],
#        "2": ["id", "name"],
#        etc...
#        }
#   puis on peux appeler la méthode suivante
#   ui.choose_category(dict)    

    ui.choose_category()

    print(ui.get_choice("game"))
    print(ui.get_choice("category"))

    print(ui.get_choices())

if __name__ == "__main__":
    main()
