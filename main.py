import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    while True:
        user_choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if user_choice == "off":
            print("Thank you for coming! Goodbye <3 ")
            break
        elif user_choice == "report":
            sandwich_maker_instance.show_report()
        elif user_choice in recipes:
            sandwich_size = user_choice
            order_ingredients = recipes[sandwich_size]["ingredients"]
            if sandwich_maker_instance.check_resources(order_ingredients):
                sandwich_maker_instance.make_sandwich(sandwich_size, order_ingredients, cashier_instance)
            else:
                print("Insufficient resources to make the sandwich.")
        else:
            print("Invalid choice. Please enter 'small', 'medium', 'large', 'off', or 'report'.")

if __name__ == "__main__":
    main()

