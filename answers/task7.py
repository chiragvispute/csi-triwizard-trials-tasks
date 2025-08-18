import requests
from bs4 import BeautifulSoup

url = "https://harrypotter.fandom.com/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for a in soup.find_all("a"):
    print(a.get("href"))
