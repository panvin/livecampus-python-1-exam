import pandas 
import pathlib
import sys
import os
from pprint import pprint
import json


dir_path = pathlib.Path(__file__).parent
#file_arg = str(sys.argv[1])
games =  os.path.join(dir_path, "games.json")
categories =  os.path.join(dir_path, "categories.json")
leaderboard =  os.path.join(dir_path, "leaderboard.json")


def export_json_games(games):
    


    #Convertir le fichier en dataframe
    games_df = pandas.read_json(games)

    print(games_df)


    dict = {}

  #Faire une boucle qui parcoure le df de games
    for column, rows in games_df.items():
        print(type(rows))
        print(type(column))
        for row in rows:
            if row == None or isinstance(row,str) or isinstance (row, bool):
                continue
            #for data in rows :
                #print(data['abbreviation'])
                #if data['place'] <= nombre_joueurs:
                 #print(data['place'])
            

                #Affiche les id de chaque joueur
                #pprint (data['run']['players'][0]['id'])
                #Affiche le positionnement de chaque joueur
                #pprint (data ['place'])

def export_json_categories(categories):
    
    #Convertir categories en dataframe
    categories_df = pandas.read_json(categories)

    #Créer un dictionnaire 
    categories_dict = {}

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
                #Mettre ces données dans le dictionnaire des catégories
                categories_dict.update({category_name:category_id})

    pprint(categories_dict)
                #for data in row : 
                #    if not "run" in data:
                #        continue
                
                    #if data['place'] <= nombre_joueurs:
                    #print(data['place'])
                

                    #Affiche les id de chaque joueur
                    #pprint (data['run']['players'][0]['id'])
                    #Affiche le positionnement de chaque joueur
                    #pprint (data ['place'])


def export_json_leaderboard(leaderboard):
        
     #Convertir categories en dataframe
    leaderboard_df = pandas.read_json(leaderboard)

    #Créer un dictionnaire 
    leaderboard_dict = {}


    #Faire une boucle qui parcoure l'API
    for column, rows in leaderboard_df.items():
        print(type(rows))
        print(type(column))
        for row in rows:
            if row == None or isinstance(row,str) or isinstance (row, bool):                    
                continue

            for data in row : 
                if not "run" in data:
                    continue
            #Affiche les id de chaque joueur
                pprint(data)
                #Affiche les id de chaque joueur
                pprint (data['run']['players'][0]['id'])
                    #Affiche le positionnement de chaque joueur
                    #pprint (data ['place'])
            #Affiche le positionnement de chaque joueur
           # pprint (row['place'])

            #for data in row : 
             #   if not "run" in data:
              #      continue
               # pprint(data)
                    #if data['place'] <= nombre_joueurs:
                    #print(data['place'])
                

                    

  
#export_json_games(games)
#export_json_categories(categories)
export_json_leaderboard(leaderboard)
