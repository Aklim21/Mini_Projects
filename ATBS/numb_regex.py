import re

message = 'ksarhgbaksjvbasf 07414949199 asfasjgl +447414949199 askldjbvaksljdf 447414949199'

#r'' results in the raw string
#/d recognised a digit character
MobileNumbRegex = re.compile(r'07\d\d\d\d\d\d\d\d\d')
UKNumbRegex = re.compile(r'44\d\d\d\d\d\d\d\d\d\d')

#re.compile() calls the compile method on the defined expression

matchObjectmob = MobileNumbRegex.search(message)
matchObjectUKNumb = UKNumbRegex.findall(message)

print('Mobile:',matchObjectmob.group())


#If we are looking for the
print(UKNumbRegex.findall(message))
print('search returned %s result(s)', len(matchObjectUKNumb))
