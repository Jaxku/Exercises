#Moral Age Verification System to see if you are old enough to get a drivers licence

#The age of the child is a constant
license_age = 16
age = int(input("What is your age? :"))

#Checking system to see the teenager is old enough to get a drivers licence
if age > license_age:
    print("You are eligible to apply for a Driver's Licence in Aotearoa")
