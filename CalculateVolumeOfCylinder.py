import math

def float_value(prompt):
    run_again = True
    while(run_again):
        try:
            user_input = float(input(prompt))
            if user_input <= 0:
                continue
        except:
            print("ERROR: Value must be greater than 0")
        else:
            run_again = False
    return user_input


#Declare variables / INPUT
cylinder_radius = float_value("Enter the radius of your Cylinder: ")
cylinder_height = float_value("Enter the height of your Cylinder: ")

#Declare variables / OUTPUT
volume = math.pi * cylinder_radius * 2 * cylinder_height
print(f"Your volume is: {volume}")
