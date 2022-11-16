from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

webpage = 'https://coinmarketcap.com/' 

page = urlopen(webpage).read()		

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

#print(title.text)

table_rows = soup.findAll("tr")

for x in range(1,6):
    td = table_rows[x].findAll("td")
    coin_name = td[2].text
    current_price = float(td[3].text.replace(",","").replace("$",""))
    percent_change_in_last_24_hours = float(td[5].text.replace("%",""))
    corresponding_price_based_on_change = float((current_price/percent_change_in_last_24_hours) + 1)

    print(f"Coin: {coin_name}")
    print(f"Price: {current_price:,.2f}")
    print(f"Percent change in last 24 hours: {percent_change_in_last_24_hours}%")
    print(f"Price based on percent change: {corresponding_price_based_on_change}")
    print()
    print()