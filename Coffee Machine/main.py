MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    return money


def transaction(money_added, coffee):
    global profit
    if money_added == MENU[coffee]["cost"]:
        profit += MENU[coffee]["cost"]
    elif money_added > MENU[coffee]["cost"]:
        profit += MENU[coffee]["cost"]
        refund_money = round(money_added - MENU[coffee]["cost"], 2)
        print(f"Here is ${refund_money} dollars in change.")
        print(f"Here is your {coffee}☕. Enjoy!")
    else:
        print("Sorry not enough money. Money refunded.")


def coffee_making(chosen_coffee):
    if resources["water"] >= MENU[chosen_coffee]["ingredients"]["water"]:
        water = True
    else:
        water = False

    if resources["coffee"] >= MENU[chosen_coffee]["ingredients"]["coffee"]:
        coffee = True
    else:
        coffee = False

    if chosen_coffee == "latte" or chosen_coffee == "cappuccino":
        if resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
            milk = True
        else:
            milk = False

        if milk:
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
        else:
            print("Sorry there is not enough milk.")
            return
    
    if water and coffee:
        resources["water"] -= MENU[chosen_coffee]["ingredients"]["water"]
        resources["coffee"] -= MENU[chosen_coffee]["ingredients"]["coffee"]
        money = process_coins()
        transaction(money, chosen_coffee)
    elif water:
        print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")


coffee_dispenser = True
while coffee_dispenser:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        coffee_dispenser = False
    elif choice == "report":
        report()
    else:
        coffee_making(choice)