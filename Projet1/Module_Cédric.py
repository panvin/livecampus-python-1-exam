import requests

class Runner():     
    
    def __init__(self, nickname):
        
        self.nickname = nickname
        
    def get_runner(self):
        #Get nickname in speedrun database 
        url = "https://www.speedrun.com/api/v1/users/"
        response_API = requests.get(f'{url}{self.nickname}')
        
        return response_API.json()
        
        
class SearchGame():
    
    def __init__(self, gamename):
        
        self.gamename = gamename
    
    def get_game(self):
        #Get name of the game and att to the url
        url = "https://www.speedrun.com/api/v1/games/"
        response_API = requests.get(f'{url}{self.gamename}')
        
        return response_API.json()  
        
class SearchCategory():
    
    def __init__(self, gamename):
        
        self.gamename = gamename
        self.selected_category = ""
           
    def get_category(self):
        
        
        url_categories = (f"https://www.speedrun.com/api/v1/games/{self.gamename}/categories")
        categories_API = requests.get(url_categories)
        
        return categories_API.json()
            
    def get_leaderboard(self):
        
        #if self.selected_category in self.categories:
            url_leaderboard = (f"https://www.speedrun.com/api/v1/leaderboards/{self.gamename}/category/{self.selected_category}")
            leaderboard_API = requests.get(url_leaderboard)
            
            return leaderboard_API.json()
        
    def set_category(self, chosen_category):
        
        self.selected_category = chosen_category
        
#print(Runner("CeDiBuG").get_runner())
#print(SearchGame("re4steam").get_game())               
#print(SearchCategory("re4steam").get_category()) 
        
#tg = SearchCategory("re4steam")
#tg.set_category("xd17p04d")
#print(tg.get_leaderboard())

#print(SearchCategory("re4steam").get_category())     
