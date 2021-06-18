import csv
import glob

def searchDirectoryForDecks():
    decks = []
    for i in glob.glob(r'*csv'):
        decks.append(i.rstrip(".csv"))
    return decks

def loadDeck(filename):
    deck = []
    filename = filename + ".csv"
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            card = []
            card.append(row[1])
            card.append(row[2])
            deck.append(card)
    return deck


def displayDirectoryDecks(decks):
    counter = 1
    for deck in decks:
        print(str(counter) + ". " + deck.title())
        counter += 1


def chooseDeck(decks):
    while True:
        userChoice = input("\nSelect deck: ")
        # if userChoice.lower() not in decks.items():
        #     print("Requested deck not available. Please check your spelling and try again.")
        #     continue
        # else:
        for deck in decks:
            if deck == userChoice.lower():
                userDeck = loadDeck(userChoice.lower())
                userDeck.pop(0)
                # userDeck.insert(0, userChoice.lower())
                return userDeck
                break


def printDeck(deck):
    print("DECK LIST // " + deck[0].upper())
    print("QUANTITY\t" + "NAME\n")
    for card in deck[1:]:
        print(card[0] + "\t" + card[1])



