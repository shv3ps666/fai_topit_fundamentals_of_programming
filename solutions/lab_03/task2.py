measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]

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

print('======================================================================')

#Линейный поиск
n = int(input("Введите число: "))
check = False
for i in range(len(measurements)):
    if measurements[i] == n:
        print(i)
        check = True
        break
if check == False:
    print(-1)

print('======================================================================')

#Дополнительный алгоритмический эксперимент
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(prime(int(input('Введите число(проверка на простоту): '))))


print('======================================================================')

# Практическое расширение
import random
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

res = []
for i in [10, 100, 1000]:
    sp = [random.randint(1, i * 10) for j in range(i)]
    target = sp[random.randint(0, len(sp) - 1)]
    ind_l, linear_sravn = linear_search(sp, target)
    ind_b, binary_sravn = binary_search(sp, target)
    res.append([i, linear_sravn, binary_sravn])
for i in res:
    print('Размер:', i[0], "| Кол-во сравнений в линейном поиске:", i[1] , "| Кол-во сравнений в бинарном поиске: ", i[2])