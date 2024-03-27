# Importeer alle functies en variabelen uit helper.py
from helper import decoreer, fooi_pp, onderstreep 
from presentatie import presenteer
import csv

# Maak een dictionary genaamd 'inkomsten'
inkomsten = {
    'Aardbeien-ijs-totaal': 1000,
    'Vanille-ijs-totaal': 2000,
    'Chocolade-ijs-totaal': 1500,
    'Waterijsjes-totaal': 750
}

# Bereken de totale inkomsten door de waarden op te tellen
totaal_inkomsten = sum(inkomsten.values())

# Presenteer de inkomsten op een gestructureerde manier
presenteer(inkomsten, totaal_inkomsten)

# Definieer een functie genaamd 'som'
def som(dictionary):
    # Tel alle waarden in de dictionary op
    return sum(dictionary.values())