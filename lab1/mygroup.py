groupmates = [
    {
        "name": "Павел",
        "surname": "Черниговский",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Александр",
        "surname": "Шаловасов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Серафим",
        "surname": "Сухарев",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Павел",
        "surname": "Овчинников",
        "exams": ["АиГ", "ИС", "ЭЭиС"],
        "marks": [5, 4, 5]
    },
        {
        "name": "Егор",
        "surname": "Алексанов",
        "exams": ["Web", "Информатика", "Философия"],
        "marks": [5, 5, 3]
    }
]

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(20), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), 
              student["surname"].ljust(20), 
              str(student["exams"]).ljust(30), 
              str(student["marks"]).ljust(20))

def filter_students_by_avg(students, min_avg):
    return [
        student for student in students
        if sum(student["marks"]) / len(student["marks"]) > min_avg
    ]

if __name__ == "__main__":
    threshold = float(input("Введите минимальный средний балл: "))
    filtered = filter_students_by_avg(groupmates, threshold)
    
    if filtered:
        print("\nСтуденты со средним баллом выше", threshold, ":")
        print_students(filtered)
    else:
        print("Нет студентов со средним баллом выше", threshold)
