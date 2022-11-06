def ProcessInput(inputString):
    validInput=['film-tv','history','sport','music']
    if inputString in validInput:
        return inputString
    else:
        print("Incorrect Input, please try again.")
    
