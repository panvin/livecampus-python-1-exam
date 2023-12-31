#########################################################################################
#                      Projet 2 Examen Semaine Python Livecampus                        #
#               Anne Cadeillan  -  Cédric Artaud  -  Vincent PANOUILLERES               #
#########################################################################################

# Projet Github: https://github.com/panvin/livecampus-python-1-exam

from ModuleVincent.file_utils import FileUtils
from ModuleCedric.log_report import Log_Report
from ModuleAnne.classesDiagnostic import Diagnostic
from pprint import pprint
import pathlib
import os

def main():
    
    # Définition des path utilisés dans le projet
    rootFile = pathlib.Path(__file__).parent.resolve()
    json_filename = "ntt.json"
    json_path = os.path.join(rootFile, json_filename)
    xlsx_filename = "projet2.xlsx"
    xlsx_path = os.path.join(rootFile, xlsx_filename)

    file_utils = FileUtils()

    #Copie du fichier json
    if os.path.isfile(json_path):
        file_utils.simple_copy_file(json_path)
    

        #Extraction des données du fichier json en passant le path
        report_utils = Log_Report()
        logs_list = report_utils.extract_logs(json_path)

        # Adaptation du format de données pour l'export xlsx
        logs_dict = { "log level": [i[1] for i in logs_list],
                    "message"  : [i[2] for i in logs_list],
                    }

    else:
        print(f"Le fichier json {json_path} n'existe pas")
        logs_dict = { "log level": [""],
                    "message"  : [""],
                    }

    infos_dict= Diagnostic().create_diagnostic()

    # Adaptation du format de données pour l'export xlsx, il faut qu'on ait le même nombre de lignes dans chaques listes
    max_array = len(infos_dict["Les variables d'environnements"])
    for key, rows in infos_dict.items():
        while len(rows)< max_array:
            rows.append("")
 
    # Export des données
    file_utils.export_as_xlsx(xlsx_path, logs_dict, infos_dict)

if __name__ == "__main__":
    main()