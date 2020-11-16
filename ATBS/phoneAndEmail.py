#! python 3
import re, pyperclip

#method to pass in data

#copy in data from clipboard

#paste in data to script from clipboard
text = pyperclip.paste()

#create regex for phone numbers
phoneRegex = re.compile(r'''
((\+\d\d|0)\d\d\d\d\d\d\d\d\d\d)
#allows for mobile as well as international

''',re.VERBOSE)

#create regex for emails
emailRegex = re.compile(r'''

#structure
#<name>(@)<domain>(.)(industry)
#name& domain:
#create unique character class:
#[a-zA-Z0-9.+]+
#industry: (com|co.uk|gov|gov.uk|ac.uk|edu)

([a-zA-Z0-9.+]+
@
[a-zA-Z0-9.+]+
.
(com|co.uk|gov|gov.uk|ac.uk|edu))

''',re.VERBOSE)
#extract data from text
phoneNumbers = phoneRegex.findall(text)
emailList = emailRegex.findall(text)
#both will return lists of the matching results

#present data in clean way

UKDirectory = []
intDirectory = []
allNumbers = [UKDirectory,intDirectory]

for i in phoneNumbers:
    if i[1] == '0':
        UKDirectory.append(i[0])
    else:
        intDirectory.append(i[0])
'\n'.join(UKDirectory)
'\n'.join(intDirectory)

addressBook = []

for i in emailList:
    addressBook.append(i[0])

'\n'.join(emailList)

print('UK numbers:',UKDirectory)
print('International Numbers:',intDirectory)
print('Email Addresses:',addressBook)



