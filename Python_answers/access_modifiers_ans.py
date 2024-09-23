'''
1. Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. 
Call the private method in main method. Create a sub class and try to access the private fields and methods from sub class.
2. Create a class with PROTECTED fields and methods. Access these fields and methods from any other class in the same package.
Also, Access the PROTECTED fields and methods from child class located in a different package. Access the PROTECTED fields and 
methods from any class in different package
3. Create a class with PUBLIC fields and methods. Access the public methods and fields from any class in the same package
or different package.
'''

# super class
class Super:
     
    # public data member
    name1 = None
 
    # protected data member
    _name2 = None
      
    # private data member
    __name3 = None
     
     # constructor
    def __init__(self, name1, name2, name3): 
        self.name1 = name1
        self._name2 = name2
        self.__name3 = name3
     
    # public member function  
    def displayPublicMembers(self):
  
        # accessing public data members
        print("Public Data Member: ", self.name1)
        
    # protected member function  
    def _displayProtectedMembers(self):
  
        # accessing protected data members
        print("Protected Data Member: ", self._name2)
      
    # private member function  
    def __displayPrivateMembers(self):
  
        # accessing private data members
        print("Private Data Member: ", self.__name3)
    # public member function
    def accessPrivateMembers(self):    
           
        # accessing private member function
        self.__displayPrivateMembers()
  
# derived class
class Sub(Super):
  
    # constructor
    def __init__(self, name1, name2, name3):
            Super.__init__(self, name1, name2, name3)
           
    # public member function
    def accessProtectedMembers(self):
        # accessing protected member functions of super class
        self._displayProtectedMembers()
  
# creating objects of the derived class    
object = Sub("Mrunal", "Kulkarni" , "Pune")
 
# calling public member functions of the class
object.displayPublicMembers()
object.accessProtectedMembers()
object.accessPrivateMembers()
 
# Object can access protected member
print("Object is accessing protected member:", object._name2)