"""
Ernest La Mertha
Module 07 Lab Assignment
Part A

This program calculates that paycheck of someone based on the amount of hours
they worked and their hourly wage.    
"""

class Payment:
    def __init__(self, hours_worked, hourly_wage):
        self.__hours_worked = hours_worked
        self.__hourly_wage = hourly_wage
        self.__gross_pay = 0
        self.__tax_amount = 0
        self.__net_pay = 0
        
    def get_hours_worked(self):
        return(self.__hours_worked)
        
    def get_hourly_wage(self):
        return(self.__hourly_wage)
        
    def get_gross_pay(self):
        return(f"Your gross pay is ${self.__gross_pay}")
        
    def get_tax_amount(self):
        return(f"Your tax amount is ${self.__tax_amount}")
        
    def get_net_pay(self):
        return(f"Your net pay is ${self.__net_pay}")
        
    def calculate_gross_pay(self):
        self.__gross_pay = round(self.__hours_worked * self.__hourly_wage, 2)
        return(self.__gross_pay)
            
    def calculate_tax_amount(self):
        self.calculate_gross_pay()
        self.__tax_amount = round(self.__gross_pay * 0.3, 2)
        return(self.__tax_amount)
            
    def calculate_net_pay(self):
        self.calculate_gross_pay()
        self.calculate_tax_amount()
        self.__net_pay = round(self.__gross_pay - self.__tax_amount, 2)
        return(self.__net_pay)
