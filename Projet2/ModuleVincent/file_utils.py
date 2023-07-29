import pandas
import shutil
import os

class FileUtils:

    def simple_copy_file(self, path: str) -> None:
        
        filePathNoExt, fileExt = os.path.splitext(path)
        newPath = f'{filePathNoExt}-copy{fileExt}'
        
        try:
            shutil.copyfile(path, newPath)
        except shutil.SameFileError:
            print("Le fichier copié doit être différent du fichier à copier")
        except OSError as error:
            print(f"Une erreur est survenue lors de la copie du fichier: {error}")
        else:
            print("Le fichier a été copié sans incident.")

    def export_as_xlsx(self, path: str, logs_dict: dict, infos_dict: dict) -> None:
        
        try:
            with pandas.ExcelWriter(path) as writer:
                pandas.DataFrame(logs_dict).to_excel(writer, sheet_name='Logs')
                pandas.DataFrame(infos_dict).to_excel(writer, sheet_name='System status')

        except OSError as error:
            print(f"Une erreur est survenue lors de la copie du fichier: {error}")
        except Exception as error:
            print(f"Une erreur est survenue lors de la sauvegarde du fichier .xlsxl: {error}")
        else:
            print(f"La sauvegarde du fichier xlsx s'est déroulé sans problème")