def presenteer(totaal, mijn_dict):
     """
     Accepteer een dictionary en de parameter 'totaal' als invoer.
     Presenteerde dictionary-items met hun waarden in euro's 

     """
     for item, waarde in mijn_dict.items():
         print(f"{item} : {waarde} euro")

     print("=" * 26)
     print(f"totaal : { totaal} euro")

# Voorbeeldgebruik:
if __name__ == "__main__":
    mijn_dict = {"vis" : 10, "vlees" : 25, "overig" : 15}
    totaal = 50
    presenteer(totaal, mijn_dict)


   