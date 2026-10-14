student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print('4.1------------------------------------------------------')
print(student[0])
print(student[-1])


print('4.2------------------------------------------------------')
print(student[0:4])
print(student[5:13])


print('4.3------------------------------------------------------')
print(student.upper())
print(student.lower())



print('4.4------------------------------------------------------')
print(student[0] + '.' + student[5] + '.')


print('4.5------------------------------------------------------')
print(course[::-1])


print('4.6------------------------------------------------------')
#1 способ(%)
print("%s — %s: %d/%d (%s%%)" % (student, course, completed, total, (completed / total) * 100))
#2 способ(.format())
print("{} - {}: {}/{} ({}%)".format(student, course, completed, total, (completed / total) * 100))
#3 способ(f-строка)
print(f"{student} — {course}: {completed}/{total} ({(completed / total) * 100}%)")


print('4.7------------------------------------------------------')
symbol = "Я"
print(symbol)
print(ord(symbol))
print(chr(1071))
print(symbol.encode('utf-16'))
print(len(symbol.encode('utf-8')))


print('4.8------------------------------------------------------')
#student[0] = '0'