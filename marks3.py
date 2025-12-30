# marks3.py
marks = [90, 25, 67, 45, 80]
range(len(marks))

# for number in range(len(marks)):
#     if marks[number] < 60: 
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." % (number+1))


result = [x*y for x in range(2,10) for y in range(1,10)]
print(result) 