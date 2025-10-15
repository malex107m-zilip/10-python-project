import random

name = input("What is your name ? ")
print("Good luck !",name)
words = ['rainbow''coputar','science','programming','math','player','condition',
         'reverse','water','board','geeks']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won")
        print("The word is : ",word)
        break
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have",turns,"more guesses")
        if turns == 0:
            print("You Lose")
            print("The word is : ",word)