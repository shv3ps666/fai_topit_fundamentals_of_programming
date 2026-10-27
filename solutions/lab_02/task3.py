import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


print('=======================================')


# Эксперимент со слабой ссылкой
import weakref

class Record:
    pass

record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())


print('=======================================')


#Практическое задание
class Record:
    pass
registry = weakref.WeakValueDictionary()

rec1 = Record()
rec2 = Record()
rec3 = Record()

registry["1"] = rec1
registry["2"] = rec2
registry["3"] = rec3
print([(key, value) for key, value in registry.items()])

del rec3
print([(key, value) for key, value in registry.items()])
del rec2
print([(key, value) for key, value in registry.items()])



