#Function Declarations
'''
Function to get and validate float values
Input:
Output: a validated float value
'''
def get_float_value(prompt):
    run_again = True
    while (run_again):
        try:
            user_input = float(input(prompt))
            if(user_input <= 0):
                print("ERROR: Value must be greater than 0.\n")
                continue
        except:
            print("ERROR: Input must be a number.\n")
        else:
            run_again = False
    
    return user_input

#INPUT
#Declare variables for known values
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6
#prompt the user to enter the amount of wall to paint
#Convert to float
#if error in input ask user to re-enter input. Input must be greater than 0
wall_area = get_float_value("What is the area of wall in sq/ft: ")

#prompt user to enter cost of paint per gallon
paint_price = get_float_value("What is the price of paint per gallon: ")


#PROCESS
#Calculate to hours of labor
#Calculate the cost of labor
#Calculate the amount of paint
#Calculate the cost of the paint
#Calculate total cost of the job

#OUTPUT
#Print hours of labor, cost of labor, amount of paint, 
#cost of paint, total job cost