from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

webpage = 'https://www.coingecko.com/' 

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

table_rows = soup.findAll("tr")
for x in range(1,6):
    td = table_rows[x].findAll("td")
    coin_name = td[2].text
    current_price = int(td[3].text.replace(",","").replace("$",""))
    percent_change_in_last_24_hours = int(td[5].text.replace("%",""))
    corresponding_price_based_on_change = 