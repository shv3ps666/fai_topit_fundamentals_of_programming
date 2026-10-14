a = 1000
a = 1001
c = int("1000")

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)#True
print("a is b:", a is b)#True
print("a == c:", a == c)#True
print("a is c:", a is c)#False



print('2.3--------------------------------------------------------------------')
c = None
print("c:", c)
print("Тип:", type(c))
print("Идентификатор:", id(c))
print("c is None:", c is None)



print('2.4--------------------------------------------------------------------s')
first = "python"
second = "py" + "thon"

print(first == second)
print(first is second)