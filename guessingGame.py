import random 

print("number Guessing Game !!!")
number=random.randint(1,9)
chances=0

print("guess a number from 1 to 9...")
while chances<5:
    guess=int(input("enter ur guess"))
    if guess ==number:
        print("you guessed the number !!!")
        break
    elif guess < number:
        print("too low pick a higher number ")
    else:
        print("too high pick a lower number ")
    chances+=1

if not chances <5:
    print("u lose !!! the number is ",number)
