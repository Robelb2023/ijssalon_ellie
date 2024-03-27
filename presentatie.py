# Maak een functie genaamd 'presenteer'
def presenteer(dictionary, totaal):
    # Print elk sleutel-waardepaar in de dictionary
    for key, value in dictionary.items():
        print(f"{key} : {value} euro")
    
    # Print een scheidingslijn
    print("==========================")
    
    # Print het totaal
    print(f"Totaal : {totaal} euro")