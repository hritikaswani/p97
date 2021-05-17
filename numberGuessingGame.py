import random
gotCorrect = False
tries = 5
numberGenerator = round(random.randint(1,9))

while gotCorrect == False:
    answer = int(input("What is the number? "))

    if (answer == numberGenerator):
        print("You are correct")
        tries += 1
        gotCorrect = True
        

    elif (answer > numberGenerator):
        print("Too big")
        tries = tries - 1

    else:
        print("Too small")
        tries = tries - 1

if tries > 0:
    print("Congratulations!")

else:
    print("Too Bad!")
