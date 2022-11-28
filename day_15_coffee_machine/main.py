from data import MENU, resources

# RESOURCES

total_water = int(resources["water"])
total_milk = int(resources["milk"])
total_coffee = int(resources["coffee"])

#
# power = True
money = 0
POWER = "Online"
user_input = "shop"
coins = 0.00
print(f"Power Status: {POWER} . All works good.\n")
print(f"USER NAME: >>> {user_input} <<<  ### Its tells in which mode currently running coffe machine.")

print("\n##### CURRENTLY RESOURCES IN MACHINE #####")
print(f"Total water in machine: {total_water}ml")
print(f"Total milk in machine: {total_milk}ml")
print(f"Total coffee in machine: {total_coffee}ml\n")
print(f"\nCOINS: ${coins}")


# POWER SWITCH ON OFF function 'off()' once it called machine will go down and print message
def off():
    global POWER
    POWER = False
    print(f"function off() has been called and POWER set to: {POWER}")
    return POWER


def price(coffee):
    for coffee in MENU:
        #     print(coffee)
        coffee = MENU[coffee]
        price = coffee["cost"]
        #    print(*coffee["ingredients"])
        water_cost = coffee["ingredients"]["water"]
        coffee_cost = coffee["ingredients"]["coffee"]
        #     print(f"# coffee = {coffee}  \n#  price = {price} \n#  water_cost = {water_cost} \n#  coffee_cost = {coffee_cost}")
        return coffee, price, water_cost, coffee_cost
        #    print(price)
        return price
    return


def pay():
    global coins
    total_price = price()
    coins = coins - total_price
    return coins


def insert_coins():
    global coins
    global POWER
    question = input("Type 'y' if you want insert coins, type 'n' to back to main MENU: ")
    if question == "y":
        coin_quarters = int(input("How many quarters $0.25 you want insert?: "))
        coin_dimes = int(input("How many dimes $0.10 you want insert?: "))
        coin_nickles = int(input("How many nickles $0.05 you want insert?: "))
        coin_pennies = int(input("How many pennies $0.01 you want insert?: "))
        coin_quarter = 0.25 * coin_quarters
        coin_dime = 0.10 * coin_dimes
        coin_nickle = 0.05 * coin_nickles
        coin_penny = 0.01 * coin_pennies
        coins = coin_quarter + coin_dime + coin_nickle + coin_penny
        POWER = True
        pay()
        return


def ask():
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        off()
    if user_input == "admin":
        def admin():
            print(f"\n ***** ****    ADMIN COMMANDS     **** ***** ")
            print(f" ***** ADD WATER: 'admin add water 123'  *** ")
            print(f" ***** ADD MILK: 'admin add milk 123'   **** ")
            print(f" ***** ADD COFFEE: 'admin add coffee 123' ** ")
            print(f" ***** ****  ADMIN COMMANDS END   **** ***** \n")

        admin()
        ask()
    if user_input == "espresso":
        insert_coins()
        print("Here your espresso")
    if user_input == "latte":
        print("You just purchase latte")
    if user_input == "cappuccino":
        print("Cappuccino is ready!")


ask()
print(f"Coins left: ${round(coins, 2)}")
print(f"\nPOWER at the bottom: {POWER}")
