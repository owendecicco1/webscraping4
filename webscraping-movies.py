
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)

'''
table_rows = soup.findAll('tr')

for rec in table_rows[1:6]:
    td = rec.findAll("td")
    Rank = td[0].text
    Movie_Name = td[1].text
    Total_Gross = int(td[7].text.replace("$"," ").replace(",",""))
    Distrubuter = td[9]
    Theaters = int(td[6].text.replace(",",""))
    average_gross = format(int(Total_Gross/Theaters,2))
    print(f"Rank: {Rank}")
    print(f"Movie Name: {Movie_Name}")
    print(f"Total Gross: {Total_Gross}")
    print(f"Distrubuter: {Distrubuter}")
    print(f"Average Gross: {average_gross}")
    print()
    print()
'''
movie_rows = soup.findAll("tr")
for x in range(1,6):
    td = movie_rows[x].findAll("td")
    rank = td[0].text
    movie_name = td[1].text
    theater = int(td[6].text.replace(",",""))
    gross = int(td[7].text.replace(",","").replace("$",""))
    dis = td[9].text

    avg = gross / theater

    print(f"Rank: {rank}")
    print(f"Movie Name: {movie_name}")
    print(f"Total Gross: ${gross:,.2f}")
    print(f"Dirstibutor: {dis}")
    print(f"Average per theater: {avg:,.2f}")
    print()
    print()









    


print(title.text)
##
##
##
##

