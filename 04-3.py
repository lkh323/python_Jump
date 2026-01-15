f = open("C:\\Dev\\python_Jump\\_newfile.txt", "w")
f.close()

f = open(".\\_newfile.txt", "w", encoding="utf-8")
for data in range(11):
    data = "{} 번째 라인입니다.\n".format(str(data).zfill(2))
    f.write(data)
f.close()

f = open(".\\_newfile.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

f = open(".\\_newfile.txt", "r", encoding="utf-8")
lines = f.readlines()
for line in lines:
    # print(line.strip())
    print(line, end="")
f.close()

f = open(".\\_newfile.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close()

f = open(".\\_newfile.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


f = open(".\\_newfile.txt", "a", encoding="utf-8")
for i in range(11, 20):
    f.write("{} 번째 라인입니다.\n".format(str(i).zfill(2)))
f.close()


# if 문 블록의 예
if True:
    if_var = "if 블록 안의 변수"

print(if_var)  # 정상 작동! "if 블록 안의 변수" 출력

# for 문 블록의 예
for i in range(3):
    loop_var = "반복문 안의 변수"

print(i)  # 정상 작동! 2 출력
print(loop_var)  # 정상 작동! "반복문 안의 변수" 출력


# with 문에서 변수 사용 예제
with open(".\_newfile.txt", "w") as f:
    content = "Hello, Python!"  # with 블록 내에서 변수 선언
    f.write(content)

# with 블록을 벗어난 후에도 변수에 접근 가능
print(content)  # "Hello, Python!" 출력
