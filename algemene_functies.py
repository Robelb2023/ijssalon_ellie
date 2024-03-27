def mijn_functie_2(argument):
    # Definieer een woordenboek om argumenten te koppelen aan hun bijbehorende teruggeefwaarden
    argument_naar_teruggeefwaarde = {
        12.3: [15, 9, 36, 4],
        12.2: [14, 10, 24, 6],
        10.5: [15, 5, 50, 2],
        100.20: [120, 80, 2000, 5]
    }
    
    if argument in argument_naar_teruggeefwaarde:
        return argument_naar_teruggeefwaarde[argument]
    else:
        return None

if __name__ == "__main__":
    arg = 100.20
    resultaat = mijn_functie_2(arg)
    if resultaat:
        print(f"Voor argument {arg} is de teruggeefwaarde {resultaat}")
    else:
        print(f"Geen overeenkomstige teruggeefwaarde gevonden voor argument {arg}")