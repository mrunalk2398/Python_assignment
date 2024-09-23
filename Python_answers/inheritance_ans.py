# 7. Inheritance
''' A, B and C are classes. A is a super class. B is a sub class of A. C is a sub class of B. Create three methods in each class,
2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C.
Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class 
using its own object/instance. Call an overridden method with super class reference to B and C class’s objects
Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members '''
class A:
    def method(self):
        print("Method from Class A")
    
class B(A):
    def method(self):
        print("Method from Class B")
    def method1(self):
        print("A reference of B")
    
class C(B):
    def method(self):
        print("Method from Class C")
    def method1(self):
        print("A reference of C")
    
# Main method
def main():
    # Creating instances of each class
    a = A()
    b = B()
    c = C()

    # Calling methods of each class using its own object
    print("Class A method:")
    a.method()
        
    print("\nClass B method:")
    b.method()
        
    print("\nClass C method:")
    c.method()
        
    # Calling method with superclass references
    print("\nCalling method with superclass references:")
    a_reference_b = B()
    a_reference_b.method1()  

    a_reference_c = C()
    a_reference_c.method1()  

if __name__ == "__main__":
    main()