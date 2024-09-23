# 1. Write two methods with the same name but different number of parameters of same type and call the methods

class Name:
    # Method with different numbers of parameters using default arguments
    def display(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a} {b}")

name = Name()
name.display("Mrunal")
name.display("Mrunal", "Kulkarni") 

#-------------------------------------------------------------------------------------------------------------------
# 2. Write two methods with the same name but different number of parameters of different data type and call the methods

class Name:
    # Method with different numbers of parameters using default arguments
    def display(self, a, b=None):
        if b is None:
            print(f"Single parameter: {a}")
        else:
            print(f"Two parameters: {a} {b}")

name = Name()
name.display("Mrunal")
name.display("Mrunal", 25) 

