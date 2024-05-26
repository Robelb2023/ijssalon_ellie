from helper import decoreer, fooi_pp, onderstreep, som
from presentatie import presenteer
import csv

inkomsten = {
    "Aardbeien-ijs-totaal"  :  "1000",
    "Vanille-ijs-totaal"    :  "2000",
    "Chocolade-ijs-totaal"  :  "1500",
    "Waterijsjes-totaal"    :  "750"
}

# Bereken de totale som van inkomsten met behulp van de som-functie
totaal_inkomsten = som(inkomsten)

# Print het resultaat
print(f"De totale inkomsten zijn: {totaal_inkomsten}")

with open ('boekhouding.csv' , 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])
    
print("Gegevens zijn naar boekhouding.csv geschreven.")