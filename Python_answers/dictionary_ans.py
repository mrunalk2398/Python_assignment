# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
'''
students = {
    1: "Prashant",
    2: "Aakash",
    3: "Gaurav",
    4: "Rohit",
    5: "Vishal"
}
'''

#print("Student ID and Name Dictionary:")
#for student_id, name in students.items():
#    print(f"ID: {student_id}, Name: {name}")


# 1.1. Adding the values in dictionary
# students[6] = "Kunal"

# 1.2. Updating the values in dictionary
# students[6] = "Vaibhav"

# 1.3. Accessing the value in dictionary
# student_names = students.values()  # Convert view object to a list for printing
# print("Student names:", student_names)

# 1.4. Create a nested loop dictionary

students = {
    1: {
        "name": "Mrunal",
        "age": 22,
        "grades": {
            "math": 85,
            "science": 90,
            "english": 88
        }
    },
    2: {
        "name": "Mrunmayee",
        "age": 23,
        "grades": {
            "math": 78,
            "science": 84,
            "english": 80
        }
    },
    3: {
        "name": "Rutuja",
        "age": 21,
        "grades": {
            "math": 92,
            "science": 89,
            "english": 91
        }
    },
    4: {
        "name": "Shital",
        "age": 24,
        "grades": {
            "math": 75,
            "science": 80,
            "english": 70
        }
    },
    5: {
        "name": "Madhura",
        "age": 22,
        "grades": {
            "math": 88,
            "science": 92,
            "english": 85
        }
    }
}

for student_id, info in students.items():
    print(f"Student ID: {student_id}")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print("  Grades:")
    for subject, grade in info['grades'].items():
        print(f"    {subject}: {grade}")
    print()  

# 1.5. Access the values of nested loop dictionary

student_id = 1
name = students[student_id]["name"]
print(f"Name of student with ID {student_id}: {name}")

# 1.6. Print the keys present in a particular dictionary
students = {
    1: "Mrunal",
    2: "Mrunmayee",
    3: "Rutuja",
    4: "Shital",
    5: "Madhura"
}

for student_id in students.keys():
    print(f"The keys are in Dictionary : {student_id}")
    
# 1.7. Delete a value from a dictionary
del students[5]
print(f"In students dictionary, No. 5 is deleted {students}")