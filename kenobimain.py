#will hopefully read lines from a file and allow me to manipulate them
import csv
import IOFunction as io
import manipulationFunction as mf
from tkinter import *

deckNames = io.searchDirectoryForDecks()


root = Tk()

titleLabel = Label(root, text="Welcome to Kenobi2!")
titleLabel.pack()

showDecksButton = Button(root, text="SHOW MANAGED DECKS", command=lambda : io.displayDirectoryDecks(root, deckNames))
showDecksButton.pack()

root.mainloop()


# def main():
#     deckNames = io.searchDirectoryForDecks()
#      print(io.chooseDeck(deckNames))
#     print(mf.findCommonCards(deckNames))


#
# if __name__ == "__main__":
#     main()