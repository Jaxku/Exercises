import random
number = random.randint(1, 10)

guess = int(input("Guess the number: "))
while guess != number:
    if guess < number:
        print("The number is higher!")
    if guess > number:
        print("The number is lower!")
    guess = int(input("Wrong, Try again:"))
print("You got it!")
