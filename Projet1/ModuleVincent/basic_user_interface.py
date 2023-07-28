import sys

class BasicUserInterface:

    def __init__(self):
        self.max_leaderboard = 10
        self.allowed_games= {
            "1": ["j1nem5x1", "RE 4 (steam)"],
            "2": ["n268nk6p", "Half-life"]
        }
        self.categories_dict = {
            "1" : ["824r4wgd", "New Game"],
            "2" : ["9d8g9r3k", "New Game+"],
            "3" : ["xd17p04d", "Separate Ways"],
            "4" : ["zd37egv2", "Separate Ways+"],
            "5" : [ "9kvyz08k", "Assignment Ada"],
            "6" : ["rkljypnd", "No Merchant"],
            "7" : ["n2ym0q72", "Wesker"],
            "8" : ["wk645pod", "Hunk"],
            "9" : ["mke70oj2", "Ada"],
            "10": ["5dwxlj52", "Krauser"],
            "11": ["7dg7o8gd", "Leon"]
        }
        self. msg_dict = {
            "welcome" : "Bienvenue sur l'outil de sélection de Leaderboard!!",
            "game": "Choisissez votre jeu (\"exit\" pour quitter): ", 
            "category": "Choisissez la catégorie  (\"exit\" pour quitter):",
            "third_choice": f"Choisissez le nombre de lignes dans le leaderboard  (max {self.max_leaderboard} - \"exit\" pour quitter): "
        }
        self. choice_dict = {}


    def start(self) -> None:
        self.print_msg("welcome")        
        self.print_choice("game", self.allowed_games)

    def choose_category(self, categories_dict = "") -> None:
        #self.categories = categories_dict
        self.print_choice("category", self.categories_dict)

    def choose_max_leaderboard(self):
        self.print_choice("second_choice", self.categories_dict)


    def print_choice(self, choice_key: str, choice_dict: dict ):
        self.print_msg(choice_key)
        self.print_item_choice(choice_dict)
        self.ask_for_choice(choice_key, choice_dict)

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

    def get_choices(self) -> dict:
        return self.choice_dict
    
    def get_choice(self, choice_id) -> str:
        return self.choice_dict[choice_id]

