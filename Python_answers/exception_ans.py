# 1. Generate Arithmetic Exception without exception handling
def arithmetic_exception():
    result = 10 / 0  # This will raise ZeroDivisionError
    print(result)

# Uncomment to test the exception
# arithmetic_exception()

# ---------------------------------------------------------------------------------------------------------------------
# 2. Handle Arithmetic Exception using try-except block
def handle_arithmetic_exception():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught a division by zero error!")

handle_arithmetic_exception()


#----------------------------------------------------------------------------------------------------------------------
# 3. Method that throws exception, called without try block
def throw_exception():
    raise ValueError("This is a custom exception!")

# Uncomment to test throwing an exception without try block
# throw_exception()

#----------------------------------------------------------------------------------------------------------------------
# 4. Program with multiple catch blocks (except blocks)
def multiple_exceptions_handling():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError!")
    except TypeError:
        print("Caught a TypeError!")
    except Exception as e:
        print(f"Caught a generic exception: {str(e)}")

multiple_exceptions_handling()


# 5. Program to throw exception with your own message
def throw_custom_exception():
    raise Exception("This is my custom error message!")

# Uncomment to test the custom exception
# throw_custom_exception()

#----------------------------------------------------------------------------------------------------------------------
# 6. Program to create your own exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Raise the custom exception
def raise_custom_exception():
    raise MyCustomException("This is a custom exception!")

# Uncomment to test custom exception
# raise_custom_exception()

#----------------------------------------------------------------------------------------------------------------------
# 7. Program with finally block
def program_with_finally():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError.")
    finally:
        print("This block always executes, whether an error occurs or not.")

program_with_finally()


# 8. Generate Arithmetic Exception
def generate_arithmetic_exception():
    result = 1 / 0  # This will raise ZeroDivisionError
    print(result)

# Uncomment to test
# generate_arithmetic_exception()

#----------------------------------------------------------------------------------------------------------------------
# 9. Generate FileNotFoundException
def generate_file_not_found_exception():
    try:
        with open('non_existent_file.txt', 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print("File not found exception caught!")

generate_file_not_found_exception()


#----------------------------------------------------------------------------------------------------------------------
# 10. Generate ClassNotFoundException (ModuleNotFoundError in Python)
def generate_module_not_found_exception():
    try:
        import non_existent_module
    except ModuleNotFoundError:
        print("Module not found exception caught!")

generate_module_not_found_exception()


#----------------------------------------------------------------------------------------------------------------------
# 11. Generate IOException (using OSError)
def generate_io_exception():
    try:
        with open('/invalid/path/to/file.txt', 'r') as file:
            data = file.read()
    except OSError:
        print("IO exception (OSError) caught!")

generate_io_exception()

#----------------------------------------------------------------------------------------------------------------------
# 12. Generate NoSuchFieldException (AttributeError in Python)
class MyClass:
    def __init__(self):
        self.name = "Example"

def generate_no_such_field_exception():
    obj = MyClass()
    try:
        print(obj.age)  # `age` doesn't exist
    except AttributeError:
        print("No such field exception (AttributeError) caught!")

generate_no_such_field_exception()
