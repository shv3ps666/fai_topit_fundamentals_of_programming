# Лабораторная работа № 3. Алгоритмы, коллекции и функции

## Цель работы

Научиться переводить условие задачи в алгоритм, выбирать подходящую структуру данных и разделять программу на небольшие функции с понятными контрактами.

## Задание 1. Условия и классификация данных

Создадим `task1.py`. Программа получает:

- целое число от 0 до 100 — результат студента;
- строку `exam`, `project` или `practice` — тип работы;
- целое число от 0 до 5 — количество пропущенных занятий.

Можно считать, что данные введены в корректном формате.

### Часть 1. Проверка диапазонов

С помощью `if / elif / else` проверим, что результат и количество пропусков входят в допустимые диапазоны. Если хотя бы одно значение некорректно, выведем сообщение и не будем выполнять дальнейшую классификацию.
```python
result = int(input("Введите результат: "))
work_type = str(input("Введите тип работы: "))
skip = int(input("Введите количество пропусков: "))

if result < 0 or result > 100:
    print("Значение результата некорректно")
elif skip < 0 or skip > 5:
    print("Значение пропусков некорректно")
else:
```

### Часть 2. Определение уровня результата
Назначим уровни:

Недостаточный(0-59), удовлетворительный(60-74), хороший(75-89), отличный(90-100).

Если пропущено более трех занятий, уровень снижается на одну ступень, но не может стать ниже уровня «недостаточный».
```python
    if result < 60:
        print('уровень:', "недостаточный")
    elif result < 75:
        if skip <= 3:
            print('уровень:', "удовлетворительный")
        else:
            print('уровень:', "недостаточный")
    elif result < 90:
        if skip <= 3:
            print('уровень:', "хороший")
        else:
            print('уровень:', "удовлетворительный")
    else:
        if skip <= 3:
            print('уровень:', "отличный")
        else:
            print('уровень:', "хороший")
```

### Часть 3. Сопоставление с образцом

С помощью `match / case` сформируем пояснение для типа работы:

- `exam` — экзаменационная работа;
- `project` — проектная работа;
- `practice` — практическая работа.

Для неизвестного значения предусмотрим отдельную ветвь.
```python
match work_type:
    case 'exam':
        print("Тип работы - ", 'экзаменационная работа')
    case 'project':
        print("Тип работы - ", 'проектная  работа')
    case 'practice':
        print("Тип работы - ", 'практическая  работа')
    case _:
        print("Значение типа работы некорректно")
```

### Часть 4. Тестовые сценарии

Проверим программу не менее чем на восьми наборах данных, включая границы диапазонов: `0`, `59`, `60`, `74`, `75`, `89`, `90`, `100`.

| № | result | work_type | skip | Ожидаемый результат                                      | Фактический результат                                    |
|---|--------|-----------|------|----------------------------------------------------------|----------------------------------------------------------|
| 1 | 0      | project   | 1    | уровень: недостаточный<br>project - проектная работа     | уровень: недостаточный<br>project - проектная работа     |
| 2 | 59     | exam      | 3    | уровень: недостаточный<br>exam - экзаменационная работа  | уровень: недостаточный<br>exam - экзаменационная работа  |
| 3 | 60     | practice  | 4    | уровень: недостаточный<br>practice - практическая работа | уровень: недостаточный<br>practice - практическая работа |
| 4 | 74     | exam      | 5    | уровень: недостаточный<br>exam - экзаменационная работа  | уровень: недостаточный<br>exam - экзаменационная работа  |
| 5 | 75     | project   | 0    | уровень: хороший<br>project - проектная работа           | уровень: хороший<br>project - проектная работа           |
| 6 | 89     | practice  | 3    | уровень: хороший<br>practice - практическая работа       | уровень: хороший<br>practice - практическая работа       |
| 7 | 90     | exam      | 4    | уровень: хороший<br>exam - экзаменационная работа        | уровень: хороший<br>exam - экзаменационная работа        |
| 8 | 100    | project   | 2    | уровень: отличный<br>project - проектная работа          | уровень: отличный<br>project - проектная работа          |

