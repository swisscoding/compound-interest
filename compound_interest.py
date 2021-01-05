#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate compound interest | ----\n", fg("red")))

# user interaction
principal_investment = float(input("Principal investment: "))
interest_rate = float(input("Interest rate in %: "))
times_compounded = float(input("Times compounded: "))
time_of_investment = float(input("Time the money is invested (in years): "))

# function
def compound_interest(principal, rate, amount_of_compoundments, time):
    return round(principal * (1 + rate / amount_of_compoundments)**(amount_of_compoundments * time), 2)

amount = stylize(str(compound_interest(principal_investment, interest_rate, times_compounded, time_of_investment)), fg("green"))
print(f"\nThe amount of the future investment is calculated as {amount}.\n")
