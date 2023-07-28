import requests

class Runner():
    
    def __init__ (self, nickname):
        
        self.nickname = nickname
        self.name = ""
        self.country = "" 
        self.ville = ""
        self.twitch = ""
        self.youtube = ""
        
        
    def get_runners(self):
        #Get nickname in speedrun database 
        url = "https://www.speedrun.com/api/v1/users/"
        response_API = requests.get(f'{url}{self.nickname}')
        
        #Get required data 
        self.name = response_API.json()['data']['names']['international']
        self.country = response_API.json()['data']['location']['country']['names']['international']
        self.ville = response_API.json()['data']['location']['region']['names']['international']
        self.twitch = response_API.json()['data']['twitch']
        self.youtube = response_API.json()['data']['youtube']['uri']
        
        #print all of them
        print(f"Nom : {self.name}")
        print(f"Pays : {self.country}")
        print(f"Ville : {self.ville}")
        print(f"Twitch : {self.twitch}")
        print(f"Youtube : {self.youtube}")
        
        
class SearchGame():
    
    def __init__ (self, gamename):
    
        self.gamename = gamename
        self.game_name = ""
        self.release_date = "" 
    
    def get_game(self):
        #Get name of the game and att to the url
        url = "https://www.speedrun.com/api/v1/games/"
        response_API = requests.get(f'{url}{self.gamename}')
        
        #Get data for API 
        self.game_name = response_API.json()['data']['names']['international']
        self.release_date = response_API.json()['data']['release-date'] 
        
        #Print data
        print(f"Nom du jeux : {self.game_name}")
        print(f"Date de sortie : {self.release_date}")
        
class SearchCategory():
    
    def __init__ (self, gamename):
    
        self.categories = ""
        self.selected_category = ""
        self.gamename = ""
        
    def get_category(self):
        
        url_categories = (f"https://www.speedrun.com/api/v1/games/{self.gamename}/categories")
        categories_API = requests.get(url_categories)
        self.categories = categories_API.json()['data']
        for category in self.categories:
            print(f" Categorie :  {category['id']} : {category['name']}")
            
    def get_leaderboard(self, gamename):
        
        #if self.selected_category in self.categories:
            url_leaderboard = (f"https://www.speedrun.com/api/v1/leaderboards/{self.gamename}/category/{self.selected_category}")
            leaderboard_API = requests.get(url_leaderboard)
            self.leaderboard = leaderboard_API.json()['data']['run']
            for Place in self.categories:
                print(f" Nom :  {Place['place']}")
                        
        