### Практическое расширение
```python
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
```
Вывод:
```
Индивидуальные результаты:
[95, exam, 1] - уровень: отличный | тип работы: экзаменационная работа
[85, project, 4] - уровень: удовлетворительный | тип работы: проектная  работа
[72, practice, 2] - уровень: удовлетворительный | тип работы: практическая  работа
[58, exam, 0] - уровень: недостаточный | тип работы: экзаменационная работа
[60, project, 5] - уровень: недостаточный | тип работы: проектная  работа
[100, practice, 3] - уровень: отличный | тип работы: практическая  работа
[75, exam, 4] - уровень: удовлетворительный | тип работы: экзаменационная работа
[45, project, 1] - уровень: недостаточный | тип работы: проектная  работа
[90, practice, 0] - уровень: отличный | тип работы: практическая  работа
[74, exam, 3] - уровень: удовлетворительный | тип работы: экзаменационная работа
================================
Итоговая сводка
Недостаточный: 3
Удовлетворительный: 4
Хороший: 0
Отличный: 3
```

## Задание 2. Циклы и базовые алгоритмические схемы
Исходные данные в `task2.py`:
```python
measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
```
Не используя `min()`, `max()`, `sum()` и `list.count()`, реализуем за один проход:
- вычисление суммы;
- поиск минимального значения;
- поиск максимального значения;
- подсчет четных значений;
- подсчет значений, превосходящих среднее арифметическое
```python
summa, chet = 0, 0
minimum, maximum = float('inf'), float('-inf')
more_than_arifm, count = 0, 0

for i in measurements:
    summa += i #Сумма
    if i < minimum: #Минимум
        minimum = i
    if i > maximum: #Максимум
        maximum = i
    if i % 2 == 0: #Четные значения
        chet += 1
    count += 1

arifm = summa / count
for i in measurements:
    if i > arifm:
        more_than_arifm += 1

print('Сумма:', summa)
print('Минимум:', minimum)
print('Максимум:', maximum)
print('Четных чисел:', chet)
print('Больше среднего арифметического:', more_than_arifm)
```
Последний пункт требует второго прохода, поскольку среднее становится известно после вычисления суммы.

Вывод:
```
Сумма: 144
Минимум: 7
Максимум: 21
Четных чисел: 4
Больше среднего арифметического: 6
```
Реализуем линейный поиск первого вхождения числа, введенного пользователем. Если число отсутствует, программа выведет `-1`.
```python
n = int(input("Введите число: "))
check = False
for i in range(len(measurements)):
    if measurements[i] == n:
        print(i)
        check = True
        break
if check == False:
    print(-1)
```
### Дополнительный алгоритмический эксперимент

Реализуем проверку простоты положительного целого числа. Переберем возможные делители только до квадратного корня из числа включительно.
```python
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```
Временная сложность: O($\sqrt{n}$)

- Сложность зависит от самого числа `n`.
- Требуется O(1) дополнительной памяти(только несколько целочисленных переменных).
- Ограничение делителей квадратным корнем корректно,
- Если число `n` составное, то `n = a · b`, где `a, b > 1`. Если бы оба множителя были строго больше корня из `n`, то их произведение было бы `a · b` > $\sqrt{n}$ · $\sqrt{n}$ = `n`

### Практическое расширение
Реализуем сортировку выбором и бинарный поиск в отсортированном списке. Для линейного и бинарного поиска посчитаем количество выполненных сравнений.

