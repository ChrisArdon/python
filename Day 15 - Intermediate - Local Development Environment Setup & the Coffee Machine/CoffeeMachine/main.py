MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Variables
next_coffee = True


def calculate_money(coffee_flavor, cost):
    """Function that takes all the parameters and returns the total change amount"""

    # We get all the total coins inserted and multiply them by their value.
    quarters = float(input(" how many quarters?: ")) * 0.25
    dimes = float(input(" how many dimes?: ")) * 0.10
    nickles = float(input(" how many nickles?: ")) * 0.05
    pennies = float(input(" how many pennies?: ")) * 0.01

    # We add all the coins inserted
    total_amount_of_coins = quarters + dimes + nickles + pennies
    change = round(total_amount_of_coins - cost, 2)

    if total_amount_of_coins >= cost:
        return f"Here is ${change} in change. \nHere is your {coffee_flavor} ☕. Enjoy! \n"
    else:
        return "Sorry that's not enough money. Money refunded."


def calculate_resources(coffee_flavor):
    """It takes the coffee flavor and refresh the resources based on the amount of ingredients"""
    resources["water"] = resources["water"] - MENU[coffee_flavor]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee_flavor]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[coffee_flavor]["ingredients"]["coffee"]


def enough_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


while next_coffee:
    # Asking the user what type of coffee they want
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Print Report
    if coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money: ${profit}")

    # Checking the user's input to decide what to do
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if enough_resources(MENU[coffee_type]["ingredients"]):
            print("Please insert coins.")
            print(calculate_money(coffee_type, MENU[coffee_type]["cost"]))  # Here is your change
            profit += MENU[coffee_type]["cost"]
            calculate_resources(coffee_type)

    # For maintainers of the coffee machine, they can use 'off' as a secret word to turn off the machine.
    elif coffee_type == "off":
        print("Shutting Down...")
        next_coffee = False

    else:
        print("You must enter a valid option...")
