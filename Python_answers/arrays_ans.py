# Write a function to add integer values of an array
import numpy as np
def sum_array(arr):
    np_arr = np.array(arr)
    int_arr = np_arr[np_arr.astype(int) == np_arr]
    return np.sum(int_arr)
arr = [1,8,3,7,4,9,2,6]
result = sum_array(arr)
print(result)

# ---------------------------------------------------------------------------------------------------------------------------

# Write a function to calculate the average value of an array of integers
def calculate(arr):
    np_arr = np.array(arr)

    int_arr = np_arr[np_arr.astype(int) == np_arr]
    
    # Calculate and return the average
    if len(int_arr) == 0:
        return 0
    return np.mean(int_arr)

arr = [1,2,3,4,5,6,7,8,9,10]
result = calculate(arr)  
print(result)  

# -----------------------------------------------------------------------------------------------------------------------------

# Write a program to find the index of an array element
def calculate(num):
    sum_num = 0
    #Loop through the array to average value of elements 
    for i in num:
        sum_num = sum_num + i          

    avg = sum_num / len(num)
    return avg

print("The average is", calculate([10,21,32,43,54]))

# --------------------------------------------------------------------------------------------------------------------------
# Write a function to test if array contains a specific value
def find_index(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i  
    return -1  

arr = [10, 20, 30, 40, 50]
element = 30
index = find_index(arr, element)
print(f"Index of {element} is: {index}")  


# -------------------------------------------------------------------------------------------------------------------------
# Write a function to remove a specific element from an array
arr = [1,2,3,4,5]
for num in arr:
    if num == 5:
        print("Specific Value Exist")


# ------------------------------------------------------------------------------------------------------------------------
# Write a function to copy an array to another array
arr = [1,2,3,4,5]
arr.remove(0)
print(arr)


# -----------------------------------------------------------------------------------------------------------------------
# Write a function to insert an element at a specific position in the array
arr = [1,2,3,4,5]
arr1 = []                                             #creating empy array
arr1 = arr.copy()                                     #copying/duplicating arr in arr1
print(arr1)


# -----------------------------------------------------------------------------------------------------------------------
# Write a function to find the minimum and maximum value of an array
arr = [5,1,9,10,4,7,6,3]
def find_min_max(arr):
    if len(arr) == 0:
        return None, None  
    
    return min(arr), max(arr)
min_val, max_val = find_min_max(arr)
print("Minimum:", min_val)  
print("Maximum:", max_val)  


# -----------------------------------------------------------------------------------------------------------------------
# Write a function to reverse an array of integer values
arr = [5,1,9,10,4,7,6,3]
arr.reverse() 
print(arr)


# --------------------------------------------------------------------------------------------------------------------
#  Write a function to find the duplicate values of an array
arr = [44,5,1,9,10,44,7,6,3,9]

for i in range(0,len(arr)):
    for x in range(i + 1,len(arr)):
        if arr[i] == arr[x]:
            print("Duplicate element in given array:",arr[x])


# --------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the common values between two arrays
arr = [44,5,1,9,10,44,7,6,3,9]
arr1 = [5,1,9,10,4,7,6,3]
print("Common values in given arrays:",set(arr).intersection(arr1))


# ---------------------------------------------------------------------------------------------------------------------------------
# Write a method to remove duplicate elements from an array
arr = [44,5,1,9,10,44,7,6,3,9]
arr1 = [] 
for i in arr:
    if i not in arr1:
        arr1.append(i)
print(arr1)


# ----------------------------------------------------------------------------------------------------------------------------------
# Write a method to find the second largest number in an array
arr = [5,1,9,10,44,7,6,3]
arr.sort()
print("Second largest number:",arr[-2]) 


# ------------------------------------------------------------------------------------------------------------------------------
# Write a method to find the second largest number in an array
arr = [1,2,3,4,5,6,7,8,9]
evennumbers = 0
oddnumbers = 0
for i in arr:
    if i % 2 == 0:
        evennumbers += 1
    else:
        oddnumbers += 1 
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)


# ---------------------------------------------------------------------------------------------------------------------------
# Write a method to find number of even number and odd numbers in an array
arr = [10,6,11,13,14]
arr.sort() 
print("Diffrence of largest and smallest value:",arr[-1]-arr[0])


# -----------------------------------------------------------------------------------------------------------------------------
# Write a function to get the difference of largest and smallest value
arr = [1,4,6,12,23,13]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")


# ----------------------------------------------------------------------------------------------------------------------------
# Write a method to verify if the array contains two specified elements(12,23)
arr = [1,4,6,12,23,13]
for i in arr:
    if i == 12:
        print("Exist in array")
    if i == 23:
        print("Exist in array")


# --------------------------------------------------------------------------------------------------------------------------------
# Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    return list(set(arr))

arr = [1, 2, 2, 3, 4, 4, 5, 6, 6]
new_arr = remove_duplicates(arr)
print("Array with duplicates removed:", new_arr)