Псевдокод бинарного поиска и сортировки выбором соответственно:
```
#Бинарный поиск
Binary_search(A, low, high, V): 
    if high < low:
        return low - 1
    mid = low + ⌊(high - low) / 2⌋
    if V = A[mid]:
        return mid
    else if V < A[mid]:
        return Binary_Search(A, low, mid - 1, V)
    else:
        return Binary_Search(A, mid + 1, high, V)

#Сортировка выбором
Selection_sort(A, n): 
    for i = 0 to n - 2:
        min_idx = i
        for j = i + 1 to n - 1:
            if A[j] < A[min_idx]:
                min_idx = j
        if min_idx != i:
            swap(A[i], A[min_idx])
```
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons
```
| Размер списка | Количество сравнений в линейном поиске | Количество сравнений в бинарном поиске |
|---------------|----------------------------------------|----------------------------------------|
| 10            | 3                                      | 4                                      |
| 100           | 64                                     | 6                                      |
| 1000          | 466                                    | 10                                     |

Асимптотика по времени:

Сортировка выбором: O(n<sup>2</sup>)

Линейный поиск: O(n)

Бинарный поиск: O(log n)

## Задание 3. Коллекции и выбор структуры данных

Создадим `task3.py`. Используем данные о сдаче лабораторных работ:

```python
submissions = [("anna", "lab_01", 5), ("boris", "lab_01", 4), ("anna", "lab_02", 5), ("daria", "lab_01", 3), ("boris", "lab_02", 5), ("anna", "lab_01", 4)]
```
Построим:
1. Множество всех студентов.
2. Множество всех сданных лабораторных работ.
3. Словарь, в котором каждому студенту соответствует список его попыток.
4. Словарь лучших результатов по ключу `(student, laboratory)`.
5. Словарь количества попыток для каждой пары `(student, laboratory)`.

Выведите студентов, которые сдавали обе работы, используя операции над множествами.
```python
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
```
```
{'anna', 'boris'}
```

Добавим новую запись и обновим структуры без полного повторного построения.
```python
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
```
Объясним, почему:
- множество подходит для хранения уникальных значений;

Множество в Python реализовано на базе хеш-таблицы: при добавлении элемента вычисляется его хеш, и элемент помещается в «корзину». Если элемент с таким хешом и значением уже существует - он игнорируется. Поэтому дубликаты физически не могут появиться, а проверка принадлежности и вставка выполняются за O(1) в среднем.

- кортеж можно использовать как ключ словаря;

Ключом словаря может быть любой хешируемый объект. Хешируемыми в Python являются неизменяемые типы int, str, float, bool, tuple.

- список нельзя использовать как ключ словаря;

Потому что список - изменяемый объект, а значит, нехешируемый. При попытке сделать список ключом получим `TypeError: unhashable type: 'list'`.

- словарь предпочтительнее списка для частого поиска результата по составному ключу.

Словарь предпочтительнее, потому что проверка вхождения в него занимает O(1), а в списке - O(n).

Оценка средней сложности добавления и поиска для использованных коллекций:
```
set   - добавление (add)            - O(1) 
dict  - поиск по ключу              - O(1)
dict  - вставка                     - O(1)  
list  - добавление в конец(append)  - O(1) 
list  - поиск элемента (in)         - O(n)   
```
### Практическое расширение
Реализуем текстовые запросы к построенным данным:
```
student anna
best anna lab_01
attempts boris lab_02
completed lab_01
```
```python
def request(insert_data):
    parts = insert_data.strip().split()
    if not parts:
        return "Пустой запрос"

    first = parts[0]
    other = parts[1:]

    match first, other:
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
            students_for_lab = {
                student for (student, l) in best if l == lab
            }
            if students_for_lab:
                return students_for_lab
            return f"Лабораторная работа '{lab}' не найдена или никем не сдавалась"

        case _:
            return f"Неизвестная команда или неверное количество аргументов: '{insert_data}'"
