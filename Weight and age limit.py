age = float(input("Age:"))
weight = float(input("Weight in kgs:"))
aids = str(input("aids? y or n "))

AGE_LIMIT = 16
WEIGHT_LIMIT = 50

if age > AGE_LIMIT and weight > WEIGHT_LIMIT and aids == "n":
    print("Eligible to donate blood")
else:
    print("Not eligible to donate blood")
