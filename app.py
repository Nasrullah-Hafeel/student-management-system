students = []


def add_student(name, age):
    student = {
        "name": name,
        "age": age
    }

    students.append(student)
    print(f"Student {name} added successfully.")


add_student("Ahmed", 21)