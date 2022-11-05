import requests
from bs4 import BeautifulSoup

URL = "https://www.onthisday.com/"
page= requests.get(URL)

soup= BeautifulSoup(page.content, "html.parser")

