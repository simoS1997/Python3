import requests
from bs4 import BeautifulSoup

def aplicacio_5():
    print("Aplicació 5 seleccionada.")

    # URL de la pàgina web per fer scraping
    url = "https://www.wikipedia.org"

    # Fer la petició HTTP GET a la pàgina web
    response = requests.get(url)

    # Verificar que la petició s'ha realitzat amb èxit
    if response.status_code == 200:
        # Obtenir el contingut HTML de la pàgina
        html_content = response.text

        # Crear un objecte BeautifulSoup per analitzar el contingut HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Exemple: Extreure el títol de la pàgina
        title = soup.find("title").text
        print("Títol de la pàgina:", title)

        # Exemple: Extreure tots els enllaços de la pàgina
        links = soup.find_all("a")
        print("Enllaços de la pàgina:")
        for link in links:
            print(link["href"])

    else:
        print("No s'ha pogut accedir a la pàgina.")


# Programa principal
aplicacio_5()