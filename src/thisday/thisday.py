import requests
from bs4 import BeautifulSoup

def connect(option):
    URL = "https://www.onthisday.com/" + option +"/"
    page= requests.get(URL)

    soup= BeautifulSoup(page.content, "html.parser")

    return soup

def get_events(soup):
    my_data = []
    events= soup.select('li.event')

    for event in events:
        my_data.append(event.get_text())

    return my_data
    
def ProcessInput(inputString):
    validInput=['film-tv','history','sport','music']
    if inputString in validInput:
        return inputString
    else:
        print("Incorrect Input, please try again.")
        return 0
