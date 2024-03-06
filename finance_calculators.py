import math

""" The user will initially see the following screen with the question asking them to choose either 'investment' or 'bond' for the calculation option
"""
print("investment - to calculate the amount of interest you'll earn on your Investment")
print("bond - to calculate the amount you'll have to pay on a home loan.")

#user is asked to select the type of calculator they want to use

calculator = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")

#bond calculator starts here

if calculator == "bond" or calculator == "BOND" or calculator == "Bond":
    
#these are the variables required for the bond calculation

    house_value = float(input("Please enter the house value now: "))
    mortgage_rate = float(input("Please enter the interest rate without any % symbol e.g. 7: "))
    monthly_rate = mortgage_rate/(12*100)
    no_of_months_to_repay = int(input("Please enter the number of months you would like to repay your mortgage for e.g. 120: "))
    monthly_repayment_amount = (monthly_rate) * (house_value) / (1 - (1 + monthly_rate)**(-no_of_months_to_repay))

#This is the calculated amount for monthly repayment with 2 decimals
    print("The total monthly repayment amount will be: " + str(monthly_repayment_amount))

# Investment calculator starts here

elif calculator == "investment" or calculator == "INVESTMENT" or calculator == "Investment": 
    
# variables required for the investment calculation, entered by the user

    amount_to_invest = float(input("Enter the amount of money you would like to invest: "))
    
    interest_rate = float(input("Enter the interest rate - you should only enter the applicable rate e.g. 8 rather than 8%: "))
    
    no_of_years = int(input("Enter the number of years you would like to invest it for: "))
#user is asked to enter "simple" or "compound" interest to use the calculator

    interest_type = input("Enter either 'simple' or 'compound' option for your interest calculation: ")
    
# a nested table to separate "simple" interest calculation from "compound" calculation.

    if interest_type == "simple": 
        new_amount_with_simple_interest = amount_to_invest*(1 + (interest_rate/100* no_of_years))
        print(new_amount_with_simple_interest)
        
#compound interest calculation starts here   

    elif interest_type == "compound": 
        new_amount_with_compound_interest = amount_to_invest * math.pow((1 + interest_rate/100), no_of_years)
        print(new_amount_with_compound_interest)
# if user enters anything else other than "bond" or "investment" when asked to enter the type of calculator they want to use
else: 
    print("Invalid entry. Try again")
        

    