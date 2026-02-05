# **"Statement of Requirements"**
# **Functional Requirements:** 
#  What inputs (specific coin integers) does the system accept? 50p, 20p, 10p, 5p
#  What is the exact output (change calculation)? Total amount entered, amount still owed, and change if total exceeds 75p.
# **Non-Functional Requirements:** 
# How should the system behave if the user inputs a string (e.g., "ten pence") instead of an integer? It doesnt accept it and prompts the user to enter a valid coin.
def main():
    total = 0
    while total < 75:
        input_coins = input("Please enter a coin (5, 10, 20, or 50): ")
        if not input_coins.isdigit():
            print("Invalid input. Please enter a valid coin value.")
            continue
        input_coins = int(input_coins)
        if total == 75:
            print("You have entered 75p. You can buy a coffee.")
        elif input_coins == 0:
            print("You have entered 0p. Please enter coins.")
        elif input_coins == 5:
            total += input_coins
            print("You have entered 5p.")
        elif input_coins == 10:
            total += input_coins
            print("You have entered 10p.")
        elif input_coins == 20:
            total += input_coins
            print("You have entered 20p.")
        elif input_coins == 50:
            total += input_coins
            print("You have entered 50p.")
        else:
            print("Invalid coin. Please enter 5p, 10p, 20p, or 50p.")
        amount_owed = 75 - total
        if amount_owed > 0:
            print("You still need " + str(amount_owed) + "p.")
        else:
            change = total - 75
            print("Here is your coffee. Your change is " + str(change) + "p.")

main()

