def main():
    total = 0
    while total < 75:
        input_coins = int(input("Please enter coins. "))
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

