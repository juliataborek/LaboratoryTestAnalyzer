from scrapper import LeksykonScrapper #import klasy LeksykonScrapper z pliku scrapper
import csv

leksykon = LeksykonScrapper() #obiekt klasy LeksykonScrapper
leksykon.scrape() #wywołanie metody scarpe

#Tworzenie pliku CSV z danymi o normach badań krwi.
with open("norms.csv", mode="w", encoding="utf-8") as file: #otwiera plik norms.csv w trybie zapisu
    file.write("name;kind;units;norm\n")#zapis nagłówka kolumn w formacie CSV
    #Iteracja przez wszystkie zebrane normy i zapis ich wierszy do pliku.
    for test_norm in leksykon.test_norms:
        #Dla każdego obiektu klasy TestNorm, które są zapisane w liście,
        #będącej atrybutem obiektu klasy LeksykonScrapper
        #zapisuje ten obiekt w pliku wywołując na nim funkcję to_csv().
       file.write(f"{test_norm.to_csv()}\n")
