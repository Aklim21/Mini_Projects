def collatz(number):
    if (number % 2) == 0:
        return (number//2)
    else:
        return(3*number+1)

print('Enter a number')

number = ''
while not number:        
        try:
            number = int(input())
        except ValueError:
            print('Please enter an integer value')
loop = 0

while True:
    value = collatz(number)
    if value == 1:
        break
    else:
        loop = loop+1
        number = collatz(number)
        print(collatz(number))
        continue
    
print('End')
print('Loop =', loop)
        
    