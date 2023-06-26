#The program below is a financial calculator which calculate either an investment or a home loan repayment using user input.

import math

#1 menu options - user can choose either investment or bond 
 
print("=========== MENU OPTIONS ===========")
print("Type 'i' for investment: to calculate the amount of interest you will earn on your investment")
print("Type 'b' for bond: to calculate the amount you will have to pay on a home loan")
print("Type 'q' to quit")

menu_choice = input("\n Choose 'i' for investment or 'b' for bond to proceed: \n ").lower() 

#2 ensure user enter a valid option to proceed

while (menu_choice != 'i' and menu_choice != 'b' and menu_choice != 'q'):
    menu_choice = input("\n You have not enter a valid option. \n Choose 'i' for investment or 'b' to proceed: \n").lower() 


#3 investment selected - calculate simple or compound interest according to user input

if menu_choice == 'i':
    print("=========== INVESTMENT ===========")
    print("*** Enter only numbers ***")
    amount = float(input('Enter the amount of money: '))
    rate = float(input('Enter the interest rate (%): '))
    years = float(input('Enter the number of years: '))
    interest = input("Choose 's' for simple or 'c' for compound interest: ").lower()
    rate = rate / 100
    
    if interest == 's':
        total_invested = amount * (1 + rate * years)
        print(f'The total amount of your investment will be £ {round(total_invested,2)} after {years} years.')
    if interest == 'c':
        total_invested = amount * math.pow((1 + rate), years)
        print(f'The total amount of your investment will be £ {round(total_invested,2)} after {years} years.')

#4 bond selected - calculate amount to be paid on home loan  

elif menu_choice == 'b':
    print("=========== BOND ===========")
    print("*** Enter only numbers ***")
    house_value = float(input('Enter the current house value: '))
    bond_rate = float(input('Enter the interest rate (%): '))/100
    bond_months = int(input('Enter the number of months for the bond repayment: '))
    
    total_repay = (bond_rate * house_value) / (1 - (1 + bond_rate) ** (- bond_months))    
    print(f'The bond repayment will be £ {round(total_repay,2)} for {bond_months} months.')

else:
    print('You quit the system. Thank you')