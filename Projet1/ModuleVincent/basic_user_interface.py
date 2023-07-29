import sys

class BasicUserInterface:

    def __init__(self):
        self.max_leaderboard = 30
        self.allowed_games= {
            "1": ["j1nem5x1", "RE 4 (steam)"],
            "2": ["76rkwed8", "Nier Automata"]
        }
        self.categories_dict = {}
        self. msg_dict = {
            "welcome" : "Bienvenue sur l'outil de sélection de Leaderboard!!",
            "game": "Choisissez votre jeu (\"exit\" pour quitter): ", 
            "category": "Choisissez la catégorie  (\"exit\" pour quitter):",
            "maximum": f"Choisissez le nombre de lignes dans le leaderboard  (max {self.max_leaderboard} - \"exit\" pour quitter): "
        }
        self. choice_dict = {}


    def start(self) -> None:
        self.print_msg("welcome")        
        self.print_choice("game", self.allowed_games)

    def choose_category(self, categories_dict = {}) -> None:
        if categories_dict:
            self.categories_dict = categories_dict
        if  self.categories_dict:
            self.print_choice("category", self.categories_dict)
        else:
            print("Une erreur s'est produit, il n'y a pas de catégorie associé à ce jeu")
    
    
    def choose_maximum(self):
        self.print_msg("maximum")
        print(f"(1 - {self.max_leaderboard})")
        self.ask_for_choice_max()


    def print_choice(self, element: str, choice_dict: dict ):
        self.print_msg(element)
        self.print_item_choice(choice_dict)
        self.ask_for_choice(element, choice_dict)

    def print_item_choice(self, choice_dict: dict):
        for key, value  in choice_dict.items():
            print(f"{key} - {value[1]}")

    def print_msg(self, key: str) -> None:
        print(self.msg_dict[key])

    def ask_for_choice(self, choice_key: str, choice_dict: dict):
        is_choice_correct = False
        while not is_choice_correct :
            choice = input()
            if choice in choice_dict:
                self.choice_dict[choice_key] = choice_dict[choice][0]
                is_choice_correct = True
            elif "exit" == choice :
                print("Arrêt de l'éxécution du script!")
                sys.exit()
            else:
                print("La valeur entrée est incorrecte")

    def ask_for_choice_max(self):
        is_choice_correct = False
        while not is_choice_correct :
            choice = input()
            choice_as_number = int(choice)
            if 1 <= choice_as_number <= self.max_leaderboard:
                self.choice_dict["maximum"] = choice_as_number
                is_choice_correct = True
            elif "exit" == choice :
                print("Arrêt de l'éxécution du script!")
                sys.exit()
            else:
                print("La valeur entrée est incorrecte")


    def set_categories(self, categories_dict: dict[str, list]) -> None:
        self.categories_dict = categories_dict
    
    def get_choices(self) -> dict:
        return self.choice_dict
    
    def get_choice(self, choice_id) -> str:
        return self.choice_dict[choice_id]