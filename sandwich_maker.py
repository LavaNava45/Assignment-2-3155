from data import recipes
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for ingredient, required_amount in ingredients.items():
            if self.machine_resources.get(ingredient, 0) < required_amount:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients, cashier_instance):
        recipe = recipes[sandwich_size]["ingredients"]  # Fixed variable name here
        cost = recipes[sandwich_size]["cost"]  # Fixed variable name here

        if self.check_resources(recipe):
            print("Please insert coins.")
            coins_inserted = cashier_instance.process_coins()
            if cashier_instance.transaction_result(coins_inserted, cost):
                print(f"{sandwich_size.capitalize()} sandwich is ready. Bon appétit!")
                for ingredient, amount in recipe.items():
                    self.machine_resources[ingredient] -= amount

    def show_report(self):
        for ingredient, amount in self.machine_resources.items():
            unit = "slice(s)" if ingredient in ["bread", "ham"] else "ounce(s)" if ingredient == "cheese" else "unit(s)"
            print(f"{ingredient.capitalize()}: {amount} {unit}")

