submissions = [("anna", "lab_01", 5), ("boris", "lab_01", 4), ("anna", "lab_02", 5), ("daria", "lab_01", 3), ("boris", "lab_02", 5), ("anna", "lab_01", 4)]

#1)Множество студентов
students = {name for name, lab, score in submissions}
print(students)

#2)Множество лабораторных работ
labs = {lab for name, lab, score in submissions}
print(labs)

#3)Попытки студентов
attempts = {}
for name, lab, score in submissions:
    if name not in attempts:
        attempts[name] = []
    attempts[name].append([lab, score])
print(attempts)

#4)Словарь лучших результатов
best = {}
for name, lab, score in submissions:
    key = (name, lab)
    best[key] = max(best.get(key, score), score)
print(best)

#5)Словарь количества попыток
attempts_count = {}
for name, lab, score in submissions:
    key = (name, lab)
    attempts_count[key] = attempts_count.get(key, 0) + 1
print(attempts_count)

students_lab_01 = {name for name, lab, score in submissions if lab == "lab_01"}
students_lab_02 = {name for name, lab, score in submissions if lab == "lab_02"}
students_both = students_lab_01 & students_lab_02
print(students_both)


new_submission = ("daria", "lab_02", 4)
submissions.append(new_submission)

name, lab, score =  new_submission

students.add(name)

labs.add(lab)

if name in attempts:
    attempts[name].append((lab, score))
else:
    attempts[name] = [(lab, score)]

if (name, lab) in best:
    if score > best[(name, lab)]:
        best[(name, lab)] = score
else:
    best[(name, lab)] = score

if (name, lab) in attempts_count:
    attempts_count[(name, lab)] += 1
else:
    attempts_count[(name, lab)] = 1

students_lab_01 = {name for name, lab, score in submissions if lab == "lab_01"}
students_lab_02 = {name for name, lab, score in submissions if lab == "lab_02"}
students_both = students_lab_01 & students_lab_02
print(students_both)

print('========================================')

print(students)
print(labs)
print(attempts)
print(best)
print(attempts_count)
print(students_both)


print('========================================')

#Практическая часть
def request(insert_data):
    parts = insert_data.strip().split()
    if not parts:
        return "Пустой запрос"

    cmd = parts[0]
    args = parts[1:]

    match cmd, args:
        case "student", [name]:
            if name in attempts:
                return attempts[name]
            return f"Студент '{name}' не найден"

        case "best", [name, lab]:
            key = (name, lab)
            if key in best:
                return best[key]
            return f"Нет данных о сдаче '{lab}' студентом '{name}'"

        case "attempts", [name, lab]:
            key = (name, lab)
            return attempts_count.get(key, 0)

        case "completed", [lab]:
            # Находим всех студентов, сдававших указанную работу
            students_for_lab = {
                student for (student, l) in best if l == lab
            }
            if students_for_lab:
                return students_for_lab
            return f"Лабораторная работа '{lab}' не найдена или никем не сдавалась"

        case _:
            return f"Неизвестная команда или неверное количество аргументов: '{insert_data}'"


sp = [
    "student anna",
    "best anna lab_01",
    "attempts boris lab_02",
    "completed lab_01",
    "student ivan",             # отсутствующий студент
    "best anna lab_03",         # отсутствующая работа
    "attempts ivan lab_01",     # студент без попыток
    "completed lab_99",         # неизвестная лабораторная
    "best anna",                # неверное число параметров
]

for q in sp:
    print(q)
    print(request(q))
    print('----')
