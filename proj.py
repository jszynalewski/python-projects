import os 
import shutil

folder = input("Wprowadź ścieżkę folderu: ")

kategorie = {
    "Zdjęcia" : [".jpg", ".png", ".gif"],
    "Muzyka" : [".mp3", ".wav", ".wma"],
    "Dokumenty" : [".pdf", ".odt", ".docx"]
    }

for file in os.listdir(folder): #listuje pliki w folderze 
    rozszerzenie = os.path.splitext(file)[1] #pobiera rozszerzenie pliku 
    for key, values in kategorie.items(): 
        if rozszerzenie in values:
            os.makedirs(os.path.join(folder, key), exist_ok=True) #tworzenie folderu i łączenie ściezek
            shutil.move(os.path.join(folder, file), os.path.join(folder, key)) #shuil.move() - przenoszenie plików
            break
    else:
        print(f"Plik {file} nie pasuje do żadnej kategorii")