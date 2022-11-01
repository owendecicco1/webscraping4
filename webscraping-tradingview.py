from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url =  "https://www.webull.com/quote/us/gainers"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

title  = soup.title

print(title.text)



#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

tablecells = soup.findAll("div", attrs = {"class": "table-cell"})

print(tablecells[0].text)
#will print out a list
#Number 1 is the actual text

print(tablecells[0].text)
print(tablecells[1].text)
print(tablecells[3].text)
print(tablecells[5].text)
print(tablecells[6].text)

print("Percentage Change: ",tablecells[3].text)
print("High: ",tablecells[5].text)
print("Low: ",tablecells[6].text)

name = 1
high = 5
low = 6

count = 1

while count <= 5:
    calc = ((float(tablecells[high].text) - float(tablecells[low].text)) / float(tablecells[low].text)) * 100
    print(f'* Name: {tablecells[name].text} || High: {tablecells[high].text} || Low: {tablecells[low].text}')
    print(calc)
    name += 11
    high += 11
    low += 11
    count += 11


