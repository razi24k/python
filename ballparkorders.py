# this code is in progress
def orders_cost(items):
    menu={
        "nachos":6.00,
        "pizza":6.00,
        "cheeseburger":10.00,
        "water":4.00,
        "coke":5.00,
    }
    total_cost=0

    for item in items:
        if item in menu:
            total_cost += menu[item]
        else:
            total_cost += menu["coke"]
    tax=total_cost*0.07
    cost_with_tax=total_cost+tax
    print(cost_with_tax)



orders=input()
orders_list=orders.split()
orders_cost(orders_list)