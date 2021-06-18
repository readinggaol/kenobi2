#will hopefully read lines from a file and allow me to manipulate them
import csv
import IOFunction as io
import manipulationFunction as mf








def main():
    deckNames = io.searchDirectoryForDecks()
    # print(io.chooseDeck(deckNames))
    print(mf.findCommonCards(deckNames))



if __name__ == "__main__":
    main()