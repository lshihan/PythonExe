from data import MENU, resources
import os


def clear():
    if os.name == "nt":
        _ = os.system('cls')


def is_rss_suff(order):
    for item in order:
        if order[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

profit = 0
is_on = True

while is_on:
    user_pref = input("What would you like? (Espresso/Latte/Cappucino)\n").lower()
    if user_pref == "off":
        is_on = False
    elif user_pref == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")       
        print(f"Coffee: {resources['coffee']}g")     
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_pref]
        is_rss_suff(drink['ingredients'])