import requests
from bs4 import BeautifulSoup


# main driver of the program
def run(args):
    option = process_input(str(args[1]))
    if option == 0:
        return 'Please use one of the following options: film-tv, history, sport, music'

    dom = connect(option)
    if dom == 0:
        return 'Error in getting URL'

    li = get_events(dom)
    if li == 0:
        return 'Error getting data from page'

    return show(li)


# processes the input given on the commandline
def process_input(inputString):
    validInput=['film-tv','history','sport','music']
    if inputString in validInput:
        return inputString
    else:
        print("Incorrect Input, please try again.")
        return 0


# connects to the respective URL
def connect(option):
    if process_input(option) != 0:
        URL = "https://www.onthisday.com/" + option +"/"
        page= requests.get(URL)

        soup= BeautifulSoup(page.content, "html.parser")

        return soup
    else:
        return 0


# gets the events from the page
def get_events(soup):
    if isinstance(soup, BeautifulSoup):
        my_data = []
        events= soup.select('li.event')

        for event in events:
            my_data.append(event.get_text())

        return my_data
    else:
        return 0
    

# displays the data to the user
def show(my_data):
    if type(my_data) is not list:
        return 0

    return_string = ''
    for data in my_data:
        return_string += str(data) + '\n'
    return return_string[:-1]
    