```
## Задание 4. Функции, параметры и области видимости
```python
def arithmetic_mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    parts = name.strip().split()
    if not parts:
        return ""
    return " ".join(part.capitalize() for part in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    if not results:
        return f"{prefix}: {student} - нет данных"
    avg_score = sum(results) / len(results)
    return f"{prefix}: {student} - {avg_score:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    if not tags:
        return ()
    cleaned: list[str] = []
    seen: set[str] = set()

    for tag in tags:
        value = tag.strip()
        if not value:
            continue
        if lowercase:
            value = value.lower()

        if value not in seen:
            seen.add(value)
            cleaned.append(value)
    return tuple(cleaned)


# Проверки arithmetic_mean
assert arithmetic_mean([1.0, 2.0, 3.0, 4.0]) == 2.5
assert arithmetic_mean([5.0]) == 5.0
assert arithmetic_mean([]) == 0.0
assert arithmetic_mean([10.5, 2.5]) == 6.5

# Проверки normalize_name
assert normalize_name("  иван   иванович  ") == "Иван Иванович"
assert normalize_name("АННА") == "Анна"
assert normalize_name("   ") == ""
assert normalize_name("пЕтР  СИДОРОВ") == "Петр Сидоров"


# Проверки build_report
assert build_report("Иван", [5, 5], precision=0) == "Результат: Иван - 5"
assert build_report("Анна", [5, 4], precision=1, prefix="Сводка") == "Сводка: Анна - 4.5"
assert build_report("Борис", []) == "Результат: Борис - нет данных"
assert build_report("Дарья", [5, 5, 5], precision=0) == "Результат: Дарья - 5"


# Проверки collect_tags
assert collect_tags(" Python ", "python", "DEV ", "") == ("python", "dev")
assert collect_tags("Linux", "linux", "Docker", lowercase=False) == ("Linux", "linux", "Docker")
assert collect_tags() == ()
assert collect_tags("  ", "", "   ") == ()

#5)
mean_val = arithmetic_mean([4.5, 3.8, 5.0])
norm_name = normalize_name("  алексей   смирнов  ")
report = build_report("Алексей Смирнов", [4, 5, 4], precision=3, prefix="Успеваемость")
tags = collect_tags("Backend", "Python", " backend ", lowercase=True)

print(f"Среднее: {mean_val}")
print(f"Имя: {norm_name}")
print(report)
print(f"Теги: {tags}")

print('===================================================================')

#6)
raw_tags_list = ["  Git  ", "Docker", "git", "CI/CD", "   "]
unpacked_tags = collect_tags(*raw_tags_list)
print("Результат распаковки списка (*):", unpacked_tags)

slov = {
    "precision": 1,
    "prefix": "Итоговая аттестация",
}
unpacked_report = build_report("Мария Иванова", [5, 5, 4, 5], **slov)
print("Результат распаковки словаря (**):", unpacked_report)
```
Вывод:
```
Среднее: 4.433333333333334
Имя: Алексей Смирнов
Отчет: Успеваемость: Алексей Смирнов - 4.333
Теги: ('backend', 'python')

Результат распаковки списка (*): ('git', 'docker', 'ci/cd')
Результат распаковки словаря (**): Итоговая аттестация: Мария Иванова - 4.8
```

### Исследование LEGB
```python
course = "DevOps"

def outer_function():
    course_tracker = "Базовый курс" # локальное имя outer_function; для inner_function оно объемлющее (Enclosing)

    def inner_function():
        nonlocal course_tracker
        course_tracker = "Продвинутый курс"
        print(f"[inner] course: {course}")
        print(f"[inner] course_tracker: {course_tracker}")

    print(f"[outer до вызова inner] course_tracker: {course_tracker}")
    inner_function()
    print(f"[outer после вызова inner] course_tracker: {course_tracker}")

outer_function()
print(f"[global] course остался неизменным: {course}")
```
Вывод:
```
[outer до вызова inner] course_tracker: Базовый курс
[inner] course: DevOps
[inner] course_tracker: Продвинутый курс
[outer после вызова inner] course_tracker: Продвинутый курс
[global] course остался неизменным: DevOps
```
Схема областей видимости:
```
+-------------------------------------------------------------------------------+
| Built-in B: print                                                             |
|                                                                               |
|   +-----------------------------------------------------------------------+   |
|   | Global G: course, outer_function                                      |   |
|   |                                                                       |   |
|   |   +---------------------------------------------------------------+   |   |
|   |   | Enclosing E: outer_function - course_tracker, inner_function  |   |   |
|   |   |                                                               |   |   |
|   |   |   +-------------------------------------------------------+   |   |   |
|   |   |   | Local L: inner_function                               |   |   |   |
|   |   |   |                                                       |   |   |   |
|   |   |   |   +-----------------------------------------------+   |   |   |   |
|   |   |   |   |            nonlocal course_tracker            |   |   |   |   |
|   |   |   |   +-----------------------------------------------+   |   |   |   |
|   |   |   |                                                       |   |   |   |
|   |   |   +-------------------------------------------------------+   |   |   |
|   |   |                                                               |   |   |
|   |   +---------------------------------------------------------------+   |   |
|   |                                                                       |   |
|   +-----------------------------------------------------------------------+   |
|                                                                               |
+-------------------------------------------------------------------------------+ 
```
Правило LEGB: при чтении имени Python ищет его последовательно в областях Local → Enclosing → Global → Built-in и берёт первое найденное. Какая область считается локальной для имени, определяется при компиляции функции: если имя где-то в теле функции присваивается, оно локальное, если нет global или nonlocal.

### Ошибка изменяемого значения по умолчанию
Исследуйте и исправьте функцию:

```python
def add_result(value, results=[]):
    results.append(value)
    return results
print(add_result(5))
print(add_result(6))
```
Вывод:
```
[5]
[5, 6]
```

Объясните ошибку через жизненный цикл объекта значения по умолчанию.

Значение по умолчанию вычисляется один раз при выполнении def и хранится в самой функции (add_result). Все вызовы без аргумента получают один и тот же объект. Если функция его меняет(так как список изменяемый), изменения остаются до следующего вызова.

```python
def add_result_fixed(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results
print(add_result_fixed(5))
print(add_result_fixed(6))
```
Вывод:
```
[5]
[6]
```
### Практическое расширение
Реализуйте функцию `apply_to_results(operation, values)`, принимающую другую функцию и последовательность результатов. Передайте в нее именованную функцию и `lambda`. Затем создайте фабрику `make_threshold_checker(threshold)`, которая возвращает функцию проверки результата. Продемонстрируйте две независимые проверки с разными порогами и объясните, какое значение сохраняется в замыкании.
```python
def apply_to_results(operation, values):
    result = []
    for value in values:
        result.append(operation(value))
    return result

def square(x):
    return x**2

def make_threshold_checker(threshold):
    def check(result):
        return result >= threshold

    return check

results = [48, 62, 75, 90]

print(apply_to_results(square, results))  # именованная функция
print(apply_to_results(lambda x: x * 2, results))  # lambda

pass1_check = make_threshold_checker(60)
pass2_check = make_threshold_checker(85)

print(pass1_check(70), pass2_check(70))
print(apply_to_results(pass1_check, results))
print(apply_to_results(pass2_check, results))
```
Вывод:
```
[2304, 3844, 5625, 8100]
[96, 124, 150, 180]
True False
[False, True, True, True]
[False, False, False, True]
```

Каждая функция сохраняет свой `threshold`: `pass_check` - 60, `another_check` - 85. Поэтому проверки работают независимо друг от друга. `pass_check` не результат проверки, а ссылка на функцию `check`.

## Задание 5. Анализатор учебных результатов

Создайте программу, которая анализирует результаты группы. Исходные данные можно хранить непосредственно в `task5.py`:

```python
students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}
```

### Обязательные функции

Реализуйте:

- `mean(values)` — среднее значение;
- `minimum(values)` — минимум без использования `min()`;
- `maximum(values)` — максимум без использования `max()`;
- `classify(score)` — текстовая категория результата;
- `student_summary(name, results)` — словарь с итогами одного студента;
- `group_summary(students)` — общая статистика группы;
- `find_top_students(students)` — список студентов с наибольшим средним результатом;
- `format_report(student_data, group_data)` — итоговый текстовый отчет.

Программа должна:

1. Сформировать статистику для каждого студента.
2. Вывести средний, минимальный и максимальный результат.
3. Определить категорию по среднему результату.
4. Найти лидера или нескольких лидеров с одинаковым средним результатом.
5. Посчитать количество студентов в каждой категории.
6. Вывести общий средний результат группы.
7. Сформировать рейтинг без изменения исходного словаря.
8. Корректно обрабатывать студента с пустым списком результатов с помощью заранее выбранного правила.

### Проверка

Подготовьте не менее шести сценариев:

- обычный набор данных;
- один студент;
- несколько лидеров;
- пустая группа;
- студент без результатов;
- граничные значения категорий.

Для каждой публичной функции сформулируйте контракт: допустимые входные данные, результат и возможные особые случаи. Объясните декомпозицию программы и оцените сложность построения общей статистики.

```python
students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values):
    if not values:
        return None
    return sum(values) / len(values)


