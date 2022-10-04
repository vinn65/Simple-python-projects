import random

print('What is your name?: ')
name = input()

print('I am thinking of a number between 1 and 20')
secNum = random.randint(1,20)

for guesses in range(1,7):
    print('Take a guess')
    UserNum = int(input())
    if UserNum < secNum:
        print('Your guess is too low')
    elif UserNum > secNum:
        print('Your guess is too high')    
    else:
        break

if UserNum == secNum:
    print('Good job! You guessed my number in: ' + guesses+ " guesses")
else:
    print('The number I was thinking of is: ' + str(secNum))    