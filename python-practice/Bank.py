"""Imagine you are tasked with developing a simple ATM program. 
Write a program that asks the user to enter the amount they want to withdraw. 
Use a try/except block to handle the ValueError that may occur if the user enters a non-numeric input.
 If a numerical input is provided, check if the withdrawal amount is within the user's account balance. 
 If it is, update the account balance and print a withdrawal successful message. 
If there's a ValueError or if the withdrawal amount exceeds the account balance, print an appropriate error message.
"""

try: 

    account_balance = int(input("What is your account balance? "))
    print("your account balance is:", account_balance)

    try:

        withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

        if withdrawal_amount < account_balance:
            print(withdrawal_amount,"has been withdrawed from your account.")
        
        else:
            print("you cannot withdraw more than your account balance")

    except ValueError:
        print("you can only enter an integer. Try again")

except ValueError:

    print("you can only enter an integer. Try again")