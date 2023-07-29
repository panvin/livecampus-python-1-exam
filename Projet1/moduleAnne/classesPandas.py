import pandas 
import pathlib
import sys
import os
from pprint import pprint
import json


dir_path = pathlib.Path(__file__).parent
games =  os.path.join(dir_path, "games.json")
categories =  os.path.join(dir_path, "categories.json")
leaderboard =  os.path.join(dir_path, "leaderboard.json")
pseudo = os.path.join(dir_path, "pseudo.json")

def export_pseudo(pseudo):

    pseudo_df = pandas.read_json(pseudo)

    for column, rows in pseudo_df.items():

        for index, row in rows.items():
            if row == None or isinstance(row,str) or isinstance (row, bool):                    
                continue
            if index == 'names' :
                for k, r in row.items():
                    if k == "international":
                        username = r
                return username
                






def export_json_games(games):
    


    #Convertir le fichier en dataframe
    games_df = pandas.read_json(games)
    #Créer un dictionnaire
    games_dict = {}

    #Créer une valeur key pour notre dictionnaire
    key = 0

    #Créer une valeur liste pour notre dictionnaire
    new_value=[]

     #Faire une boucle qui parcoure le df de games
    for column, rows in games_df.items():
        

        #Itérer à travers le json au format dataframe
        for index, row in rows.items():
            if row == None or isinstance(row,str) or isinstance (row, bool):
                continue
            #Afficher le tableau avec un tri plus clair
            #pprint(f"{key} : {row}")

            #Trouver le nom du jeu vidéo et le mettre dans une variable
            if index == "names":
                for k, r in row.items():
                    if k == "international":
                        game_name = r

            #Trouver sa date de sortie et la mettre dans une variable
            if index == "released":
                release_date = row
            #Itérer la valeur key
                key = key + 1
                #Concaténer nos deux valeurs en une variable                 
                new_value = [game_name, release_date]
                #Mettre ces données dans le dictionnaire des catégories
                games_dict.update({str(key):new_value})
        return games_dict



def export_json_categories(categories):
    
    #Convertir categories en dataframe
    categories_df = pandas.read_json(categories)

    #Créer un dictionnaire 
    categories_dict = {}

    #Créer une valeur key pour notre dictionnaire
    key = 0

    #Créer une valeur liste pour notre dictionnaire
    new_value=[]
    #Faire une boucle qui parcoure le df de categories
    for column, rows in categories_df.items():
            print(type(rows))
            print(type(column))
            for row in rows:
                if row == None or isinstance(row,str) or isinstance (row, bool):
                    continue
                #pprint(row)
                #Chercher le nom et l'id des catégories
                category_name = (row['name'])
                category_id = (row['id'])
                #Itérer la valeur key
                key = key + 1
                #Concaténer nos deux valeurs en une variable                 
                new_value = [category_id, category_name]
                #Mettre ces données dans le dictionnaire des catégories
                categories_dict.update({str(key):new_value})
    return categories_dict

    

def export_json_leaderboard(leaderboard):
        
     #Convertir categories en dataframe
    leaderboard_df = pandas.read_json(leaderboard)

    #Créer un dictionnaire 
    leaderboard_dict = {}

    #Créer une valeur key pour notre dictionnaire
    key = 0

    #Créer une valeur liste pour notre dictionnaire
    new_value=[]

    #Faire une boucle qui parcoure l'API
    for column, rows in leaderboard_df.items():
    
        for row in rows:
            if row == None or isinstance(row,str) or isinstance (row, bool):                    
                continue

            for data in row : 
                if not "run" in data:
                    continue
            
                #pprint(data)
                #Affiche les id de chaque joueur
                leaderboard_id = (data['run']['players'][0]['id'])
                #Affiche le positionnement de chaque joueur
                leaderboard_place = (data ['place'])
                #Itérer la valeur key
                key = key + 1
                #Concaténer nos deux valeurs en une variable                 
                new_value = [leaderboard_id, leaderboard_place]
                #Mettre ces données dans le dictionnaire des catégories
                leaderboard_dict.update({str(key):new_value})

    return leaderboard_dict
                

                    

  
#export_json_games(games)
#export_json_categories(categories)
#export_json_leaderboard(leaderboard)
#export_pseudo(pseudo)
