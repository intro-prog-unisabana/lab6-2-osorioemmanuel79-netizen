# Diccionario principal
students = {
    "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
    "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
    "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}


def student_averages(data):
    result = {}

    for student, grades in data.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result


def assignment_averages(data):
    result = {}

    # Obtener todas las tareas desde el primer estudiante
    assignments = list(next(iter(data.values())).keys())

    for assignment in assignments:
        total = 0
        count = 0

        for grades in data.values():
            total += grades[assignment]
            count += 1

        result[assignment] = round(total / count)

    return result