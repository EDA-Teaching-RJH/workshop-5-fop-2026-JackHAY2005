import re
def main():
    camel = input("What is your first and last name? ")

    for i in range(len(camel)):
        if camel[i].isupper():
            print("_" + camel[i].lower(), end="")
        else:
            print(camel[i], end="")
main()