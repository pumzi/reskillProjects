'''
# Login
    - Ask: account #, password
'''


# Import random numbers
import datetime
import random 

# Using date.today()
todaysDate = datetime.datetime.now()

todaysDate_now = todaysDate.strftime("%b %d, %Y (%H:%M:%S)")

# dictionary
database = {}

def init():
    
    print("Welcome to Bank of Authority. Today is", todaysDate_now)
    
    haveAccount = int(input("Do you have account with us? 1 (yes) or 2 (no)"))

    if(haveAccount == 1):
        login()
    
    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option")
        init()

def login():
    print("**** Login to your account ****")

    accountNumberFromUser = int(input("What is your account number? \n "))
    password = input("What is your password? \n ")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

    print('Invalid account or password')
    login()

    
def register():
    print("****** Register ******")
    
    email = input("What is your email address? ")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    password = input("Create a password: ")
    while True:
        if len(password) > 8:
            password = input("Password should be 8 characters. Create a password: ")
        else:
            print("Thank You!")
            break
    accountNumber = generateAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password]
    
    print("Your account has been created")
    print("=== === ======== ====")
    print("Your account number is: %d" % accountNumber)
    print("Keep it safe.")
    print("=== === ======== ====")

    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user [1]))
    selectedOption = int(input("What would you like to do? (1) Withdrawal (2) Deposit (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        withdrawal()

    elif(selectedOption == 2):
        deposit()
    
    elif(selectedOption == 3):
        logout()
    
    elif(selectedOption == 4):
        exit()
    
    else:
        print("Invalid option")

def withdrawal():
    withdrawal = int(input("How much would you like to withdrawal? "))
    print("Your withdrawal of $%d is completed" % withdrawal)

def deposit():
    deposit = int(input("How much would you like to deposit? "))
    print("Your deposit of $%d is completed " % deposit)

def generateAccountNumber():

    print("Generating Account Number")
    return random.randrange(1111111111, 9999999999)

def logout():
    login()


## Start Banking with Bank of Authority
init()

    