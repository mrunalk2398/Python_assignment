# # 1. Define a static variable and access that through a class

class My_Class:
    static_var = 10
print("Accessing static variable through class:", My_Class.static_var)

#---------------------------------------------------------------------------------------------------------------------------
# 2. Define a static variable and access that through a instance

class My_Class:
    static_var = 10

my_class = My_Class()
print("Accessing static variable through instance:", my_class.static_var)

#---------------------------------------------------------------------------------------------------------------------------
# 3. Define a static variable and change within the instance

class My_Class:
    static_var = 10

my_class = My_Class()
my_class.static_var = 15
print(my_class.static_var) 

#---------------------------------------------------------------------------------------------------------------------------
# 4. Define a static variable and change within the class

class My_Class:
    static_var = 10

my_class = My_Class()
my_class.static_var = 15  # This creates an instance variable
print(my_class.static_var) # (instance variable)
print(My_Class.static_var) # (class-level static variable)