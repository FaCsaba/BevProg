#!/usr/bin/env python3
# coding: utf8

# Homework 1:
# Excersize in getting input from a user and using an if statement
# Ask the user for their age and based on that write out if they can:
#   - legally drink in the United States of America
#   - can legally buy cigarette products in Hungary
#   - can legally obtain a drivers license in Hungary
#   - can watch Shrek 2, a film rated for 12 and above

# Caveats: excersize did not specify if we are only allowed to display a single fact,
# I choose to interpret that as we may choose to display these facts as they come

def ask_for_input() -> int:
    while True:  # simple error handling. if user provides incorrect data we loop until we get a number
        try:
            inp = input("What is your age? ")
            return int(inp)
        except ValueError as err:
            print("{inp} is not a number".format(inp=inp))
            continue


AMERICAN_LEGAL_DRINKING_AGE = 21
CAN_BUY_CIGARETTES_IN_HUNGARY = 18
HUNGARIAN_LEGAL_AGE_TO_GET_A_DRIVERS_LICENSE = 17
CAN_WATCH_SHREK_2 = 12


def main():
    age = ask_for_input()
    if age >= AMERICAN_LEGAL_DRINKING_AGE:
        print("🇺🇸🦅🇺🇸 AMERICA FUCK YEAH!! You can drink alcohol in this beautiful free country 🇺🇸🦅🇺🇸!!!!!")
    if age >= CAN_BUY_CIGARETTES_IN_HUNGARY:
        print("Congrats you can corrode your lungs with fags. You can legally buy cigarette products in hungary")
    if age >= HUNGARIAN_LEGAL_AGE_TO_GET_A_DRIVERS_LICENSE:
        print("You can have a drivers license in Hungary. Doesn't mean you can afford it though.")
    if age >= CAN_WATCH_SHREK_2:
        print("You can watch the best piece of cinema there is. You are allowed to view Shrek 2!")
    else:
        print("You are a literal baby. You can't do anything")


if __name__ == "__main__":
    main()
