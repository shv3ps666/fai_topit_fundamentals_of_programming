"""
Программа запрашивает у пользователя данные об эксперименте(название, кол-во запусков, длительность запуска, комплексный коэффициент).
После ввода данных программа рассчитывает общую длительность всех запусков, комплексный коэффициент. В конце программа выводит информационную карточку.
"""

username = input()
experiment_name = input()
start_count = int(input())
length_of_start = float(input())
re_complex = float(input())
im_complex = float(input())

duration_sec = start_count * length_of_start
duration_min = duration_sec / 60
coef = complex(re_complex, im_complex)
coef_square = re_complex ** 2 + im_complex ** 2
has_runs = bool(start_count)

print('========================================')
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f'Исследователь: {username}')
print(f'Запуски: {start_count}')
print(f'Общее время: {duration_sec:.2f} с ({duration_min:.2f} мин)')
print(f'Коэффициент: {coef}')
print(f'Квадрат модуля: {coef_square:.2f}')
print(f'Есть выполненные запуски: {has_runs}')
print('========================================')


print('Диагностическая строка с типами шести введенных значений:')
print('username:         ', type(username))
print('experiment_name:  ', type(experiment_name))
print('start_count:      ', type(start_count))
print('length_of_start:  ', type(length_of_start))
print('re_complex:       ', type(re_complex))
print('im_complex:       ', type(im_complex))



