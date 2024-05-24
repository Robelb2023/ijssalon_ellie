from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    # Bereken nieuwe prijs na korting
    nieuwe_prijs = prijs * (1 - korting)
    # Genereer de aanbiedingstekst
    aanbieding = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro. "

    #Retourneer de aanbiedingstekst
    return aanbieding

#Test de functie met de opgegeven argumenten
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    # Bereken het totaal van de inkomsten
    totaal = sum(inkomsten)

    # Retourneer het totaal
    return totaal

# Test de functie met de opgegeven argumenten
inkomsten_per_dag = [220,430, 125, 160, 205, 90, 345]
print(f"Totaal van de inkomsten per dag: {inkomsten_totaal(inkomsten_per_dag)}")
      
def inkomsten_totaal(inkomsten, btw):
   #Bereken het totaal van de inkomsten
    totaal = sum(inkomsten)
   #Bereken het btw bedrag
    btw_bedrag = totaal * btw
   #Genereer de gewenste uitvoertekst
    uitvoer=f"Het totaal van alle inkomsten van deze week is {totaal:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."
   #Retourneer de uitvoertekst
    return uitvoer

#Test de functie met de opgegeven argumenten
inkomsten_per_dag=[220, 430, 125, 160, 205, 90, 345]
btw_percentage = 0.09
print(inkomsten_totaal(inkomsten_per_dag, btw_percentage))

def laag_en_hoog(mijn_lijst):
   #Bereken de hoogste en laagste waarde in de lijst
    hoogste=max(mijn_lijst)
    laagste=min(mijn_lijst)

   #Retourneer een lijst met de hoogste en laagste waarde
    return[hoogste, laagste]

#Test de functie met de opgegeven argumenten
inkomsten_per_dag= [220, 430, 125, 160, 205, 90, 345]
print(f"Hoogste en laagste inkomsten: {laag_en_hoog(inkomsten_per_dag)}")

def gemiddelde(mijn_lijst):
   #Bereken het gemiddelde van de waarden in de lijst
    gemiddelde=sum(mijn_lijst) / len(mijn_lijst)

   #Retourneer het gemiddelde
    return gemiddelde

#Test de functie met de opgegeven argumenten
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
print(f"Gemiddelde inkomsten per dag: {gemiddelde(inkomsten_per_dag):.2f}")

def gemiddelde(mijn_lijst):
   #Bereken het gemiddelde van de waarden in de lijst 
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)

   #Genereer de gewenste uitvoertekst
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro."

   #Retourneer de uitvoertekst
    return uitvoer

#Test de functie met de opgegeven argumenten
inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
print(gemiddelde(inkomsten_per_dag))

def hoog_en_laag(mijn_lijst):
   #Bereken de hoogste en laagste waarde in de lijst 
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)

   #Retourneer een lijst met de hoogste en laagste waarde
    return[hoogste, laagste]

def meervoudig(invoer_lijst):
   #Roep de functie hoog_en_laag aan met de opgegeven invoerlijst 
    return hoog_en_laag(invoer_lijst)

#Test de functie met de opgegeven argumenten
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
print(f"Hoogste en Laagste waarden:{meervoudig(invoer_lijst)}")

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = invoer_lijst(korte_lijst[0], korte_lijst[1])
    return uitvoer

