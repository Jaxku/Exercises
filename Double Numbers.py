#Doubling numbers

def calculate_double(amount):
    double = amount * 2
    return double

# Main routine
question = int(input("How much? "))
answer = calculate_double(question)
print(f"Double {question} is {calculate_double(question)}")


#Halfing numbers

def calculate_half(amount2):
    half = amount2 // 2
    return half

#Main routine
amount2 = int(input("How much? "))
answer = calculate_half(amount2)
print(f"Half of {amount2} is {calculate_half(amount2)}")

#10 more

def calculate_add10(amount3):
    tenmore = amount3 + 10
    return tenmore

amount3 = int(input("How much? "))
answer = calculate_add10(amount3)
print(f"Half of {amount3} is {calculate_add10(amount3)}")


