import random

options = ['paper', 'rock', 'scissors']
usersVictory = print('Draw!')

def compileUserAnswer(letter):
    converter = {
        'p': 0,
        'r': 1,
        's': 2,
    }
    return converter.get(letter)

def printResult(usersAnswer, computersAnswer):
    if usersAnswer == computersAnswer:
        print('Draw!')
        return
    elif usersAnswer == 'paper' and computersAnswer == 'rock':
        usersVictory
        return
    elif usersAnswer == 'rock' and computersAnswer == 'scissors':
        usersVictory
        return
    elif usersAnswer == 'scissors' and computersAnswer == 'paper':
        usersVictory
        return
    print('You have lost!')

print('That is Rock Paper Scissors game')
print('Type specific letter for each choice')
print('r - rock \np - paper \ns - scissors')
usersLetter = input('Let\'s give a shoot: \n')
while not (usersLetter == 'p' or usersLetter == 'r' or usersLetter == 's'):
    print('It seems like you didn\'t choose any of three options')
    usersLetter = input('Let\'s give a shoot: \n')

usersAnswer = options[compileUserAnswer(usersLetter)]
computersAnswer = options[random.randrange(0, 3)]

print('Your choice: ' + usersAnswer + '\nComputer choice: ' + str(computersAnswer)) 
printResult(usersAnswer, computersAnswer)
