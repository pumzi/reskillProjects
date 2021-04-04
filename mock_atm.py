import datetime

# Using date.today()
todaysDate = datetime.datetime.now()

todaysDate_now = todaysDate.strftime("%m/%d/%Y, %H:%M:%S")

name = input("What is your name? \n")

allowedUsers = ["Gilligan", "Ginger", "Maryann"]
allowedPasswords = ["skipper", "Skipper", "Professor"]
currentBalance = 1000

if(name in allowedUsers):
    password = input("What is your password? \n")
    userID = allowedUsers.index(name)

    while True:

        if(password == allowedPasswords[userID]):
            print("Welcome! Today is", todaysDate_now)
            print("These are the available options: \n")
            print ("1. Withdrawal \n")
            print('2. Deposit \n')
            print('3. Complaint \n')
            
            selectedOption = int(input("Please select an option: "))
            
            print(selectedOption)
                
            if(selectedOption == 1):
                print("You selected %s" % selectedOption)
                withdrawal = int(input("How much would you like to withdrawal? "))
                print("Take your cash: $%s" % withdrawal)
                
            elif(selectedOption == 2):
                print("You selected %s" % selectedOption)
                deposit = int(input("How much would you like to deposit? \n "))
                print(deposit)
                newBalance = int(currentBalance + deposit)
                print("Your new balance is: %s" % newBalance)

            elif(selectedOption == 3):
                    print("You selected %s" % selectedOption)
                    complaint = input("What issue will you like to report? \n ") 
                    print("Thank you for contacting us")

            else:
                    print("Invalid Option. Please try again!")

        else:
            print('Password is incorrect, please try again')
            break

else:
    print('Name not found, please try again')

