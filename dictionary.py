import json
from difflib import get_close_matches

# TODO: unittesting

dictionary = json.load(open("data.json"))

def get_definitions(word):
    word = word.lower().strip()
    # TODO: regex to make it just letters?
    # TODO: Clean up?
    return_val = []
    if word in dictionary:
        return_val.append("- " + word)
        for term in dictionary[word]:
            return_val.append("\t: " + term)
    else:
        close = similar_words(word)
        if len(close) > 0:
            return_val.append("That doesn't appear to be a word. Did you mean:")
            for potential in close:
                return_val.append("- " + potential)
                for term in dictionary[potential]:
                    return_val.append("\t: " + term)
        else:
            return ["Sorry, that doesn't appear to be a word. Double check it and try again."]
    return return_val

def display_definitions(definitions):
    for defn in definitions:
        print(defn)

def display_welcome():
    print("Welcome to this very useful dictionary.")
    print("Please enter a word or term to get started...")

def get_input():
    return input("> ")

def similar_words(word):
    # return SequenceMatcher(None, word, word2).ratio()
    return get_close_matches(word, dictionary.keys())

if __name__ == "__main__":
    display_welcome()
    while True:
        word = get_input()
        display_definitions(get_definitions(word))
