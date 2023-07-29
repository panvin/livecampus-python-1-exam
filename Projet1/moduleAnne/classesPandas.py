import pandas 



class JsonToDictionnary :
        

    def export_pseudo(self, pseudo):
        #Convertir le fichier en dataframe
        pseudo_df = pandas.read_json(pseudo)

        #Parcourir le fichier
        for column, rows in pseudo_df.items():

            for index, row in rows.items():
                if row == None or isinstance(row,str) or isinstance (row, bool):                    
                    continue
                #Trouver le nom de l'user et le mettre dans une variable
                if index == 'names' :
                    for k, r in row.items():
                        if k == "international":
                            username = r
                    return username
                    


    def export_json_games(self, games):
        
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


    def export_json_categories(self, categories):
        
        
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

                for row in rows:
                    if row == None or isinstance(row,str) or isinstance (row, bool):
                        continue
                    
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

        

    def export_json_leaderboard(self, leaderboard):
            
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
                    #Variable qui contient le statut du joueur : guest ou user
                    rel = (data['run']['players'][0]['rel'])
                    #Si le.la joueur.se est un.e user, on cherche son id dans le dataframe
                    if rel == "user":
                        leaderboard_id = (data['run']['players'][0]['id'])
                    
                    #Si le.la joueur.se est un.e guest, on cherche son name dans le dataframe
                    elif rel == "guest":
                        guest_name = (data['run']['players'][0]['name'])
                        leaderboard_id = (f"guest = {guest_name}")

                    #Temps du joueur /de la joueuse    
                    leaderboard_realtime =(data['run']['times']['realtime'])
                    #Affiche le positionnement de chaque joueur
                    leaderboard_place = (data ['place'])
                    #Itérer la valeur key
                    key = key + 1
                    #Concaténer nos deux valeurs en une variable                 
                    new_value = [leaderboard_id, leaderboard_realtime, leaderboard_place]
                    #Mettre ces données dans le dictionnaire des catégories
                    leaderboard_dict.update({str(key):new_value})

        return leaderboard_dict
                

        