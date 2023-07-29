import os
import platform
import psutil
from pprint import pprint

"""
# Modèle de donnée pour Anne
    infos_dict = {
        "OS" : ["Windows 10 Pro"],
        "CPU": ["Infos cpu"],
        "RAM": ["Infos Ram"],
    }
"""

def diagnostic():

    #-----------------RECUPERER LE NOM DE L'OS-----------------
     #Stocker les infos sur l'os dans une variable
    os_infos = platform.uname()
    
    #Stocker le nom de l'os
    name_os = (os_infos[0])
    #Stocker la relase de l'os
    release_os =(os_infos[2])

    #-----------------CPU-----------------

    #Stocker le nom du ou des processeurs
    cpu_name = platform.processor()
    
    #Stocker le pourcentage d'utilisation
    cpu_percentage = psutil.cpu_percent(interval=3)


    #-----------------RAM-----------------
    #Stocker les infos sur la mémoire dans une variable
    memory = psutil.virtual_memory()

    #Stocker le pourcentage d'utilisation de la mémoire
    memory_percentage = memory[2]


    # -----------------5 PROCESSUS LES PLUS EXIGEANTS EN TERME DE CONSOMMATION-----------------
    
    #Créer un dictionnaire
    processes_dict={}

    for proc in psutil.process_iter(['name', 'memory_percent']):
        process_name = (proc.info['name'])
        process_memory_percent = (proc.info['memory_percent'])
        
        #Concaténer nos deux valeurs en une variable                 
        process_name, process_memory_percent

        #Mettre ces données dans le dictionnaire des catégories
        processes_dict.update({process_name:process_memory_percent})
        sorted_dict = sorted(processes_dict.items(), key=lambda x:x[1], reverse = True)
        converted_dict = dict(sorted_dict)
    
    i = 0
    for k, value in converted_dict.items():
        i = i + 1
        print(k)
        print(value)
        if i  == 5:
            break
            




diagnostic()