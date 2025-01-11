from scrapper import LeksykonScrapper #import klasy LeksykonScrapper z pliku scrapper
import csv

leksykon = LeksykonScrapper() #obiekt klasy LeksykonScrapper
leksykon.scrape() #wywołanie metody scarpe


with open("norms.csv", mode="w", encoding="utf-8") as file:
    file.write("name;kind;units;norm\n")

    for test_norm in leksykon.test_norms:
       file.write(f"{test_norm.to_csv()}\n")
