odd = [1, 3, 5, 7, 9]
print(odd)  # [1, 3, 5, 7, 9]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

a = list()
print(a)  # []
print(type(a))  # <class 'list'>

a = [1, 2, 3]
print(a[0])  # 1
print(a[1])  # 2
print(a[2])  # 3
a[0] + a[2]


a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])  # 1
print(a[1])  # 2
print(a[2])  # 3
print(a[3])  # ['a', 'b', 'c']
print(a[3][0])  # a
print(a[3][1])  # b
print(a[3][2])  # c

a = [1, 2, 3, ['a', 'b', 'c', [100, 200, 300]]]
print(a[3][3][0])  # 100
print(a[3][3][1])  # 200
print(a[3][3][2])  # 300
print(a[3][3][0] + a[3][3][2])  # 400


a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5])  # [3, ['a', 'b', 'c'], 4]    
print(a[3][1:3])  # ['b', 'c']

a = [1, 2, 3]
b = [4, 5, 6]
a + b # [1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
a * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

a = [1, 2, 3]
len(a)  # 3

a = [1, 2, 3]
a[2] = 4
print(a)  # [1, 2, 4]

a = [1, 2, 3]
del a[1]
print(a)  # [1, 3]

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)  # [1, 2]  

a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]

a = [1, 2, 3]
a.append([4, 5])

a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]

a = ['a', 'c', 'b', 'd']
a.sort()
print(a)  # ['a', 'b', 'c', 'd']


a = ['a', 'c', 'b']
a.reverse()
print(a)  # ['b', 'c', 'a']


a = [1, 2, 3]
a.index(2)  # 1
a.index(3)  # 2

a = [1, 2, 3]
a.insert(0, 4)
print(a)  # [4, 1, 2, 3]
a.insert(3, 5)
print(a)  # [4, 1, 2, 5, 3]


a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)  # [1, 2, 1, 2, 3]

a = [1, 2, 3]
a.pop()
print(a)  # [1, 2]


a = [1, 2, 3]
a.pop(1)
print(a)  # [1,

a = [1, 2, 3, 1]
a.count(1)  # 2

a = [1, 2, 3]
a.extend([4, 5])
print(a)  # [1, 2, 3, 4, 5]

b = [6, 7]
a.extend(b) 
print(a)  # [1, 2, 3, 4, 5, 6, 7]