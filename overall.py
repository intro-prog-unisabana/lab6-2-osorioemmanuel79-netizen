def student_averages(data):
    result = {}

    for student, grades in data.items():
        average = sum(grades.values()) / len(grades)
        result[student] = round(average)

    return result


def assignment_averages(data):
    result = {}

    # Obtener las tareas (hw1, hw2, etc.)
    assignments = next(iter(data.values())).keys()

    for assignment in assignments:
        total = 0

        for grades in data.values():
            total += grades[assignment]

        average = total / len(data)
        result[assignment] = round(average)

    return result