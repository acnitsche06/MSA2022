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
        print("Good job you followed directions")
        break

#If user chose 1, ask for username and password; and check username and password combination in the users.txt file
if user_option == "1":
    while True:
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")
        #Open the users files
        user_file = open("users.txt", "r")
        user_found = False
        for line in user_file:
            credentials = line.split(", ")
            #Check if username and password are valid
            if user_name == credentials[0] and user_pass == credentials[1].rstrip():
                #If valid, write to users.txt file and move on to prompt for student data
                user_found = True
                break

        if user_found:
            print(f"User {user_name} successfully logged in!\n")
            break
        #If not valid reprompt the user
        else:
            print(f"User {user_name} not found!\n")


#If user chose 2, ask for username and password; and validate username and password length.
#-If valid, write to users.txt file and move on
#If not vaild reprompt user

#Ask user how many students to enter data for
#Prompt user to enter student name and number score
#Store data somewhere
#Convert the number score to a letter grade


#Print student data(name, score, grade)
#Calculate and print class average