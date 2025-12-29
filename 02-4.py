
t1 = ()
print(t1)  # ()

t2 = (1,)
print(t2)  # (1,)

t3 = (1, 2, 3)
print(t3)  # (1, 2, 3)

t4 = 1, 2, 3
print(t4)  # (1, 2, 3)

t5 = ('a', 'b', ('ab', 'cd'))
print(t5)  # ('a', 'b', ('ab', 'cd'))

# 튜플은 요소를 변경할 수 없음(immutable)
t1 = (1, 2, 'a', 'b')
del t1[0]  # TypeError: 'tuple' object doesn't support item deletion
t1[0] = 'c'  # TypeError: 'tuple' object does not support item assignment


t1 = (1, 2, 'a', 'b')
print(t1[0])  # 1
print(t1[3])  # b
print(t1[-1])  # b
print(t1[1:3])  # (2, 'a')

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
print(t3)  # (1, 2, 'a', 'b', 3, 4)

t2 = (3, 4)
t4 = t2 * 3
print(t4)  # (3, 4, 3, 4, 3, 4)

t1 = (1, 2, 'a', 'b')
len(t1)  # 4    

# 튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.



