import math

print("*** Welcome to the Online Banking Application ***")
def sign_in():
    global name
    global pin
    global c_balance
    name = str(input("Please create your user name "))
    pin = str(input("Please create your 4 digit PIN "))
    if len(pin) == 4:
        pin = pin
    else:
        print("The PIN has to be 4 digits.")
        new_pin = str(input("Please create your 4 digit PIN "))
        if len(new_pin) != 4:
            print("The PIN has to be 4 digits")
            sign_in()
        else:
            pin = new_pin
    print("Your account is successfully created!")    

def forgot_pin():
    print("Forgot PIN")
    recover_pin = str(input("Please create your new 4 digit PIN "))
    if len(recover_pin) != 4:
        print("The PIN has to be 4 digits")
        forgot_pin()
    else:
        print("New PIN restored successfully, Please login!")
        pin = recover_pin
        login()

def deposit_interest(p, r, t):
    # A = Pe^(rt) ... formula for calculating compound interest
    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    # Calculations
    a = p * e
    return a

def login():
    # name1 represents username
    # pin1 represents user's pin
    name1 = str(input("Please enter your username "))
    pin1 = str(input("Please enter your PIN "))
    # check if the name and pin matched
    if name1 == name and pin1 == pin:
        print("Welcome to the Online Banking Application" + " " + name)
        print("Please choose from the Menu below")
        list_menu = ["1-Deposit", "2-Withdrawal", "3-Transfer", "4-Check Balance", "5-Deposit Interest", "6-Calculate Compound Interest"]
        for l in list_menu:
            print(l)
        choice = int(input("Please select an option"))
        # initialize
        deposit = 0
        withdrawal = 0
        c_balance = 0

        # deposit
        if choice == 1:
           deposit = float(input("Enter amount to deposit "))
           c_balance = deposit
           print("Your current balance is"+" "+str(c_balance))

        # withdraw
        elif choice == 2:
            withdrawal = int(input("Enter amount to withdraw"))
            if withdrawal > c_balance:
                print("You have insufficient funds for this transactions")
                login()
            else:
                c_balance = deposit - withdrawal
                print(str(withdrawal) +" "+ "has been withdrawn from your account" +" "+ " and your current balance is"
                      +" "+ str(c_balance))

        # transfer
        elif choice == 3:
            destination_acc = str(input("Enter receiver's 13 digit account number"))
            if len(destination_acc) == 13:
                transfer_amount = int(input("Enter the amount of money to be transferred"))
                if transfer_amount > c_balance:
                    print("Insufficient funds/ account balance")
                    login()
                else:
                    c_balance = deposit - transfer_amount
                    print("The transaction of " + " " + str(transfer_amount) + " " + "to"+ str(destination_acc) +
                          " is successful." + " and your new current balance is" + str(c_balance))
            else:
                print("Destination account is invalid!")
                login()

        # check current balance
        elif choice == 4:
            print("Your current balance is" +" "+ str(c_balance))

        # interest rate
        elif choice == 5:
            if deposit > 50000:
                rate = 3
            elif deposit > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Your current deposit interest rate is" +" "+ str(rate) + " %")

        # calculate compound interest
        elif choice == 6:
            list_options = ["1-Calculate Interest based on your current balance", "2-Calculate Interest based on a deposit input"]
            for m in list_options:
                print(m)
            choice_2 = int(input("Please select an option")) # based on amount of cash in DB
            if choice_2 == 1:
                timing = str(input("How many years do you wish to invest your funds?"))
                if deposit > 50000:
                    rate_x = 3/100
                elif deposit > 30000:
                    rate_x = 2/100
                else:
                    rate_x = 1.5/100
                print("Your current balance in" + " " + "timing" + " " + "years will be")
                print(deposit_interest(c_balance, rate_x, timing))
            elif choice_2 == 2: # simulation value
                timing_2 = str(input("How many years do you wish to invest you funds?"))
                funds = str(input("Enter the amount of funds you wish to deposit"))
                funds = int(funds)
                if deposit > 50000:
                    rate_x = 3/100
                elif deposit > 30000:
                    rate_x = 2/100
                else:
                    rate_x = 1.5/100
                print("Your current balance in" + " " + "timing" + " " + "years will be")
                print(deposit_interest(funds, rate_x, timing_2))
        else:
            print("Oops! Option not available ")
            login()

    else:
        print("Username or PIN is incorrect; do you have an account ?!")
        # list of options
        list1 = ["1-Yes", "2-No"]
        for i in list1:
            print(i)
        inp = int(input("Select an option"))
        if inp == 1:
            list2 = ["1-Do you want to login again?", "2-You forgot your PIN"]
            for j in list2:
                print(j)
            response = str(input("Select an option"))
            response = int(response)
            if response == 1:
                login()
            elif response == 2:
                forgot_pin()
            else:
                print("Option not available")
                login()
        elif inp == 2:
            print("Please create your account")
            sign_in()
    exit()

def main_menu():
    options_2 = int(input("Choose 1 to Sign In or 2  to Login"))
    if options_2 == 1:
        sign_in()
    elif options_2 ==2:
        login()
    else:
        print("Oops! Option not available!")
        main_menu()
    exit()

def exit():
    option_3 = str(input("Do you wish to conduct any transaction? Yes(y) or No(n)"))
    if option_3.lower() == "y":
        login()
    elif option_3.lower() == "n":
        print("Thank you for using BSS App.")
    else:
        print("Oops! Option not available")
        main_menu()

main_menu()