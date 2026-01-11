dir([1, 2, 3])

dir({'1':'a'})

divmod(7, 3)


for i, name in ['body', 'foo', 'bar']:
     print(i, name)


for i, name in enumerate(['body', 'foo', 'bar']):
     print(i, name)


eval('1+2')     



def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))



def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))


class Person:
    pass

a = Person()

isinstance(a, Person)


# 스마트팜 센서 리스트
sensors = "12345"

# enumerate를 사용한 출력
for i, name in enumerate(sensors, start=1):
    print(f"{i}번 센서 장치: {name}")

for i in "12345":
    print(f"{i}번 센서 장치")


ord('a')


sorted([3, 1, 2],reverse=True)

print([3, 1, 2].sort())

a = [3,1,2]
a.sort
print(a)


list(zip([1, 2, 3], [4, 5, 6]))

list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
dir(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))