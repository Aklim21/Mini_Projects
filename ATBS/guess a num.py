import random as rd

answer = rd.randint(1,20)

print('Im thinking of a number between 1 and 20.')
print('Take a guess!')
Try = 0

while True:
    
    guess = int(input())
    if guess == answer:
        break
    if guess < answer:
        print('Too Low!')
        Try = Try + 1
        continue
    if guess > answer:
        print ('Too high!')
        Try = Try + 1
        continue
    
    

print('Nice One! You got it in', Try , 'Go(es)')     