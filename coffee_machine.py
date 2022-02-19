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
            "coffee": 24,
            "milk": 150,
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


def enough_resource(ingredients):
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"sorry there is not enough {item}.")
            return False
        return True


def process_payment():
    print('insert coins: ')
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def enongh_money(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print('here is the change ', "$",change, sep='')
        global profit
        profit += cost
        return True
    else:
        print('not enough money , so i will keep the money')
        return False


def make_coffee(choice,resources, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")


profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True
while is_on:
    choice = input('What would you like ? (espresso/latte/cappuccino): ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print("----------resources-----------")
        print('water: ', resources['water'], 'ml', sep='')
        print('milk: ', resources['milk'], 'ml', sep='')
        print('coffee: ', resources['coffee'], 'ml', sep='')
        print('profit: ', '$', profit, sep='')
    else:
        drink = MENU[choice]
        if enough_resource(drink['ingredients']):
            payment = process_payment()
            if enongh_money(payment, drink["cost"]):
                make_coffee(choice,resources, drink['ingredients'])



print(profit,resources)
