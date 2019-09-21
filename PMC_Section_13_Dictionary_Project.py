import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead?  y or n  " % get_close_matches(word, data.keys())[0])
        if yn == "y":
             return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
             return "Exit Program"
        else:
             return "Incorrect Input - Exit Program" 
    else:
        return "The word does not exist in the database."

theInput = input("Enter Word: ")
#print(translate(theInput))
output = translate(theInput)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

