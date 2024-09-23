# 1. Different ways creating a string

My_name = 'Prashant'        # By single quotes
My_name1 = "Prashant"       # By double quotes
My_name2 = """Prashant      
            Kokande"""      # By triple quotes for multiple lines

print(My_name)
print(type(My_name))

print(My_name1)
print(type(My_name1))

print(My_name2)
print(type(My_name2))

#--------------------------------------------------------------------------------
# 2. Concatenating two strings using + operator

string1 = "Prashant"
string2 = "Kokande"
Final = string1 + string2
print(Final)


#--------------------------------------------------------------------------------
#3. Finding the length of the string

string = "Prashant"
len_str = len(string)
print(len_str)


#--------------------------------------------------------------------------------
# 4. Extract a string using Substring

string = "Hello ! Prashant Kokande"
substring = string[7:24]
print(f"Substring of string is {substring}")

#------------------------------------------------------------------------------------
# 5. Searching in strings using index()

string = "Prashant"
search_str = "a"
result = print(string.index(search_str))  #It gives u first occurance index

# another way

string = "Prashant"
search_str = "a"
if search_str in string:
    print(string.index(search_str))
else:
    print("No found")

#------------------------------------------------------------------------------------
# 6. Matching a String Against a Regular Expression With matches()

import re
str = 'Python is an interpreted, object-oriented, high-level programming language'
substr = "obje"
match = re.search(substr, str)

if match:
    print("Match found:", match.group())
else:
    print("No match found")

#-----------------------------------------------------------------------------------

# 7. Comparing strings
str1 = "Prashant"
str2 = "Kokande"
str3 = "Prashant"
# Comparing equal to
if str1 == str2:
    print("Match Found")
elif str1 == str3:
    print("Match Found")
else:
    print("Match not found")

# comparing not equal to
if str1 != str2:
    print("Match not equal")
elif str1 != str3:
    print("Match not equal ")
else:
    print("Match equal")

#------------------------------------------------------------------------------------
# 8. startsWith(), endsWith() and compareTo()
# i) startswith()

string = "Hello, world!"

print(string.startswith("Hello")) 
print(string.startswith("world"))  

# ii) endswitch()
string = "Hello, world!"

print(string.endswith("world!"))  
print(string.endswith("Hello"))  

#iii) compareto()
string1 = "apple"
string2 = "banana"

# In string compare output is given on the basis of alphabetic (first a then b then c)
print(string1 < string2)  
print(string1 > string2)  
print(string1 == string2) 

# Another way

def compare_to(string1, string2):
    if string1 < string2:
        return print("string 1 is less than string 2")
    else:
        return print("string 2 is less than string 1")

result = compare_to("apple", "banana")
print(result)  

#------------------------------------------------------------------------------------
# 9. Trimming strings with strip()

string = "   Hello, World!   "
trimmed_string = string.strip() # Removing leading and trailing whitespace
print(f"'{trimmed_string}'")


string = "123Hello, World!123"
trimmed_string = string.strip('123') # removing specific character
print(f"'{trimmed_string}'")  

#------------------------------------------------------------------------------------
#10. Replacing characters in strings with replace()

string = "Hello, World!"
trimmed_string = string.replace(",", "")
print(trimmed_string)

#------------------------------------------------------------------------------------
# 11. Splitting strings with split()

string = "Hello World !"
words = string.split()
print(words) # output comees in list
print(type(words))

date = "08-Sep-2024"
extend_date = date.split("-")
print(extend_date)

#------------------------------------------------------------------------------------
# 12. Converting integer objects to Strings

number = 123
print(number)
print(type(number))
string = str(number)
print(string)
print(type(string))

#------------------------------------------------------------------------------------
# 13. Converting to uppercase and lowercase

str = "mrunal"
STR = "MRUNAL"
print(str.upper())
print(STR.lower())