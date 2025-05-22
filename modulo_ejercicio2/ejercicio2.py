# Crea un script en Python que, haga lo siguiente:
# • Tome una palabra clave de búsqueda (puede ser una variable palabra = "laptop").
# • Ingrese a la tienda virtual (Puede ser Mercado libre o Amazon)
# • Extraiga los títulos y precios de los primeros 5 productos que coincidan.
# • Permite cambiar la palabra clave fácilmente.

# ACLARACION: se puede hacer con python puro usando urllib y htmlparser pero no es lo mas recomendable para las practicas
# asi que me ire por usar librerias especiales de python como lo son requests y bs4 para el scraping

import requests
from bs4 import BeautifulSoup

#creamos una variable para realizar la busqueda 
palabra = "playstation5"

# usaremos mercadolibre para realizar la busqueda y le haremos el scraping
url = f"https://listado.mercadolibre.com.co/{palabra}"

#enviar solicitud http
response = requests.get(url)

#validamos la respuesta de la solicitud http si no es 200 lanzamos una exception 
if response.status_code != 200:
    raise Exception(f"Error al hacer la solicitud: {response.status_code}")

#analizamos el html de la pagina 
soup = BeautifulSoup(response.text, "html.parser")

#buscamos el contenedor donde se encuentran los productos y lo limitamos a 5
productos = soup.find_all("li", class_="ui-search-layout__item", limit=5)

#vamos a mostrar los resultados
print(f"\nResultados para: '{palabra}'\n")

contador=0
for articulo in productos:
    titulo_articulo = articulo.find("a", class_="poly-component__title")
    precio_articulo = articulo.find("span", class_="andes-money-amount__fraction")
    
    titulo = titulo_articulo.get_text(strip=True) 
    precio = precio_articulo.get_text(strip=True)
    
    contador=contador+1
    print(f"{contador}. {titulo} ---- ${precio}")

    