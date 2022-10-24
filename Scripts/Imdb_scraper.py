import string
import requests
from bs4 import BeautifulSoup
import openpyxl
excel= openpyxl.Workbook()

sheet = excel.active 
sheet.title = 'Top Rated Movies' 


sheet.append(['Rank','Movie Name','Year of Release','IMDB Rating'])

url="https://www.imdb.com/chart/top/"

try:
    html= requests.get(url)
    soup= BeautifulSoup(html.content, 'html.parser')

    movies = soup.find('tbody', class_='lister-list').find_all('tr')
    for movie in movies:
        Name=       movie.find('td',class_="titleColumn").a.text
        rank=       movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        year=       movie.find('td',class_="titleColumn").span.text.strip('()')
        rating=     movie.find('td', class_='ratingColumn').get_text(strip=True)
        print(rank, Name, year,rating)
        sheet.append([rank, Name, year,rating])
        
        
        
       
except Exception as e:
    print(e)
excel.save('Imdb Top 250 Movies by Ratings.xlsx')

