# Write a function for arithmetic operators(+,-,*,/)
Value1 = int(input("Enter first number"))
Value2 = int(input("Enter Second number"))

Choice = int(input("Press 1 for Addition, Press 2 for Subtraction, Press 3 for Multiplication, Press 4 for Division"))

def Calculation():
    if Choice == 1:
        res = Value1 + Value2
        print(F"The Addition of {Value1} and {Value2} is ", res)
    elif Choice == 2:
        res = Value1 - Value2
        print(F"The Subtraction of {Value1} and {Value2} is ", res)
    elif Choice == 3:
        res = Value1 * Value2
        print(F"The Multiplication of {Value1} and {Value2} is ", res)
    elif Choice == 4:
        res = Value1 / Value2
        print(F"The Division of {Value1} and {Value2} is ", res)
    else:
        print("Please enter a correct choice")
        
Calculation()

# ----------------------------------------------------------------------------------------------------------------------------------------

# Write a method for increment and decrement operators(++, --)
Value = int(input("Enter a number"))

# For increment
Value += 1
print(f"The Value of increment is {Value}")
# For Decrement
Value -= 1
print(f"The Value of decrement is {Value}")

# ----------------------------------------------------------------------------------------------------------------------------------------

# Write a program to find the two numbers equal or not
first_number = int(input("Enter first number "))
second_number = int(input("Enter second number "))

if first_number == second_number:
    print (f"The {first_number} and {second_number} is equal")
else:
    print (f"The {first_number} and {second_number} is not equal")

# ---------------------------------------------------------------------------------------------------------------------------------------
# Program for relational operators (<,<==, >, >==)
value1 = int(input("Enter first number "))
value2 = int(input("Enter second number "))

# The answers will come in True or False whether which statement comes True.
print (f"{value2} is greater than {value1}", value1 < value2)
print (f"{value2} is greater than or equal to {value1}", value1 <= value2)
print (f"{value1} is greater than {value2}", value1 > value2)
print (f"{value1} is greater than or equal to {value2}", value1 >= value2)
print (f"{value1} is equal to {value2}", value1 == value2)
print (f"{value1} is not equal to {value2}", value1 != value2)

# -------------------------------------------------------------------------------------------------------------------------------------
# Print the smaller and larger number
value1 = int(input("Enter first number"))
value2 = int(input("Enter second number"))

if value1 > value2:
    print(f"{value1} is larger than {value2}")
elif value1 < value2:
    print (f"{value2} is larger than {value1}")
else:
    print("Both Values are equal")
    
    
if value1 < value2:
    print(f"{value1} is smaller than {value2}")
elif value1 > value2:
    print (f"{value2} is smaller than {value1}")
else:
    print("Both Values are equal")
    