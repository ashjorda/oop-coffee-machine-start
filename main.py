import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
machine = CoffeeMaker()
machine_money = MoneyMachine()

machine_state = True

while machine_state:
    drink_selection = input(f"What would you like? " + coffee_menu.get_items()).lower()

    if drink_selection == "report":
        machine.report()
        machine_money.report()
    elif drink_selection == "off":
        machine_state = False
    elif drink_selection in ["latte", "espresso", "cappuccino"]:
        if machine.is_resource_sufficient(coffee_menu.find_drink(drink_selection)):
            if machine_money.make_payment(coffee_menu.find_drink(drink_selection).cost):
                machine.make_coffee(coffee_menu.find_drink(drink_selection))
    else:
        print("You have entered an incorrect menu item.")


