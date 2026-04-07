def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    
    name = input("Enter student name:\n").title()

    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n")

        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")

        subject = subject.strip().title()
        grade = float(grade.strip())

        subjects[subject] = grade

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")

    return student_grades