# 10.Packages
# 1. Create a program to create two class.
# 1.1. Create a constructor and a method for each class
# 1.2. Create a __init__.py for adding all packages
# 1.3. Import the respective packages
# 1.4. Call each class by creating an object to it
# 1.5. Create a program by all the above


from my_package import class_one, class_two

# Create objects for both classes
object_one = class_one("Alice")
object_two = class_two("Bob")

# Call methods on both objects
print(object_one.greet())
print(object_two.greet())