def minimum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    if not values:
        return None
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def classify(score):
    if score is None:
        return "Нет данных"
    if score >= 90:
        return "Отлично"
    if score >= 75:
        return "Хорошо"
    if score >= 60:
        return "Удовлетворительно"
    return "Неудовлетворительно"


def student_summary(name, results):
    average = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": average,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(average),
    }


def find_top_students(students):
    if not students:
        return []
    means = {}
    for name, results in students.items():
        if results:
            means[name] = mean(results)
    if not means:
        return []
    best = maximum(list(means.values()))
    top = []
    for name, value in means.items():
        if value == best:
            top.append(name)
    return top


def group_summary(students):
    category_counts = {
        "Отлично": 0,
        "Хорошо": 0,
        "Удовлетворительно": 0,
        "Неудовлетворительно": 0,
        "Нет данных": 0,
    }
    total = 0
    count = 0
    for results in students.values():
        category_counts[classify(mean(results))] += 1
        total += sum(results)
        count += len(results)
    group_mean = None
    if count > 0:
        group_mean = total / count
    return {
        "student_count": len(students),
        "result_count": count,
        "mean": group_mean,
        "category_counts": category_counts,
        "top_students": find_top_students(students),
    }


def format_report(student_data, group_data):
    with_results = []
    without_results = []
    for item in student_data:
        if item["mean"] is None:
            without_results.append(f"{item['name']} (оценок: {item['count']}, категория: {item['category']})")
        else:
            with_results.append(item)

    ranking = sorted(with_results, key=lambda item: item["mean"], reverse=True)
    group_mean_str = "-" if group_data["mean"] is None else f"{group_data['mean']:.1f}"

    lines = [
        "==========================================",
        "           СВОДКА ПО УСПЕВАЕМОСТИ         ",
        "==========================================",
        f"Студентов: {group_data['student_count']} | Всего оценок: {group_data['result_count']} | Средний балл группы: {group_mean_str}",
        "------------------------------------------",
        "Индивидуальный рейтинг (по убыванию среднего балла):",
    ]

    if ranking:
        for place, item in enumerate(ranking, start=1):
            lines.append(
                f"  {place}) {item['name']} — среднее: {item['mean']:.1f} "
                f"(оценок: {item['count']}, мин. оценка: {item['min']}, макс. оценка: {item['max']}) "
                f"[{item['category']}]"
            )
    else:
        lines.append("  (нет данных для построения рейтинга)")

    lines.append("")
    lines.append("Количество студентов по категориям:")
    for category, number in group_data["category_counts"].items():
        lines.append(f"  • {category}: {number}")

    lines.append("------------------------------------------")
    lines.append("Лидеры: " + (", ".join(group_data["top_students"]) or "нет"))
    lines.append("Студенты без оценок: " + (", ".join(without_results) or "нет"))
    lines.append("==========================================")
    return "\n".join(lines)


