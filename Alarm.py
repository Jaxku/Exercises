day = int(input("What day is it: ?\n1 Mon, 2 Tue..... 7 Sun: "))
if day < 6 and day > 0:
    print("Alarm rings at 7")
elif day == 6:
    print("Alarm rings at 8")
elif day == 7:
    print("Alarm rings at 9")
else:
    print("That was not a number between 1 and 7 do you think you're funny and making a joke you're not funny and thats a horrible joke no wonder your single")
