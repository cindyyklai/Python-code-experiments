def hotel_cost(days):
    return 140 * days


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    if city == "Tampa":
        return 220
    if city == "Pittsburgh":
        return 222
    if city == "Los Angeles":
        return 475


def rental_car_cost(days):
    if days >= 7:
        return days * 40 - 50
    elif days >= 3:
        return days * 40 - 20
    else:
        return days * 40


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money


print trip_cost("Los Angeles", 5, 600)