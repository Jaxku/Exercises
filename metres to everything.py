#Get input
metres = int(input("Enter a number of metres for converison: "))

#Converison info bank
millimeters = metres * 1000
centimetres = metres * 100
kilometres = metres / 1000
inches = centimetres / 2.54
feet = metres * 3.28084
miles = kilometres * 0.621371
yards = metres * 1.09361

#results

print(metres, "metres is: ")
print(millimeters, "millimeters: ")
print(centimetres, "centimtres: ")
print(kilometres, "kilometres: ")
print(inches, "inches: ")
print(feet, "feet")
print(miles, "miles: ")
print(yards, "yards")

