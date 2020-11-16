import re

message = 'My UK numb: 07414949199, or +447414949199 if you\'re international'
UKNumbRegex = re.compile(r'(\+\d\d|0)?(\d\d\d\d\d\d\d\d\d\d)')

matchObjectUKNumb = UKNumbRegex.search(message)
print(matchObjectUKNumb.group())


