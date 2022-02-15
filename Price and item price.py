price = float(input("What is the price: "))
type = input("What type of item\neg food, electrical etc.")
if price > 10:
    if type == "food":
         price *= 0.60
    elif type == "electrical":
        price *= 0.70
    else:
        price *= 0.80

print(f"The price for your {type} item will be ${price:,.2f}")
