# 1. Create an abstract class with abstract and non-abstract methods.
from abc import ABC, abstractmethod
# Abstract Class
class Company(ABC):
    
    # Abstract method
    @abstractmethod
    def First_day(self):
        pass
    
    # Non-abstract method 
    def Last_day(self):
        print("Last day of Employee.")
        
class Employee(Company):
    
    def First_day(self):
        print("First day of Employee")
        
employee = Employee()
employee.First_day()  
employee.Last_day()   

# --------------------------------------------------------------------------------------------------------
# 2. Create a sub class for an abstract class. Create an object in the child class for the abstract 
# class and access the non-abstract methods

# Abstract Class
class Animal(ABC):
    
    # Abstract method
    @abstractmethod
    def sound(self):
        pass
    
    # Non-abstract method
    def sleep(self):
        print("The animal is sleeping.")
        
# Subclass (Child class) of abstract class
class Dog(Animal):
    
    def sound(self):
        print("Dog barks.")

# Subclass (Child class) 0f abstract class
class Cat(Animal):
    
    def sound(self):
        print("Cat meows.")

# Creating an object of the Dog class
dog = Dog()
dog.sound()  
dog.sleep()  

# Creating an object of the Cat class
cat = Cat()
cat.sound()  
cat.sleep()  

# --------------------------------------------------------------------------------------------------------
# 3. Create an instance for the child class in child class and call abstract methods

# Abstract Class
class Animal(ABC):
    
    # Abstract method
    @abstractmethod
    def sound(self):
        pass
    
    # Non-abstract method
    def sleep(self):
        print("The animal is sleeping.")
        
# Subclass (Child class) of abstract class
class Dog(Animal):
    
    def sound(self):
        print("Sound of dog is barks.")
    
    def create_instance_and_call(self): # creating instance for a child class in child class and calling abstract method
        dog_bark = Dog()
        dog_bark.sound()  

dog = Dog()
dog.create_instance_and_call()

# --------------------------------------------------------------------------------------------------------
#4. Create an instance for the child class in child class and call non-abstract methods
# Abstract Class

class Animal(ABC):
    
    # Abstract method
    @abstractmethod
    def sound(self):
        pass
    
    # Non-abstract method
    def sleep(self):
        print("The animal is sleeping.")
        
# Subclass (Child class) of abstract class
class Dog(Animal):
    def sound(self):
        print("Dog barks.")
    
    def sleep(self):
        # Call the non-abstract method from the parent class
        super().sleep()
            
    
    def create_instance_and_call(self): # Creating an instance for the child class in child class and calling non-abstract methods
        dog_work = Dog()
        dog_work.sleep()  

dog = Dog()
dog.sleep()