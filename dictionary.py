import json

# TODO: unittesting

dictionary = json.load(open("data.json"))

def get_definitions(word):
    word = word.lower().strip()
    # TODO: regex to make it just letters?
    if word in dictionary:
        return dictionary[word]
    else:
        return ["Sorry, that doesn't appear to be a word. Double check it and try again."]

def display_definitions(definitions):
    for defn in definitions:
        print(defn)

def display_welcome():
    print("Welcome to this very useful dictionary.")
    print("Please enter a word or term to get started...")

def get_input():
    return input("> ")

def similar_words(word):
    pass

if __name__ == "__main__":
    display_welcome()
    while True:
        word = get_input()
        display_definitions(get_definitions(word))
