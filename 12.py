import os

# Crear el directori Prova dins de /home/cicles/AO
ruta_directorio = "/home/cicles/AO/Prova"
os.makedirs(ruta_directorio, exist_ok=True)

# Canviar al directori Prova
os.chdir(ruta_directorio)

# Crear l'arxiu Ex12.txt i escriurte els noms dels companys de clase
companeros = ['Adrià', 'Aroa', 'Sebas', 'Eric', 'Sergi Pons', 'Sergio Bolívar', 'Sergi Martín', 'Oscar', 'Dani', 'Ainhoa', 'Aram', 'Jade', 'Isaac']
with open("Ex12.txt", "w") as f:
    for nombre in companeros:
        f.write(nombre + '\n')

# Obrir l'arxiu en mode "append" i afegir els noms dels professors.
profesores = ['Profesor1', 'Profesor2', 'Profesor3']
with open("Ex12.txt", "a") as f:
    for nombre in profesores:
        f.write(nombre + '\n')

# Obrir l'arxiu en mode lectura i guardar elcontingut dins una llista de nombres
nombres = []
with open("Ex12.txt", "r") as f:
    for linea in f:
        nombres.append(linea.strip())

# Imprimira la llista de nombres
print(nombres)
