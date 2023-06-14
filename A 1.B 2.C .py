import random

def aplicacio_1():
    print("Aplicació 1 seleccionada.")

def treballar_llistes():
    llista = []
    n = int(input("Introdueix la longitud de la llista: "))

    for _ in range(n):
        num = random.randint(1, 100)
        llista.append(num)

    print("Llista generada:", llista)

    suma = sum(llista)
    print("Suma dels elements de la llista:", suma)

    maxim = max(llista)
    print("Valor màxim de la llista:", maxim)

    minim = min(llista)
    print("Valor mínim de la llista:", minim)

    llista_ordenada = sorted(llista)
    print("Llista ordenada:", llista_ordenada)

# Exemple d'ús
treballar_llistes()


def aplicacio_2():
    print("Aplicació 2 seleccionada.")
def treballar_fitxers():
    nom_fitxer = input("Introdueix el nom del fitxer: ")

    while True:
        print("\n1. Crear una nova llista")
        print("2. Afegir un element a la llista")
        print("3. Llegir la llista")
        print("4. Actualitzar un element de la llista")
        print("5. Esborrar un element de la llista")
        print("6. Esborrar la llista")
        print("7. Sortir")

        opcio = input("Introdueix el número de l'opció desitjada: ")

        if opcio == "1":
            llista = []
            print("S'ha creat una nova llista buida.")
            guardar_llista(nom_fitxer, llista)
        elif opcio == "2":
            element = input("Introdueix l'element a afegir: ")
            afegir_element(nom_fitxer, element)
        elif opcio == "3":
            llista = llegir_llista(nom_fitxer)
            print("Llista actual:", llista)
        elif opcio == "4":
            index = int(input("Introdueix l'índex de l'element a actualitzar: "))
            element = input("Introdueix el nou valor: ")
            actualitzar_element(nom_fitxer, index, element)
        elif opcio == "5":
            index = int(input("Introdueix l'índex de l'element a esborrar: "))
            esborrar_element(nom_fitxer, index)
        elif opcio == "6":
            esborrar_llista(nom_fitxer)
            print("S'ha esborrat la llista.")
        elif opcio == "7":
            print("Gràcies per utilitzar el programa. Fins aviat!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")

def guardar_llista(nom_fitxer, llista):
    with open(nom_fitxer, 'w') as fitxer:
        for element in llista:
            fitxer.write(element + '\n')
    print("S'ha guardat la llista al fitxer.")

def afegir_element(nom_fitxer, element):
    with open(nom_fitxer, 'a') as fitxer:
        fitxer.write(element + '\n')
    print("S'ha afegit l'element al fitxer.")

def llegir_llista(nom_fitxer):
    llista = []
    try:
        with open(nom_fitxer, 'r') as fitxer:
            for linia in fitxer:
                llista.append(linia.strip())
    except FileNotFoundError:
        print("El fitxer no existeix.")
    return llista

def actualitzar_element(nom_fitxer, index, element):
    llista = llegir_llista(nom_fitxer)
    if index >= 0 and index < len(llista):
        llista[index] = element
        guardar_llista(nom_fitxer, llista)
        print("S'ha actualitzat l'element.")
    else:
        print("L'índex no és vàlid.")

def esborrar_element(nom_fitxer, index):
    llista = llegir_llista(nom_fitxer)
    if index >= 0 and index < len(llista):
        element = llista.pop(index)
        guardar_llista(nom_fitxer, llista)
        print("S'ha esborrat l'element:", element)
    else:
        print("L'índex no és vàlid.")

def esborrar_llista(nom_fitxer):
    try:
        with open(nom_fitxer, 'w') as fitxer:
            fitxer.write('')
    except FileNotFoundError:
        print("El fitxer no existeix.")


def aplicacio_3():
    print("Aplicació 3 seleccionada.")

    def vocal(a):
        if a == 'a' or a == 'A' or a == 'e' or a == 'E' or a == 'i' or a == 'I' or a == 'o' or a == 'O' or a == 'u' or a == 'U':
            return True
        else:
            return False
    
    a = input("Escriu un caràcter: ")
    print("Si posa *True* és una vocal si posa *False* és una consonant: ", vocal(a))

def aplicacio_4():
    print("Aplicació 4 seleccionada.")

    def sumarllista(a):
        sumatori = 0
        for i in a:
            sumatori += i
        return sumatori

    def llistat_multiplicat(llista):
        resultat = 1
        for x in llista:
            resultat *= x
        return resultat

    x = [1, 2, 3, 4, 5, 6]
    print("El sumatori és: ", sumarllista(x))
    print("El multiplicat és: ", llistat_multiplicat(x))

def programa_principal():
    while True:
        print("Benvingut al programa principal.")
        print("Selecciona una aplicació:")
        print("1. Aplicació 1")
        print("2. Aplicació 2")
        print("3. Aplicació 3")
        print("4. Aplicació 4")
        print("5. Sortir")

        opcio = input("Introdueix el número de l'opció desitjada: ")

        if opcio == "1":
            aplicacio_1()
        elif opcio == "2":
            aplicacio_2()
        elif opcio == "3":
            aplicacio_3()
        elif opcio == "4":
            aplicacio_4()
        elif opcio == "5":
            print("Gràcies per utilitzar el programa. Fins aviat!")
            break
        else:
            print("Opció no vàlida. Si us plau, selecciona una opció vàlida.")

programa_principal()
