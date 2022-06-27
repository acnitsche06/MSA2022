#student_minor
#Print the menu
import numbers
from turtle import st


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
        print("Good job you followed directions\n")
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

#If user chose 2, ask for username and password
elif user_option == "2":
    run_again = True
    while(run_again):
        user_name = input("Please enter your username (4-12 characters): ")
        user_pass = input("Please enter your password (6-16 characters): ")

        #Validate length of username and passowrord
        username_length = len(user_name)
        password_length = len(user_pass)

        #If valid, write to users.txt file and move on
        if(username_length >=4 and username_length <= 12 and password_length >=6 and password_length <= 16):
            user_file = open("users.txt", "a")
            user_file.write(f"{user_name}, {user_pass}\n")
            user_file.close()
            print("\nAccount successfully created")
            run_again = False

        #If not vaild reprompt user
        else:
            print("ERROR: Incorrect password and/or user name length\n")
            continue

print("Ask user for student data")
#Create 3 empty list for student name, scores, and letter grades
student_names = []
student_scores = []
student_letter_grades = []

#Ask user how many students to enter data for
num_of_students = int(input("Enter number of students to enter grades for: "))
for counter in range(num_of_students):
    #Prompt user to enter student name and number score
    student_name = input("Enter student name: ")
    student_score = float(input("Enter student score: "))
    print("\n______________")
    
    #Store data in lists
    student_names.append(student_name)
    student_scores.append(student_score)

    #Convert the number score to a letter grade and store in the letter grade list
    #use an if and elif and else statement
    if student_score > 100:
        student_letter_grades.append("A++")
    elif student_score >= 89.5 and student_score <= 100:
        student_letter_grades.append("A")
    elif student_score >= 79.5 and student_score < 89.5:
        student_letter_grades.append("B")
    elif student_score >= 69.5 and student_score < 79.5:
        student_letter_grades.append("C")
    elif student_score >= 59.5 and student_score < 69.5:
        student_letter_grades.append("D")
    else:
        student_letter_grades.append("F")

#Print student data(name, score, grade)
class_total = 0
index = 0
for counter in range(num_of_students):
    print(f"{student_names[index]}: {student_scores[index]}: {student_letter_grades[index]}")
    class_total = class_total + student_scores[index]
    index = index + 1

#Calculate and print class average
amount_students = len(num_of_students)
class_average = class_total / amount_students
print(f"Your class average is: {class_average}")