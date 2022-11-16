from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv

webpage = 'https://www.cryptocurrencychart.com/' 

page = urlopen(webpage).read()		

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

#print(title.text)

table_rows = soup.findAll("tr")
for x in range(1,6):
    td = table_rows[x].findAll("td")
    coin_name = td[1].text
    current_price = float((td[2].text.replace(",","").replace("$","")))
    percent_change_in_last_24_hours = float(td[4].text.replace("%","").replace("+","").replace("-",""))
    corresponding_price_based_on_change =((current_price/percent_change_in_last_24_hours) + 1)

    print(f"Coin: {coin_name}")
    print(f"Price: ${current_price:,.2f}")
    print(f"Percent change in last 24 hours: {percent_change_in_last_24_hours}%")
    print(f"Price based on percent change: {corresponding_price_based_on_change}")
    print()
    print()

import keys2
from twilio.rest import Client

client = Client(keys2.accountSSID,keys2.authToken)

TwilioNUMBER = "+18507808632"

myCellPhone = "+12015270829"

textmessage1 = client.messages.create(to = myCellPhone,from_= TwilioNUMBER,body = "ETH has fallen below $3,000!")
textmessage2 = client.messages.create(to = myCellPhone,from_= TwilioNUMBER, body = "BTC has fallen below $40,000!")

if coin_name == "Ethereum" and current_price > 3000:
    print(textmessage1.status)
if coin_name == "Bitcoin" and current_price > 40000:
     print(textmessage2.status)


