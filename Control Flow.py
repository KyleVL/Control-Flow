# Developer: Kyle VanLandegent
# Date: 10/11/21
# Program: ATM Transaction

'''
This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our Comparison $ Logical Operators
'''

print("Welcone to Cash-R Us Bank\n\nLet's take a moment to set up your account.\n ")

# Set up an account by asking users for their first and last names using Variables
firstName = input("What is your first name: ")
lastName = input("What is your last name: ")

print("\nWelcome to Cash-R-Us", firstName,lastName + " we will now set up a security PIN on your account.\n")

pin = input("Please choose a 4 digit security pin: ")

print("\nThank you",firstName + ", we see that you set your PIN to",pin)

print("\nWould you like to make a transaction through our automated teller machine.")
atm = input("Yes or No: ").upper()

if atm == "YES":
    print("\n-----------------------------------------------------------------------------------------------------\n")

    # This part of the program will be asking users to complete a transcription through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM",firstName,lastName)

    for i in range (3, 0 , -1):
        userPIN = input("What is your 4 digit PIN: ")
        if userPIN == pin:
            break
        else:
            print("Incorrect - try again!")

    if i == 1:
        print("You have been denied access.")
    else:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # ask users what type of transaction they want withdrawal or deposit
        typeOfTransaction = input(
            "\nWould you like to make a Withdrawal, Deposit, or view your Balance\nW = Withdrawal - D = Deposit - B = Balance: ").lower()
        if typeOfTransaction == "w":
            wAmount = int(input("Enter amount you wish to withdrawl: "))
            balance = balance - wAmount
            print("Your new balance is: $" + str(balance))

        elif typeOfTransaction == "d":
            dAmount = int(input("Enter amount you wish to withdrawl: "))
            balance = balance + dAmount
            print("Your new balance is: $" + str(balance))

        else:
            print("Your current balance is: $" + str(balance))




else:
    print("\nHave a wonderful day" ,firstName, lastName + ", please come back and visit us soon.")