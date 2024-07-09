import csv
import sys
import os

def verifica_estensione(file_path):
    _, estensione = os.path.splitext(file_path)
    return estensione

if len(sys.argv) < 3:
    print("The arguments have to be at least three. \nHINT --> run this command: python ./<app-name>.py ./<file-name>.csv names")
else:
    file_path = sys.argv[1]
    estensione = verifica_estensione(file_path)

    if estensione == ".csv":

        def ricerca_csv(file_csv, nome):
            with open(file_csv, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for riga in reader:
                    if riga['Name'] == nome:
                        return (riga['Name'], riga['City'])
                return (nome, None)
        
        
        names = sys.argv[2:]
            
        ricerca = []

        for i in names:
            risultato = ricerca_csv(sys.argv[1], i)
            ricerca.append(risultato)

        for nome_trovato, eta_trovata in ricerca:
            if nome_trovato and eta_trovata:
                print(f"Name: {nome_trovato}, City: {eta_trovata}")
            else:
                print("Name",nome_trovato,"has not been found in the csv file.")
    else:
        print("The secondo argument must have '.csv' extension in order to be read")