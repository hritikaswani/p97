import random

a = random.randint(0,9)

guess = int(input("Enter an integer from 1 to 9: "))
while a != "guess":
    print
    if (guess < a):
        print("Your guess was too low!")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif (guess > a):
        print("Your guess was too high!")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print("YOU GUESSED IT!!!!")
     
    print