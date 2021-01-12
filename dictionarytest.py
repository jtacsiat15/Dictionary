import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def getDefinition(wantedWord):
    if wantedWord in data:
        return data[wantedWord]
    elif len(get_close_matches(wantedWord, data.keys())) > 0:
        userChoice = input("Did you mean %s instead? Enter y if yes or n if no: " % get_close_matches(wantedWord, data.keys())[0])
        if userChoice == "y" :
            return data[get_close_matches(wantedWord, data.keys())[0]]
        elif userChoice == "n" :
            return "Word does not exist please try again"
        else:
            return "We did not understand your entrance"
    else:
        return "word does not exist please try again"

while True:
    userInput = input("Enter a word you want the definition of: ")

    if(userInput == 'q'):
        break
    else:
        output = getDefinition(userInput.lower())
        if type(output) == list:
            for item in output:
                print(item) 
        else:
            print(output)
    