##Example of very long winded regex:

def isPhoneNumber(text):
    if text [0:2] == '07':
        #print('is mobile')
        return True #not mobile
    if text [0] == '+':
        #print('is international')
        return True #not international
    if text [0:2] == '44':
        #print('is UK')
        return True #Not UK
    return False

message = 'ksarhgbaksjvbasf 07414949199 asfasjgl +447414949199 askldjbvaksljdf 447414949199'
foundNumber = False

for i in range(len(message)):
    chunk = message[i:i+11]
    if (chunk[0] == '+'):
        chunk = message[i:i+13]
    if (chunk[0:2] == '44'):
        chunk = message[i:i+12]
    #print (chunk)
    if isPhoneNumber(chunk):
        print('phone number found! It is:',chunk)
        foundNumber = True
if not foundNumber:
    print('Unable to find any numbers in text')
    

    
