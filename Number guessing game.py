import random
number = random.randint(1, 50)
count = 1
mode = ""
while mode != "H" and mode != "E":
    mode = input("Enter 'H' for Hard mode or 'E' for Easy: ").upper()
    if mode == "H":
        num_guesses = 4
    elif mode == "E":
        num_guesses = 10
    else:
        print("That was not a correct option try again. ")

guess = int(input("Guess the number (1 to 50): "))
while guess != number and count < num_guesses:
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
