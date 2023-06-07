def potencia(n):
    a = []
    for e in range(10):
        a.append(e ** n)
    return a

print(potencia(3))

def prova(n):
    return [x ** n for x in range(10)]

print(prova(3))  

#Resultat:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
