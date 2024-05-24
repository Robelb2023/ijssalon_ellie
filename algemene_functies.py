def mijn_functie_1(argument):
    # Bereken de teruggeefwaarde op basis van de gegeven tabel
    return argument ** 2

#Test de functie met de voorbeelden uit de tabel
print(mijn_functie_1(2)) # moet 4 retourneren
print(mijn_functie_1(4)) # moet 16 retourneren
print(mijn_functie_1(10)) # moet 100 retourneren
print(mijn_functie_1(12)) # moet 144 retourneren

def mijn_functie_2(argument):
    # Bereken de teruggeefwaarde op basis van de gegeven tabel
    return [argument + 3, argument - 3, argument * 3, argument / 3]

#Test de functie met de voorbeelden uit de tabel
print(mijn_functie_2(12.3))  # moet [15, 9, 36, 4]    retourneren
print(mijn_functie_2(12.2))  # moet [14, 10, 24, 6]   retourneren
print(mijn_functie_2(10.5))  # moet [15, 5, 50,2]     retourneren
print(mijn_functie_2(100.20)) # moet [120,80,2000,5]  retourneren