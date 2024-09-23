# 1. Write a class with a default constructor, one argument constructor and two argument constructors. 
#    Instantiate the class to call all the constructors of that class from a main class

class MyClass:
    def __init__(self, arg1=None, arg2=None):
        
        # Default constructor
        if arg1 is None and arg2 is None:
            print("Default constructor called")
            
        # One-argument constructor
        elif arg2 is None:
            self.arg1 = arg1
            print(f"One-argument constructor called with arg1={arg1}")
            
        # Two-argument constructor
        else:
            self.arg1 = arg1
            self.arg2 = arg2
            print(f"Two-argument constructor called with arg1={arg1} and arg2={arg2}")

def main():
    # Instantiate MyClass with default constructor
    obj1 = MyClass()
    
    # Instantiate MyClass with one-argument constructor
    obj2 = MyClass(10)
    
    # Instantiate MyClass with two-argument constructor
    obj3 = MyClass(10, 20)

if __name__ == "__main__":
    main()


#------------------------------------------------------------------------------------------------------------
# 2. Call the constructors(both default and argument constructors) of super class from a child class

class ParentClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("ParentClass default constructor called")
        elif arg2 is None:
            self.arg1 = arg1
            print(f"ParentClass one-argument constructor called with arg1={arg1}")
        else:
            self.arg1 = arg1
            self.arg2 = arg2
            print(f"ParentClass two-argument constructor called with arg1={arg1} and arg2={arg2}")

class ChildClass(ParentClass):
    def __init__(self, arg1=None, arg2=None):
        
        if arg1 is None and arg2 is None:
            super().__init__()

        elif arg2 is None:
            super().__init__(arg1)

        else:
            super().__init__(arg1, arg2)
        
        print("ChildClass constructor called")

def main():
    obj1 = ChildClass()
    obj2 = ChildClass(10)
    obj3 = ChildClass(10, 20)

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------------------------------------
# 3. Apply private, public, protected and default access modifiers to the constructor

class AccessModifiersExample:
    # Public variable
    def __init__(self, public_var, protected_var, private_var, default_var):
        # Public: accessible everywhere
        self.public_var = public_var

        # Protected: intended to be used within the class and its subclasses
        self._protected_var = protected_var

        # Private: only accessible within this class
        self.__private_var = private_var

        # Default (public in Python): accessible everywhere
        self.default_var = default_var

    # Public method
    def public_method(self):
        print("Public method")

    # Protected method
    def _protected_method(self):
        print("Protected method")

    # Private method
    def __private_method(self):
        print("Private method")

# Creating an instance of the class
example = AccessModifiersExample(1, 2, 3, 4)

# Accessing public variables and methods
print(example.public_var)  
example.public_method()    

print(example._protected_var) 

print(example._AccessModifiersExample__private_var)  
example._AccessModifiersExample__private_method()    
print(example.default_var)  

#------------------------------------------------------------------------------------------------------------
# 4. Write a program which illustrates the concept of attributes of a constructor.
class Student:
    def __init__(self, name, age, special):
        self.name = name  
        self.age = age    
        self.special = special 

    # Method to display student details
    def display_student_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Special: {self.special}")

student1 = Student("Mrunal", 25, "Data Science")
student2 = Student("Raghav", 24, "Data Analyst")

student1.display_student_info()
print()  
student2.display_student_info()

# Access attributes directly
print(f"\n{student1.name} is special in {student1.special}.")
print(f"{student2.name} is special in {student2.special}.")
