# True나 False는 파이썬의 예약어로, true, false와 같이 작성하면 안 되고 
# 첫 문자를 항상 대문자로 작성해야 한다.

a = True
b = False
print(a)  # True
print(b)  # False       
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>
print(1 == 1)  # True
print(2 > 1)  # True
print(2 < 1)  # False
print(1 + 1 == 2)  # True
print(1 + 1 == 3)  # False
print(bool(1))  # True
print(bool(0))  # False
print(bool("Hello"))  # True
print(bool(""))  # False
print(bool([1, 2, 3]))  # True
print(bool([]))  # False
print(bool((1, 2, 3)))  # True
print(bool(()))  # False
print(bool({'a': 1}))  # True
print(bool({}))  # False
print(bool(None))  # False
print(bool(float('nan')))  # True
print(bool(float('inf')))  # True
print(bool(float('-inf')))  # True
print(bool(range(1)))  # True
print(bool(range(0)))  # False
print(bool(set([1, 2, 3])))  # True
print(bool(set()))  # False
print(bool(frozenset([1, 2, 3])))  # True
print(bool(frozenset()))  # False
print(bool(bytearray(b'abc')))  # True
print(bool(bytearray()))  # False
print(bool(memoryview(b'abc')))  # True
print(bool(memoryview(b'')))  # False

a = [1, 2, 3]
b = a[:]

id(a)
id(b)
a is b  # True

a = [1, 2, 3]
b = a

id(a)
id(b)
a is b  # True

print(b)  # [1, 2, 3]
a[1] = 4
print(a)  # [1, 4, 3]
print(b)  # [1, 2, 3]