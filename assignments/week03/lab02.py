# Complete this ATM simulation
'''
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")
'''
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "2":
            withdraw = float(input("How much money will you Withdraw?: "))
            if withdraw > balance or withdraw < 0:
                print("Cannot Withdraw")
                continue
            elif withdraw < balance:
                balance = balance - withdraw
            print(f"Successfully, Your balance now = {balance}")

        if choice == "3":
            deposit = float(input("How much money will you Deposit: "))
            if deposit < 0:
                print("Cannot deposit less than 0")
                continue
            else:
                balance = deposit + balance
                print(f"Successfully, Your balance now = {balance}")

        if  choice == "4":
            print("Exit")
            break

        if choice == "1":
            print(f"balance = {balance}THB")
        else:
            continue

else :
    print("Invalid PIN")