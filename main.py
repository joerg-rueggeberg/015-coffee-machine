from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def check_resources(order_input):
    """Überprüft, ob genügend Ressourcen vorhanden sind, um das Getränk herzustellen."""
    for resource in MENU[order_input]["ingredients"]:
        if resources[resource] < MENU[order_input]['ingredients'][resource]:
            print(f"Sorry, there is not enough {resource}")
            return False
        else:
            resources[resource] -= MENU[order_input]['ingredients'][resource]
    return True


def process_coins(price_input):
    """Verlangt den Preis des georderten Getränkes in Münzen. Meldet, falls zu wenig und gibt Rückgeld falls zu viel"""
    print(f"Please enter ${price_input} in coins.")
    coins_sum = 0
    quarter = 0.25
    dimes = 0.1
    nickles = 0.05
    pennies = 0.01
    quarter_sum = round(int(input("How many Quarters? ")) * quarter, 2)
    coins_sum += quarter_sum
    if coins_sum < price_input:
        dime_sum = round(int(input("How many Dimes? ")) * dimes, 2)
        coins_sum += dime_sum
        if coins_sum < price_input:
            nickles_sum = round(int(input("How many Nickles? ")) * nickles, 2)
            coins_sum += nickles_sum
            if coins_sum < price_input:
                pennies_sum = round(int(input("How many Pennies? ")) * pennies, 2)
                coins_sum += pennies_sum
                if coins_sum < price_input:
                    print("Sorry that's not enough money. Money refunded.")
    if coins_sum == price_input:
        return True
    else:
        change = coins_sum - price_input
        print(f"Here is ${round(change,2)} in change.")
        return True


shutdown = False

print(logo)
while not shutdown:
    price = ""
    order = input("What would you like? (espresso/ latte/ cappuccino): ").lower()
    if order == "off":
        shutdown = True
    elif order == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']}")
    else:
        price = MENU[order]["cost"]

    if price != "" and check_resources(order):
        if process_coins(price):
            resources["money"] += MENU[order]["cost"]
            print(f"Here is your {order.title()} ☕. Enjoy!")
