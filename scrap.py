from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://argentina.as.com/resultados/futbol/argentina/2018_2019/clasificacion/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Equipos

eq = soup.find_all('span', class_='nombre-equipo')
equipos = list()

contador_equipos = 0

for i in eq:
    if contador_equipos < 26:
        equipos.append(i.text)
    else: 
        break
    contador_equipos +=1

print(equipos)


#Puntos

pt = soup.find_all('td', class_='destacado')
puntos = list()

contador_equipos = 0

for i in pt:
    if contador_equipos < 26:
        puntos.append(i.text)
    else: 
        break
    contador_equipos +=1

print(puntos)


df = pd.DataFrame({'Nombre':equipos, 'Puntos':puntos}, index=list(range(1,27)))
print(df)

df.to_csv('Clasificacion.csv', index=False)
