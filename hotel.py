print("restaurent billing system")
pizza = 150
burger = 80
pasta = 120
print("1.pizza - rs 150")
print("2.burger - rs 120")
print("3.pasta - rs 350")
choice=int(input("enter your choice:"))
quantity=int(input("enter your quantity:"))
if choice == 1:
    item="pizza"
    price = pizza
elif choice == 2:
    item="burger"
    price = burger
elif choice == 3:
    item="pasta"
    price = pasta
else:
    print("invalid choice")
    exit()
total =price * quantity
print("\n------Bill------")
print("item:",item)
print("quantity:",quantity)
print("price:",price)
print("total:",total)
print("Thank you")



