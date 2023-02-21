import string
import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/series/csa-t20-challenge-2022-23-1334878/titans-vs-dolphins-final-1334921/live-cricket-score"

html = requests.get(url)

soup = BeautifulSoup(html.content, 'html.parser')

team1=soup.find('span', class_='ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate !ds-text-ui-typo-mid')

print(team1.text)
team2=soup.find('span', class_='ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate')
print(team2.text)

