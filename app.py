students = []


def add_student(name, age):
    if age <= 0:
        print("Invalid age. Age must be greater than 0.")
        return

    student = {
        "name": name,
        "age": age
    }

    students.append(student)
    print(f"Student {name} registered successfully.")


add_student("Ahmed", 21)
add_student("John", -5)