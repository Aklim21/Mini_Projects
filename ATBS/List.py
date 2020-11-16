carbrands=[]
while True:
    print('List as many car brands as you can.')
    print('Enter nothing when you run out of guesses')
    brand = input()
    if brand == '':
        print('''Enter nothing again if you're REALLY out of guesses.''')
        brand = input()
        if brand == '':
            break
        carbrands = carbrands + [brand]
    
    carbrands = carbrands + [brand]
print('Your guesses:')

for i in range(len(carbrands)):
    print ('Index '+ str(i)+ ' in carbrands is: '+ carbrands[i])
    
    