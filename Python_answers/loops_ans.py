#  Write a program to print “Bright IT Career” ten times using for loop
name = "Bright IT Career"
for i in range(10):
    print(name)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Write a java program to print 1 to 20 numbers using the while loop
num = 1
while num <= 20:
    print(num)
    num += 1

# ---------------------------------------------------------------------------------------------------------------------------------------

# Program to equal operator and not equal operators
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

if num1 == num2:
    print (f"{num1} == {num2}: {num1 == num2}")
else:
    print(f"{num1} != {num2}: {num1 != num2}")

# --------------------------------------------------------------------------------------------------------------------------------------
# Write a program to print the odd and even numbers

value = int(input("Enter your number "))

def evenodd():
    if value%2 == 0:
        print("Given number is even: ")
    else:
        print("Given number is odd: ")
evenodd()

# -------------------------------------------------------------------------------------------------------------------------------------
# Write a program to print largest number among three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b & a > c:
    print (f"{a} is the largest number")
elif b > a & b > c:
    print (f"{b} is the largest number")    
else:
    print(f"{c} is the largest number")

# ------------------------------------------------------------------------------------------------------------------------------------
# Write a program to print even number between 10 and 20 using while

a = 10
b = 20
print("Even Numbers Between 10 to 20: ",end=" ")
while a <= b:
    if(a % 2 == 0):
        print("{0}".format(a),end=" ")
    a = a + 1
print()

# -----------------------------------------------------------------------------------------------------------------------------------
# Write a program to print 1 to 10 using the do-while loop statement

i = 1

while True:  
    print(i)
    i += 1
    
    if i > 10:  
        break

# ------------------------------------------------------------------------------------------------------------------------------------
# Write a program to find Armstrong number or not

a = int(input('Enter a number '))
sum = 0
temp = 0
temp = a
while temp > 0:
    r = temp % 10
    sum += r ** 3
    temp //= 10
if a == sum:
    print(a," is an amstrong number")
else:
    print(a," is not an amstrong number")

# -----------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the prime or not

number = int(input("Enter any number to check prime number or not: "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")

# --------------------------------------------------------------------------------------------------------------------------------------
# Write a program to palindrome or not

n = int(input("Enter number to check palindrome or not:"))
temp = n
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if(temp == rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!") 

# -------------------------------------------------------------------------------------------------------------------------------------
# Program to check whether a number is EVEN or ODD using switch

# Python program don't have switch inbuilt function 

# ------------------------------------------------------------------------------------------------------------------------------------
# Print gender (Male/Female) program according to given M/F using switch
gender = input("Enter your gender ")
if gender not in ['M', 'F', 'm', 'f']:
    print("Given input is not correct")
else:
    if gender in ['M', 'm']:
        print("Your gender is Male")
    else:
        print("Your gender is Female")

