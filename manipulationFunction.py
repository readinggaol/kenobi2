import IOFunction as io
import csv

def findCommonCards(decks):
    commonCards = []
    print("COMPARISON QUERY")
    firstDeck = io.chooseDeck(decks)
    secondDeck = io.chooseDeck(decks)

    for card in firstDeck:
        for checkCard in secondDeck:
            if card[1] in checkCard:
                print(card[1])
                commonCards.append(card)

    # print("\nCOMMON CARDS")
    # for card in commonCards:
    #     print(card[1])
    return commonCards




