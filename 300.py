#001 시작하기

print("Hello, World!")

print("Mary's cosmetics")

print(""" 신씨가 소리질렀다. "도둑이야". """)

print("C:\\Windows")

print("안녕하세요.\n만나서\t\t반갑습니다.")

print ("오늘은", "일요일")

print("naver", "kakao", "sk", sep=";")

print("naver", "kakao", "sk", sep="/")

print("first"); print("second")
print("first", end=" "); print("second")

print(5/3)



#002 변수수

삼성전자=50000
총평가금액=삼성전자*10
print(총평가금액)

시가총액, 현재가, PER = 298000000000000, 50000, 15.79
print(시가총액, 현재가, PER)

s = "hello"
t = "python"
print(s + "!", t)


print(2 + 2*3)


a = "132"
print(type(a))


num_str = "720"
int_num = int(num_str)
print(int_num, type(int_num))


#003 문자열

letters = 'python'
print(letters[0],letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])
print(license_plate[4:])
print(license_plate[:])

string = "홀짝홀짝홀짝"
print(string[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))
print(phone_number.replace("-", ""))

url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[0])
print(url_split[1])
print(url[-2:])


lang = 'python'
lang[0] = 'P'       
print(lang)


string = 'abcdfe2a354a32a'
string.replace('a','A')

