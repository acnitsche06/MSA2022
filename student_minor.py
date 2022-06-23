#Print the menu
print("Select option from menu\n__________________________")
print("1. Login")
print("2. Create User")

#Prompt and get the option the user selected
while True:
    user_option = input("Would you like to (1) Login or (2) Create an Account? ")
    #Ensure the user entered a valid option, if not, prompt the user again
    if user_option != '1' and user_option != '2':
        print("\nERROR: Enter a 1 or 2")
        continue
    else:
        print("YAY")
        break
#If user chose 1, ask for username and password; and check username and password combination in the users.txt file
#- If not valid combination reprompt the user. If valid then move on to prompt for student data
#If user chose 2, ask for username and password; and validate username and password length.
#-If valid, write to users.txt file and move on
#If not vaild reprompt user

#Ask user how many students to enter data for
#Prompt user to enter student name and number score
#Store data somewhere
#Convert the number score to a letter grade


#Print student data(name, score, grade)
#Calculate and print class average