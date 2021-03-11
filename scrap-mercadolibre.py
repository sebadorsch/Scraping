from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.mercadolibre.com.ar/ofertas?price=0.0-2000.0&page=3"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pr = soup.find_all('span', class_='promotion-item__price')
precios = list()

print(pr)

cantidad_productos = 0
sumatoria_precios = 0
for i in pr:
    precios.append( i.text[2:len(i.text)].replace(".","") )
    sumatoria_precios += round(float(float(precios[0])),2)
    cantidad_productos += 1
    


print(precios)
print("Cantidad de productos:", cantidad_productos)
print("Promedio de precios:", sumatoria_precios / cantidad_productos)