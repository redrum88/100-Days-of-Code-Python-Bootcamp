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
    "milk": 1000,
    "coffee": 100,
}
POWER = True
bank = 0.00


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins():
    """Returns the total calculated from coins inserted"""
    question = input("Type 'y' if you want insert coins, type 'n' to back to main MENU: ")
    if question == "y":
        total = int(input("How many quarters $0.25 you want insert?: ")) * 0.25
        total += int(input("How many dimes $0.10 you want insert?: ")) * 0.10
        total += int(input("How many nickles $0.05 you want insert?: ")) * 0.05
        total += int(input("How many pennies $0.01 you want insert?: ")) * 0.01
        return total


def admin_menu():
    print(f"\n ***** ****    ADMIN COMMANDS     **** ***** ")
    print(f" ***** ADD WATER: 'add water 123'  *** ")
    print(f" ***** DEL MILK: 'del milk 123'   **** ")
    print(f" ***** ADD COFFEE: 'add coffee 123' ** ")
    print(f" ***** ****  ADMIN COMMANDS END   **** ***** \n")
    admin_command = input("Please enter command as shown above: ")

    if admin_command == "exit":
        print("You exited ADMIN MODE")
        return

    else:
        print("*** Report: report after admin command what happened and if successful ")
        return admin_menu()


def is_good(received, cost):
    """Return True when payment is accepted, or False if money is insufficient"""
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Here is ${change} in change.💰")
        global bank
        bank += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {name} 🍵.")
while POWER:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        POWER = False
        print("Coffee machine is powering down...")

    elif choice == "report":
        total_water = int(resources["water"])
        total_milk = int(resources["milk"])
        total_coffee = int(resources["coffee"])
        print(f"Power Status: {POWER} . All works good.\n")
        print(f"COMMAND: >>> {choice} <<<  ### Its tells in which mode currently running coffe machine.")
        print(f"Total water in machine: {total_water}ml")
        print(f"Total milk in machine: {total_milk}ml")
        print(f"Total coffee in machine: {total_coffee}ml\n")
        print(f"COINS: ${bank}\n")

    elif choice == "admin":
        admin_menu()
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = insert_coins()
            if is_good(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
        #CALL function ADMIN MENU

