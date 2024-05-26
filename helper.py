def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()

def fooi_pp(bedrag, personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"
 
def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit

def som(d):
    """
    Accepteert een dictionary als invoer en retourneert de som van alle waarden.
    
    Args:
        d (dict): De invoer-dictionary.
    
    Returns:
        float: De som van alle waarden in de dictionary.
    """
    # Converteer de waarden naar numerieke waarden (integers)
    numerieke_waarden = [int(waarde) for waarde in d.values()]
    return sum(numerieke_waarden)
        
    return sum(d.values())

# Voorbeeld gebruik
mijn_dictionary = {"a": 10, "b": 20, "c": 30}
resultaat = som(mijn_dictionary)
print(f"De som van de waarden in de dictionary is: {resultaat}")