def build_report(data):
    student_data = [student_summary(name, results) for name, results in data.items()]
    return format_report(student_data, group_summary(data))

def run_checks():
    # 1. Обычный набор данных
    snapshot = {name: results.copy() for name, results in students.items()}
    group = group_summary(students)
    assert group["student_count"] == 4
    assert group["result_count"] == 13
    assert round(group["mean"], 2) == 79.38
    assert group["top_students"] == ["Дарья"]
    assert group["category_counts"]["Отлично"] == 1
    assert group["category_counts"]["Хорошо"] == 1
    assert group["category_counts"]["Удовлетворительно"] == 1
    assert group["category_counts"]["Неудовлетворительно"] == 1
    anna = student_summary("Анна", students["Анна"])
    assert (anna["mean"], anna["min"], anna["max"]) == (85.25, 78, 91)
    assert students == snapshot  # исходный словарь не изменён

    # 2. Один студент
    one = {"Вера": [80, 100]}
    assert group_summary(one)["top_students"] == ["Вера"]
    assert group_summary(one)["mean"] == 90.0
    assert student_summary("Вера", one["Вера"])["category"] == "Отлично"

    # 3. Несколько лидеров (одинаковое среднее 90)
    tie = {"А": [90, 90], "Б": [80, 100], "В": [70]}
    assert find_top_students(tie) == ["А", "Б"]

    # 4. Пустая группа
    empty = {}
    empty_group = group_summary(empty)
    assert empty_group["student_count"] == 0
    assert empty_group["mean"] is None
    assert empty_group["top_students"] == []
    assert "Лидеры: нет" in build_report(empty)

    # 5. Студент без результатов
    partly = {"А": [], "Б": [80]}
    assert student_summary("А", [])["mean"] is None
    assert student_summary("А", [])["category"] == "Нет данных"
    assert find_top_students(partly) == ["Б"]
    assert group_summary(partly)["mean"] == 80.0
    assert group_summary(partly)["category_counts"]["Нет данных"] == 1

    # 6. Границы категорий
    assert classify(90) == "Отлично"
    assert classify(89.99) == "Хорошо"
    assert classify(75) == "Хорошо"
    assert classify(74.99) == "Удовлетворительно"
    assert classify(60) == "Удовлетворительно"
    assert classify(59.99) == "Неудовлетворительно"
    assert classify(0) == "Неудовлетворительно"



