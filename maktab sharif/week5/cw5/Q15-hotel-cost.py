def hotel_cost(nights):
    return nights * 140


def plane_ride_cost(city):
    # Input
    cost = {"Charlotte": 183,
            "Tampa": 220,
            "Pittsburgh": 222,
            "Los Angeles": 475,
            }

    if city in cost.keys():
        return cost[city]
    else:
        return "Wrong City!"


def rental_car_cost(days):
    cost_of_car = days * 40
    if days >= 7:
        return cost_of_car - 50
    elif days >= 3:
        return cost_of_car - 20
    else:
        return cost_of_car


def trip_cost(city_y, days_s ,  spending_money):
    return hotel_cost(nights=days_s) + plane_ride_cost(city=city_y) + rental_car_cost(days=days_s) + int(spending_money)


city_y = input("Which city are you going to visit?")
days_s = int(input("How many days?"))
spending = int(input("How much money will you spend during the trip?"))
print(trip_cost(city_y, days_s, spending))