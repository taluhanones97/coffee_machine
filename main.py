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
answer="temp"
secret_word="off"

quarters = 0
dimes = 0
nickles = 0
pennies = 0
money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

while answer!=secret_word:

    answer = input("What would you like? (espresso/latte/cappuccino): ")
    secret_word="off"



    if answer == "report":
        print(resources)
        print("money: "+str(money))
    elif answer == "espresso":

        if resources["water"] >= 50 and resources["coffee"] >= 18:

            print("Please insert coins")
            quarters += int(input("How many quarters?: "))
            dimes += int(input("How many dimes?: "))
            nickles += int(input("How many nickles?: "))
            pennies += int(input("How many pennies?: "))
            money += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            if money >= MENU["espresso"]["cost"]:
                money -= MENU["espresso"]["cost"]
                resources["water"] -= 50
                resources["coffee"] -= 18
                print(f"Here is ${money} in charge.")

                print("E.g. report before purchasing espresso:")
                print("Water: 300ml")
                print("Milk: 200ml")
                print("Coffee: 100g")
                print("Money: $0")

                print("E.g. report after purchasing espresso:")
                print("Water:" + str(resources["water"]))
                print("Milk: " + str(resources["milk"]))
                print("Coffee: " + str(resources["coffee"]))
                print("Money: $" + str(money))
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif resources["water"] < 50 or resources["coffee"] < 18 :
            if resources["water"] < 50:
                print("Sorry not enough water")
            if resources["coffee"] < 18:
                print("Sorry not enough coffee")


    elif answer == "latte":

        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:

            print("Please insert coins")
            quarters += int(input("How mny quarters?: "))
            dimes += int(input("How many dimes?: "))
            nickles += int(input("How many nickles?: "))
            pennies += int(input("How many pennies?: "))
            money += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

            if money >= MENU["latte"]["cost"]:
                money -= MENU["latte"]["cost"]
                resources["water"] -= 200
                resources["coffee"] -= 24
                resources["milk"] -= 150
                print(f"Here is ${money} in charge.")

                print("E.g. report before purchasing latte:")
                print("Water: 300ml")
                print("Milk: 200ml")
                print("Coffee: 100g")
                print("Money: $0")

                print("E.g. report after purchasing latte:")
                print("Water:" + str(resources["water"]))
                print("Milk: " + str(resources["milk"]))
                print("Coffee: " + str(resources["coffee"]))
                print("Money: $" + str(money))
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif resources["water"] < 200 or resources["coffee"] < 24 or resources["milk"] < 150:
            if resources["water"] < 200:
                print("Sorry not enough water")
            if resources["coffee"] < 24:
                print("Sorry not enough coffee")
            if resources["milk"] < 150:
                print("Sorry not enough milk")

    elif answer == "cappuccino":

        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:

            print("Please insert coins")
            quarters += int(input("How mny quarters?: "))
            dimes += int(input("How many dimes?: "))
            nickles += int(input("How many nickles?: "))
            pennies += int(input("How many pennies?: "))
            money += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

            if money >= MENU["milk"]["cost"]:
                money -= MENU["milk"]["cost"]
                resources["water"] -= 250
                resources["coffee"] -= 24
                resources["milk"] -= 100
                print(f"Here is ${money} in charge.")

                print("E.g. report before purchasing cappuccino:")
                print("Water: 300ml")
                print("Milk: 200ml")
                print("Coffee: 100g")
                print("Money: $0")

                print("E.g. report after purchasing cappuccino:")
                print("Water:" + str(resources["water"]))
                print("Milk: " + str(resources["milk"]))
                print("Coffee: " + str(resources["coffee"]))
                print("Money: $" + str(money))
            else:
                print("Sorry that's not enough money. Money refunded.")
        elif resources["water"] < 250 or resources["coffee"] < 24 or resources["milk"] < 100:
            if resources["water"]<250:
                print("Sorry not enough water")
            if resources["coffee"]<24:
                print("Sorry not enough coffee")
            if resources["milk"]<100:
                print("Sorry not enough milk")



