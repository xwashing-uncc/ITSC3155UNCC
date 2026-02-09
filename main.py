import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True
    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report) ").strip().lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            for item, amount in sandwich_maker_instance.machine_resources.items():
                print(f"{item}: {amount}")
        elif choice in recipes:
            order = recipes[choice]
            if sandwich_maker_instance.check_resources(order["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, order["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, order["ingredients"])
        else:
            print("Invalid selection.")

if __name__=="__main__":
    main()
