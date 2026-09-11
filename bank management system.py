balance = 3000
while True:
    print("\n1.deposit 2.withdraw 3.balance 4.exit")
    ch = int(input("choice:"))

    if ch == 1:
        balance += int(input("Amount:"))
    elif ch == 2:

         a = int(input("Amount: "))
         if a<= balance:
             balance -= a
         else:
             print("insufficient balance")
    elif ch == 3:
              print("balance:",balance)
    elif ch == 4:
              break




