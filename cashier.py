class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        largeDollars = int(input("How many large dollars?: "))
        halfDollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        totalAmount = 1 * largeDollars + 0.5 * halfDollars + 0.25 * quarters + 0.05 * nickels
        return totalAmount

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
        return True