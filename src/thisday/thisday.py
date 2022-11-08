import requests
from bs4 import BeautifulSoup

def connect(option):
    if process_input(option) != 0:
        URL = "https://www.onthisday.com/" + option +"/"
        page= requests.get(URL)

        soup= BeautifulSoup(page.content, "html.parser")

        return soup
    else:
        return 0

def get_events(soup):
    if isinstance(soup, BeautifulSoup):
        my_data = []
        events= soup.select('li.event')

        for event in events:
            my_data.append(event.get_text())

        return my_data
    else:
        return 0
    
def process_input(inputString):
    validInput=['film-tv','history','sport','music']
    if inputString in validInput:
        return inputString
    else:
        print("Incorrect Input, please try again.")
        return 0
