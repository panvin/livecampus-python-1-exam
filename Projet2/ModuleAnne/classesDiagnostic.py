import os
import platform
import psutil
import datetime

#Cette classe extraie des données spécifiques d'informations systèmes et les retourne sous forme de dictionnaire
class Diagnostic:

    def create_diagnostic():
        #-----------------RECUPERER LE NOM DE L'OS-----------------
        #Stocker les infos sur l'os dans une variable
        os_infos = platform.uname()
        
        #Stocker le nom de l'os
        name_os = (os_infos[0])
        #Stocker la relase de l'os
        release_os =(os_infos[2])

        #Concaténer le tout dans une liste
        os_list = []
        os_list = [f"{name_os} {release_os}"]
        
        #-----------------CPU-----------------

        #Stocker le nom du ou des processeurs
        cpu_name = platform.processor()
        
        #Stocker le pourcentage d'utilisation
        cpu_percentage = psutil.cpu_percent(interval=3)

        #Concaténer le tout dans une liste
        cpu_list = []
        cpu_list = [f"{cpu_name} : {cpu_percentage}"]


        #-----------------RAM-----------------
        #Stocker les infos sur la mémoire dans une variable
        memory = psutil.virtual_memory()

        #Stocker le pourcentage d'utilisation de la mémoire
        memory_percentage = memory[2]

        #Concaténer le tout dans une liste
        memory_list = []
        memory_list = [f"{memory} : {memory_percentage}"]

        # -----------------5 PROCESSUS LES PLUS EXIGEANTS EN TERME DE CONSOMMATION-----------------
        
        #Créer un dictionnaire de processus
        processes_dict={}

        for proc in psutil.process_iter(['name', 'memory_percent']):
            process_name = (proc.info['name'])
            process_memory_percent = (proc.info['memory_percent'])
            
            #Concaténer nos deux valeurs en une variable                 
            process_name, process_memory_percent

            #Mettre ces données dans le dictionnaire des catégories
            processes_dict.update({process_name:process_memory_percent})
            #Classer le dictionnaire par ordre croissant
            sorted_dict = sorted(processes_dict.items(), key=lambda x:x[1], reverse = True)
            converted_dict = dict(sorted_dict)
        
        #Créer une liste
        processes_list = []
        
        i = 0
        for k, value in converted_dict.items():
            i = i + 1
            #Concaténer les valeurs dans la liste
            processes_list.append([f"{k} : {value}"])
            if i  == 5:
                break
    
        
        # -----------------LES VARIABLES D'ENVIRONNEMENT-----------------
        #Créer une liste et y mettre les variables d'environnement
        env_variables = []
        env_variables = list(os.environ.items())


        #-----------------PARTITION DES DISQUES-----------------

        partitions = psutil.disk_partitions()
        #Créer nos listes
        disk_list = []
        free_space_list = []
        #Parcourir les différentes partitions
        for data in partitions:
            device = data[0]
            filesystem = data[2]
            #Mettre les données dans les listes
            disk_list.append(device)
            disk_list.append(filesystem)
            
            #-----------------ESPACE RESTANT SUR LES DISQUES-----------------
            #Ici le TRY EXCEPT est inscrit au cas où des disques n'auraient pas les permissions appropriées, comme les lecteurs DVD
            try:
                disk_space = psutil.disk_usage(device)
            except:
                continue

            free_space = disk_space[2]
            #Arrondir le nombre de bytes restant sur le disque et le convertir en GB
            free_space_rounded = (round((free_space / (1024 * 1024 *1024))))
            #L'ajouter à la liste
            free_space_list.append(f"{free_space_rounded} GB")

    

        #-----------------NOM DES INTERFACES RESEAUX-----------------
        #Créer la liste
        interfaces_total = psutil.net_if_addrs()
        interfaces_list = []

        for data in interfaces_total:
            #Ajouter les données dans la liste
            interfaces_list.append(data)

        

        #-----------------BOOT TIME AU FORMAT HEURES:MINUTES:SECONDES-----------------
        #Créer la liste et ajouter les données
        boot_time = psutil.boot_time()
        list_boot_time = []
        list_boot_time.append(datetime.datetime.fromtimestamp(boot_time).strftime("%H:%M:%S"))
        

        
        #CREATION DU DICTIONNAIRE

        diagnostic_dict = {"OS": os_list, "CPU" : cpu_list, "RAM" : memory_list, "Les 5 processus qui consomment le plus de RAM " : processes_list, "Les variables d'environnements" : env_variables, "Partitions de disque" : disk_list, "Espace restant sur les disques" : free_space_list, "Interfaces réseaux" : interfaces_list, "Heures écoulées depuis le dernier démarrage" : list_boot_time }

        return diagnostic_dict