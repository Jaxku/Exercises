import random
number = random.randint(1, 50)
count = 1
print(number)
guess = int(input("Guess the number (1 to 50): "))
while guess != number and count < 10:
    count += 1
    if guess < number:
        print("The number is higher!")
    else:
        print("The number is lower!")
    guess = int(input("Try again:"))
if guess == number:
    print(f"You got it! It took you {count} guesses")
else:
    print("You used up your 10 guesses")
