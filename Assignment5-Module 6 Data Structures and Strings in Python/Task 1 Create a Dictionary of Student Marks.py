details = {
    "Alice": 50,
    "Mohan": 80,
    "Sohan": 75
}

student = input("Enter the student's name: ")
try:
    marks = details[student]
    print(f"{student}'s marks: {marks}")
except KeyError as e:
    print ("Student not found.")

    