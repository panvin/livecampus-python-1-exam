import requests
import csv 
import json

def main():
    print("Choix")
    print('1 - Chercher un runner')
    print('2 - Chercher un jeu')
    main_choice = input('Exercice 3 → ')
    if main_choice == "1":
        Runner()
    if main_choice == "2":
        Games()
    else : 
        main()

def Runner():
    print("Pseudo pour exemple : CeDIBuG")
    profile_search = input("Entrez le pseudo du runner : ")
    url = "https://www.speedrun.com/api/v1/users/"
    response_API = requests.get(f'{url}{profile_search}')

    name = response_API.json()['data']['names']['international']
    print(f"Nom : {name}")
    country = response_API.json()['data']['location']['country']['names']['international']
    print(f"Pays : {country}")
    ville = response_API.json()['data']['location']['region']['names']['international']
    print(f"Ville : {ville}")
    twitch = response_API.json()['data']['twitch']
    print(f"Twitch : {twitch}")
    youtube = response_API.json()['data']['youtube']['uri']
    print(f"Youtube : {youtube}")

    csv_save = input("Voulez vous sauvegarder le profil ? o/n ")
    if csv_save == "o":
        with open('D:\LiveCampus\python\Exercice\Exercice 4\cvs.cvs', 'wb') as csvfile:
            writer = csv.DictWriter(csvfile, response_API)
            writer.writeheader()
            writer.writerow(response_API)
    else : 
        quit()
        
def Games():
    print("Jeux pour exemple : Re4steam")
    game_search = input("Entrez le nom du jeu : ")
    url = "https://www.speedrun.com/api/v1/games/"
    response_API = requests.get(f'{url}{game_search}')

    name = response_API.json()['data']['names']['international']
    print(f"Nom : {name}")
    date = response_API.json()['data']['release-date']
    print(f"Date de sortie : {date}")
    print("Afficher les categories ?")
    ask_categorie = input(" o / n : ")
    if ask_categorie == "o":
        url_categories = (f"https://www.speedrun.com/api/v1/games/{game_search}/categories")
        categories_API = requests.get(url_categories)
        categories = categories_API.json()['data']
        for category in categories:
            print(f" Categories :  {category['name']}")
    else :
        quit()

                
main()