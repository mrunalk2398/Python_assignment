# 1. Write a program to read text file
file_path = (r'C:\Users\HP\Desktop\Python Assignment\Answers\11.Files.txt')

with open(file_path, 'r') as file:
        content = file.read()
        print(content)
        
# 2. Write a program to write text to .txt file using InputStream
def write_to_file():
    text = input("Enter the text to write to the file: ")
    
    file_path = (r'C:\Users\HP\Desktop\Python Assignment\Answers\11.Files.txt')
    
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Write the user input to the file
        file.write(text)
    
    print(f"Text has been written to {file_path}")

# Call the function
write_to_file()