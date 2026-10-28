import sys, tracemalloc

a=[]
b=[1,2,3,4,5,6,7,8,9,10]

tup =(1,2,3,4,5,6,7,8,9,10)
text = 'abcdefghij'

t=12345
n = None

print(a, 'Размер(Byte):', sys.getsizeof(a))
print(b, 'Размер(Byte):', sys.getsizeof(b))
print(tup, 'Размер(Byte):', sys.getsizeof(tuple))
print(text, 'Размер(Byte):', sys.getsizeof(str))
print(t, 'Размер(Byte):', sys.getsizeof(t))
print(n, 'Размер(Byte):', sys.getsizeof(n))


print('=======================================')


my_list = []
prev_size = sys.getsizeof(my_list)
print(f"Длина: {len(my_list)}, Размер: {prev_size} байт")

for i in range(100):
    my_list.append(i)
    current_size = sys.getsizeof(my_list)
    if current_size != prev_size:
        print(f"Длина: {len(my_list)}, Размер: {current_size} байт, (+{current_size - prev_size})")
        prev_size = current_size


print('=======================================')


tracemalloc.start()
numbers = list(range(100_000))
current, peak = tracemalloc.get_traced_memory()
print("Current memory: %.2f kB" % (current / 1024))
print("Peak memory:    %.2f kB" % (peak / 1024))
tracemalloc.stop()

print('======')

tracemalloc.start()
numbers1 = range(100_000)
current1, peak1 = tracemalloc.get_traced_memory()
print("Current memory: %.2f kB" % (current1 / 1024))
print("Peak memory:    %.2f kB" % (peak1 / 1024))
tracemalloc.stop()