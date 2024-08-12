menu = {
    "Pizza" : 40,
    "Burger": 50,
    "White Sauce Pasta": 110,
    "Cold Coffee": 100
}
print("Welcome to Shradda's Cafe_&_Restro\nHere's the Menu:")
print("Pizza : Rs.40")
print("Burger : Rs.50")
print("White Sauce Pasta : Rs.110")
print("Cold Coffee : Rs.100")

order_total = 0

item1 = input("Enter your first order : ")
if item1 in menu:
    order_total += menu[item1]
    print('Your order has been placed.')
else:
    print("We don't serve this item,please change your order.")

second_order = input('Do you want any other order? Yes/No\n')
if second_order == "Yes":
    item2 = input("Enter your second order:")
    if item2 in menu:
        order_total += menu[item2]
        print("Your order has been placed.")
    else:
        print(f"Ordered item {item2} is not available.")
        
print(f"The total amount to pay is {order_total}")
        