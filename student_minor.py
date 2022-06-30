#student_minor

def print_main_menu():
    #Print the Menu
    print("Select option from menu\n__________________________")
    print("1. Login")
    print("2. Create User")
    return

def get_user_option():
    while True:
        user_option = input("Would you like to (1) Login or (2) Create an Account? ")
        #Ensure the user entered a valid option, if not, prompt the user again
        if user_option != '1' and user_option != '2':
            print("\nERROR: Enter a 1 or 2")
            continue
        else:
            print("Good job you followed directions\n")
            break
    return user_option

def login_user():
    while True:
        user_name = input("Please enter your user name: ")
        user_pass = input("Please enter your password: ")

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

    return

#If clicked 2 create new user
def create_user():
    while True:
        user_name = get_valid_username_or_password("Please enter your username (4-12 characters): ", 4, 12)
        user_pass = get_valid_username_or_password("Please enter your password (6-16 characters): ", 6, 16)

        #Write username and password to file
        try:
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
        except:
            print("Error creating user.\n")
            continue
        else:
            print(f"User: {user_name} created")
        finally:
            user_file.close()
            break
    return
        

def get_valid_username_or_password(prompt, min_length, max_length):
    while True:
        user_input = input(prompt)
        input_length = len(user_input)

        if(input_length >= min_length and input_length <= max_length):
            break

        #If not vaild reprompt user
        else:
            print("ERROR: Input Length invalid.\n")
        
    return user_input

def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input < 1:
                print("ERROR: Input must be greater than or equal to 1.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            break
    return user_input

def get_letter_grade(score):
    #Convert the number score to a letter grade and store in the letter grade list
    #use an if and elif and else statement
    if score > 100:
        return "A++"
    elif score >= 89.5 and score <= 100:
        return "A"
    elif score >= 79.5 and score < 89.5:
        return "B"
    elif score >= 69.5 and score < 79.5:
        return "C"
    elif score >= 59.5 and score < 69.5:
        return "D"
    else:
        return "F"

def load_students_scores_and_grades(num_of_students):
    student_names, scores_list, letter_grades = [], [], []
    for counter in range(num_of_students):
        #Prompt user to enter student name and number score and make sure it is a number
        student_name = input("Enter student name: ")

        while True:
            try:
                student_score = float(input("Enter student score: "))
                if student_score < 0:
                    print("ERROR: Input can't be a negative number\n")
                    continue
            except:
                print("ERROR: Input must be a number\n")
            else:
                break

        print("\n___________________")
        
        #Store data in lists
        student_names.append(student_name)
        scores_list.append(student_score)
        letter_grades.append(get_letter_grade(student_score))
    return student_names, scores_list, letter_grades

def main():
    print_main_menu()
    #Prompt and get the option the user selected
    user_option = get_user_option()

    #If user chose 1, ask for username and password; and check username and password combination in the users.txt file
    if user_option == '1':
        login_user()


    #If user chose 2, ask for username and password
    elif user_option == '2':
        create_user()

    #Ask user how many students to enter data for
    num_of_students = get_integer_input("Enter number of students to enter grades for: ")
    student_names, student_scores, student_letter_grades = load_students_scores_and_grades(num_of_students)

    #Print student data(name, score, grade)
    class_total = 0
    index = 0
    for counter in range(num_of_students):
        print(f"{student_names[index]}: {student_scores[index]}: {student_letter_grades[index]}")
        class_total = class_total + student_scores[index]
        index = index + 1

    print("\n____________________________")
    #Calculate and print class average
    amount_students = len(student_scores)
    class_average = class_total / amount_students
    print(f"Your class average is: {class_average}")

main()