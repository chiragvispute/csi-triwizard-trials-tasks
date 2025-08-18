import requests
from bs4 import BeautifulSoup

url = "https://harrypotter.fandom.com/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#  TODO 1: Get all <a> tags
#  TODO 2: Print the href of each <a>
