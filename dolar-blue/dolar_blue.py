import requests
from bs4 import BeautifulSoup

page= requests.get("https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB")
soup = BeautifulSoup(page.text, 'html.parser')

boxcompra = soup.find('div', class_='buy-value').get_text(strip =True, separator=' ')
boxventa = soup.find('div', class_='sell-value').get_text(strip =True, separator=' ')


print("DOLAR BLUE EL CRONISTA")
print(f'El precio de compra es :{boxcompra}')
print(f'El precio de venta es :{boxventa}')
#print(precio_compra)

page2= requests.get("https://www.ambito.com/contenidos/dolar-informal.html")
soup2 = BeautifulSoup(page2.text, 'html.parser')

#boxcompra2 = soup2.find('span', class_='value data-compra').get_text(strip =True, separator=' ')
#boxventa2 = soup2.find_all('div', class_='first')
#print(boxventa2)
