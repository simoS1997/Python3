def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, 'r') as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print("Fitxer no trobat.")
    except IOError:
        print("Error d'entrada/sortida.")
    except:
        print("Error desconegut en la lectura del fitxer.")

llegir_fitxer("passwd")
