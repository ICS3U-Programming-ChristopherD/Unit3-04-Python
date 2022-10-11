#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Oct. 11, 2022
# This program checks if an integer is positive, negative, or neither.


def main():
    user_integer = int(input("Enter an integer: "))

    if user_integer > 0:
        print(f"{user_integer} is positive.")

    elif user_integer < 0:
        print(f"{user_integer} is negative.")

    else:
        print("Your integer is not negative or positive (0).")


if __name__ == "__main__":
    main()
