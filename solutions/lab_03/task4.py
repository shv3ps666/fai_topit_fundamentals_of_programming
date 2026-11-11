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



print('===================================================================================================================')
#LEGB
course = "DevOps"

def outer_function():
    course_tracker = "Базовый курс" # локальное имя outer_function; для inner_function оно объемлющее (Enclosing)

    def inner_function():
        nonlocal course_tracker # counter ищется во вложенной области, локальное не создаётся
        course_tracker = "Продвинутый курс"
        print(f"[inner] course: {course}")
        print(f"[inner] course_tracker: {course_tracker}")

    print(f"[outer до вызова inner] course_tracker: {course_tracker}")
    inner_function()
    print(f"[outer после вызова inner] course_tracker: {course_tracker}")

outer_function()
print(f"[global] course остался неизменным: {course}")


print('===================================================================================================================')
print('До фикса:')
def add_result(value, results=[]):
    results.append(value)
    return results
print(add_result(5))
print(add_result(6))
print("После фикса:")
def add_result_fixed(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results
print(add_result_fixed(5))
print(add_result_fixed(6))


print('===================================================================================================================')


#Практическое расширение
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