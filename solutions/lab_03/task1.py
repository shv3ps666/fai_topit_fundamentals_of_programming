result = int(input("Введите результат: "))
work_type = str(input("Введите тип работы: "))
skip = int(input("Введите количество пропусков: "))


#Часть 1
if result < 0 or result > 100:
    print("Значение результата некорректно")
elif skip < 0 or skip > 5:
    print("Значение пропусков некорректно")
else:
    #Часть 2
    if result < 60:
        print('Уровень:', "недостаточный")
    elif result < 75:
        if skip <= 3:
            print('Уровень:', "удовлетворительный")
        else:
            print('Уровень:', "недостаточный")
    elif result < 90:
        if skip <= 3:
            print('Уровень:', "хороший")
        else:
            print('Уровень:', "удовлетворительный")
    else:
        if skip <= 3:
            print('Уровень:', "отличный")
        else:
            print('Уровень:', "хороший")

#Часть 3
match work_type:
    case 'exam':
        print("Тип работы - ", 'экзаменационная работа')
    case 'project':
        print("Тип работы - ", 'проектная  работа')
    case 'practice':
        print("Тип работы - ", 'практическая  работа')
    case _:
        print("Значение типа работы некорректно")

print('=============================================================')

#Практическое расширение
students = [ [95, "exam", 1], [85, "project", 4], [72, "practice", 2], [58, "exam", 0], [60, "project", 5], [100, "practice", 3], [75, "exam", 4], [45, "project", 1], [90, "practice", 0], [74, "exam", 3]]
total_res = [0] * 4
stats = []

def statistics(result, work_type, skip):
    if result < 0 or result > 100:
        level = None
        type = None
    elif skip < 0 or skip > 5:
        level = None
        type = None
    else:
        if result < 60:
            level = "недостаточный"
            total_res[0] += 1
        elif result < 75:
            if skip <= 3:
                level = "удовлетворительный"
                total_res[1] += 1
            else:
                level = "недостаточный"
                total_res[0] += 1
        elif result < 90:
            if skip <= 3:
                level =  "хороший"
                total_res[2] += 1
            else:
                level = "удовлетворительный"
                total_res[1] += 1
        else:
            if skip <= 3:
                level = "отличный"
                total_res[3] += 1
            else:
                level = "хороший"
                total_res[2] += 1

    match work_type:
        case 'exam':
            type = 'экзаменационная работа'
        case 'project':
            type = 'проектная  работа'
        case 'practice':
            type = 'практическая  работа'
        case _:
            type = None
    return level, type

for result, work_type, skip in students:
    level, type1 = statistics(result, work_type, skip)
    total = f"[{result}, {work_type}, {skip}] - уровень: {level} | тип работы: {type1}"
    stats.append(total)
print("Индивидуальные результаты:")
for i in stats:
    print(i)

print('================================')

print("Итоговая сводка")
print('Недостаточный:' , total_res[0])
print('Удовлетворительный:' , total_res[1])
print('Хороший:' , total_res[2])
print('Отличный:' , total_res[3])