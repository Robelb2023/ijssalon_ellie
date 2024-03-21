from helper import decoreer

def print_aanbieding():
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }
    aanbieding = {"vanille": 4}
    aanbieding["vanille"] *= 0.8  
    #print(aanbieding)

    reclame_tekst3 = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding['vanille']:.2f} .")
    #print(reclame_tekst3.upper())

    reclame_tekst4 = reclame_tekst3.split()
    #print(reclame_tekst4)

    el = reclame_tekst4

    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el.upper())
        else:
            print(el.lower())

decoreer("aanbieding")
print_aanbieding()