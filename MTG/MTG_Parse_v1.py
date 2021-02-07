import sys


############ DeckList Parser ##############
def Parser(deckText):
    #deck level
    ParsedDeckList = ""
    for i in deckText:
        count = -1
    #card level
        for j in i:
            count += 1
            if j == "(":
                card = i[:-(len(i)-count)]
                ParsedDeckList += (card + "\n")
    return ParsedDeckList

############ Input validation ##############

try: 
    deckList = sys.argv[1]

except IndexError as e:
    print (e)
    print("""You didn't provide a valid MTG decklist.\n\nDon't try to launch this like a script you sillybilly!\nDrag a MTG decklist in a .txt format into this batch file.\nIt will then output a Parsed.txt file.\n""")
    sleep = input("Press enter to continue")
    sys.exit()



############ Data Parse ##############

deckList = sys.argv[1]
data = open(deckList, "r")        
text = Parser(data)
if not text:
    print("""Decklist already parsed you fool!\nIt's time to dudududu DUEL!""")
    sleep = input("Press enter to continue")


############ Output data to file ##############

text_file = open("Parsed.txt", "w")
text_file.write(text)
text_file.close() 

