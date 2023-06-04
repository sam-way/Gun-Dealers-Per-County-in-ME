import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_municipalities_in_Maine'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})
df = pd.read_html(str(table))[0]

df['Municipality'] = df['Municipality'].str.strip()

df = df[['Municipality', 'County']]
df.columns = ['Town', 'County']

df.to_csv('maine_towns_counties.csv', index=False)