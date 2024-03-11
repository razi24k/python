import os

users_cart = {}


# defining all functions that a user may choose
def add_item(user, product, price, number_unit=1):
    users_cart[user][product] = [price, number_unit]
    print(f"{number_unit} {product} added to {user} cart lists that equals to: {price * number_unit}$")
    try:
        if isinstance(price, (float, int)) and isinstance(number_unit, (int)):
            pass
        else:
            raise ValueError
    except ValueError:
        print("Invalid input! please enter only numbers")
        add_item(user, product, price, number_unit=1)


def remove_item(user, product, number_unit):
    try:
        if user not in users_cart:
            raise ValueError(f"User {user} has not any cart in this shop!\nThe users are: {users_cart.keys()} ")
        elif product not in users_cart[user]:
            raise ValueError(f"Product {product} not found! \nUser's products are: {users_cart[user].keys()}")
    except ValueError:
        remove_item(user, product, number_unit)
    users_cart[user][product][1] -= number_unit
    if users_cart[user][product][1] < 2:
        users_cart[user].pop(product)


def show_item(user):
    print(f"your cart contains this products:\n{users_cart[user]}")


def cart_price(user):
    price = 0
    for product in users_cart[user].keys():
        price += users_cart[user][product][0] * users_cart[user][product][1]
    return price


stop = False
print("------Hello! here is my tiny shop------")
while not stop:
    user_name = input("Please enter The User's name: ").title()
    users_cart[user_name] = {}
    user_decision = input("Please enter your choice below: \n1. Add item\n2. Remove item\n3. Show cart\n"
                          "4. your cart price\n5. exit\nyour choice here:")
    if user_decision == "5":
        stop = True
    elif user_decision == "1":
        os.system("clear")
        while True:
            add_stop = input("Please enter any key to continue and s to stop: ")
            if add_stop == "s":
                break
            try:
                add_item(user_name, input("Please enter Product's name: "),
                        float(input("Please enter price of product: ")), int(input("Please enter number of units: ")))
            except ValueError:
                print("Invalid input for price or number unit! please try again...")
    elif user_decision == "2":
        os.system("clear")
        while True:
            remove_stop = input("Please enter any key to continue and s to stop: ")
            if remove_stop == "s":
                break
            remove_item(user_name, input("Please enter Product's name: "),
                        int(input("Please enter number of units: ")))
    elif user_decision == "3":
        os.system("clear")
        while True:
            show_item(user_name)
            show_stop = input("Please enter any key to return to menu: ")
            if show_stop:
                break
    elif user_decision == "4":
        os.system("clear")
        while True:
            print(f"your cart is: {show_item(user_name)} \nand it's cost is: {cart_price(user_name)}")
            price_stop = input("Please enter any key to return to menu: ")
            if price_stop:
                break
    else:
        os.system("clear")
        print("Invalid input please try again...")
