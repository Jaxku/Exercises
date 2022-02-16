count = 0
password ="Souldossier"
attempt = input("What is your password: ")
while count < 3 and attempt != password:
    attempt = input("Password incorrect, try again: ")
    count += 1
    if attempt == password:
        print("Yes correct you are a Soul Dossier")
    else:
        print("To many attempted to become Soul Dossier")
