import pandas
from pprint import pprint 
from operator import itemgetter

class Error_Report():

    def Extract_error():
    
        
        content = ""

        rows = (content['hits']['hits'])
        liste_pleine = []
        for line in rows:
            if line['_source']['log']['level'] == "error" or line['_source']['log']['level'] == "warning":
                list_vide = [line['_source']['host']['name'], line['_source']['log']['level'], line['_source']['message']]
                if list_vide :
                    liste_pleine.append(list_vide)
        
        #pprint(sorted(liste_pleine, key=itemgetter(1)))
        return(sorted(liste_pleine, key=itemgetter(1)))