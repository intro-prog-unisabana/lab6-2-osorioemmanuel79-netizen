def student_averages(data):
    if not data:
        return {}

    result = {}

    for student, grades in data.items():
        average = sum(grades.values()) / len(grades)
        result[student] = round(average)

    return result


def assignment_averages(data):
    if not data:
        return {}

    result = {}

    assignments = next(iter(data.values())).keys()

    for assignment in assignments:
        total = 0

        for grades in data.values():
            total += grades[assignment]

        average = total / len(data)
        result[assignment] = round(average)

    return result