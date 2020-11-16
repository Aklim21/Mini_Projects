## Letter counter

##Importing  pretty print for better formatting
import pprint

text = 'Once upon a time in the Eldritch Woods there lived a Lonely Beast known as Pylon...He had always hated his parents for cursing him with this name.'

##create empty dictionary to hold each value, with the characters as the key.
count = {}

##for loop over text with a set default method on each new character.
##run text.upper to merge character cases.

for character in text.upper():
    count.setdefault(character,0)
    count[character] = count[character] + 1

##create list, and organises in alphabetical order
##pprint.pprint(count)

ftext = pprint.pformat(count)
print(ftext)