print(build_report(students))
run_checks()
```
Вывод:
```
==========================================
           СВОДКА ПО УСПЕВАЕМОСТИ         
==========================================
Студентов: 4 | Всего оценок: 13 | Средний балл группы: 79.4
------------------------------------------
Индивидуальный рейтинг (по убыванию среднего балла):
  1) Дарья — среднее: 93.8 (оценок: 4, мин. оценка: 90, макс. оценка: 97) [Отлично]
  2) Анна — среднее: 85.2 (оценок: 4, мин. оценка: 78, макс. оценка: 91) [Хорошо]
  3) Борис — среднее: 66.7 (оценок: 3, мин. оценка: 60, макс. оценка: 72) [Удовлетворительно]
  4) Илья — среднее: 58.0 (оценок: 2, мин. оценка: 55, макс. оценка: 61) [Неудовлетворительно]

Количество студентов по категориям:
  • Отлично: 1
  • Хорошо: 1
  • Удовлетворительно: 1
  • Неудовлетворительно: 1
  • Нет данных: 0
------------------------------------------
Лидеры: Дарья
Студенты без оценок: нет
==========================================
```
#### Сложность

Пусть N — общее число результатов, S — число студентов.

1. `mean`, `minimum`, `maximum`, `student_summary` для одного студента: один проход, O(k), где k — число его результатов.
2. `group_summary`: один проход по всем результатам, O(N). `find_top_students`: O(N + S), так как среднее считается для каждого студента.

3. Сортировка рейтинга: O(S log S).

Итого O(N + S log S) по времени, O(S) по дополнительной памяти (словари средних и итогов студентов).

#### Декомпозиция

Архитектура разбита на иерархические уровни, где каждый верхний слой вызывает только функции нижележащего:
* Базовый слой (`mean`, `minimum`, `maximum`, `classify`): элементарные расчёты по списку оценок и перевод балла в текстовую категорию.
* Слой агрегации (`student_summary`, `find_top_students`, `group_summary`): сборка итоговых словарей со статистикой отдельного студента и группы в целом.
* Слой представления (`format_report`, `build_report`): сортировка рейтинга и сборка текстового отчёта.

## Результаты

После выполнения работы я умею:

- применять условия, циклы и сопоставление с образцом;
- реализовывать поиск, подсчет и накопление;
- работать со списками, кортежами, словарями и множествами;
- выбирать структуру данных с учетом назначения и сложности операций;
- создавать функции с позиционными и именованными параметрами;
- использовать аннотации типов и строки документации;
- объяснять области видимости имен по правилу LEGB;
- декомпозировать прикладную задачу на функции;
- оценивать сложность простых алгоритмов.
