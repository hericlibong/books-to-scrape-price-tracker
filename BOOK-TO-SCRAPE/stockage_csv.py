# csv_storage.py
import csv
import os

# def save_to_csv(data, filename='cat_books.csv'):
#     file_exists = os.path.isfile(filename)
    
#     with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = list(data.keys())
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
#         if not file_exists:
#             writer.writeheader()
            
#         writer.writerow(data)

def save_to_csv(data, categorie_name):
    #formatage du nom de fichier pour utiliser le nom de la catégorie
    filename = f"{categorie_name.replace('', '_').replace('/', '_')}.csv"
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(data)
