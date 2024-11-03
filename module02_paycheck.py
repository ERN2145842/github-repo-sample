"""
Ernest La Mertha
Module 08 Lab Assignment
Part B

This program calculates that paycheck of someone based on the amount of hours
they worked and their hourly wage.    
"""

try:
    hours_worked = int(input("How many hours did you work this week? "))
    hourly_wage = int(input("What's your hourly wage? "))

    gross_pay = hourly_wage * hours_worked
    tax_amount = gross_pay * 0.3
    net_pay = gross_pay - tax_amount
except ValueError:
    print("ERROR: this values is not a number")
    print("Please try again")
else:
    print("")
    print(f"Your gross pay is ${gross_pay}")
    print(f"Your tax amount is ${tax_amount}")
    print(f"Your net pay is ${net_pay}")
    