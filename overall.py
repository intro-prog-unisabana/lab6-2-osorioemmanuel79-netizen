def student_averages(data):
    result = {}

    for student, grades in data.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result


def assignment_averages(data):
    result = {}

    # Obtener todas las tareas
    assignments = next(iter(data.values())).keys()

    for assignment in assignments:
        total = 0

        for grades in data.values():
            total += grades[assignment]

        avg = total / len(data)
        result[assignment] = round(avg)

    return result
input()