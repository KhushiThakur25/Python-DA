def atm():
    total = 10000
    pin = input("Enter PIN")
    if pin == "1234":
        print("Successfully login")
    else:
        raise ValueError("Invalid Pin")

    amount = int(input("Enter  the amount"))
    if amount > total:
        raise ValueError("Insufficient balance")
    else:
        total -= amount
        print("Remaining balance is :",total)
try:
    atm()
except ValueError as msg:
    print(msg)
    


