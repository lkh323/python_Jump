# 001 ~ 010 ####################################################### 

print("Hello World")
print("Mary's cosmetics")
print("신씨가 소리질렀다. \"도둑이야\".")
print("C:\Windows")

print("오늘은","일요일")
print("naver", "kakao", "sk", "samsung", sep = ";")
print("naver", "kakao", "sk", "samsung", sep = "/")

print("first", end = " "); print("second")
#세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.

print(5/3)

# 011 ~ 020 #######################################################

삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)

시가총액 = "298조"
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

s = "hello"
t = "python"
print(s + "!", t)

print(2 + 2*3)

a = "132"
print(type(a))

num_str = "720"
num_int = int(num_str)
print(num_int+1, type(num_int))

num = 100
num_str = str(num)
print(num_str, type(num_str))

data = "15.79"
data = float(data)
print(type(data))

year = "2020"
year = int(year)
print(year-3, year-2, year-1)

mon = 48584
cnt = 36
sum = mon * cnt
print(sum)
print(f"{sum:,}")

# 021 ~ 030 #######################################################

letters = 'python'
a = letters[0]
b = letters[2]
print(a)
print(b)

license_plate = "24가 2210"
print(license_plate[-4:])
print(license_plate[4:])

string = "홀짝홀짝홀짝"
print(string[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print(phone_number.replace("-",""))

url = "http://sharebook.kr"
idx = url.index("/")
print(url[idx+2:])

idx = url.index(".")
print(url[idx+1:])

url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[0])
print(url_split[1])
print(url_split[-1])

lang = 'python'
lang[0] = 'P'
print(lang)
#문자열은 immutable


string = 'abcdfe2a354a32a'
string_replace = string.replace("a","A")
print(string_replace)


string = 'abcd'
string.replace('b', 'B')
print(string)


# 031 ~ 040 #######################################################

a = "3"
b = "4"
print(a + b)

print("Hi"*3)

print("-"*80)

t1 = "python"
t2 = "java"
t3 = t1 + " " + t2 + " "
print(t3*4)


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s   나이 : %d" % (name1, age1))
print("이름 : %s   나이 : %d" % (name2, age2))

print("이름 : {}   나이 : {}".format(name1,age1))
print("이름 : {}   나이 : {}".format(name2,age2))

print("이름 : {0}   나이 : {1}".format(name1,age1))
print("이름 : {0}   나이 : {1}".format(name2,age2))

print("이름 : {name1}   나이 : {age1}".format(name1 = name1, age1 = age1))
print("이름 : {name2}   나이 : {age2}".format(name2 = name2, age2 = age2))


name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름 : {name1}   나이 : {age1}")
print(f"이름 : {name2}   나이 : {age2}")

x, y = 5, 3
print(f"{x} + {y} = {x + y}")

상장주식수 = "5,969,782,550"
a = int(상장주식수.replace(",",""))
print(a, type(a))

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "   삼성전자    "
print(data)
print(data.strip())
print(data.lstrip())
print(data.rstrip())



# 041 ~ 050 ######################################################

ticker = "btc_krw"
print(ticker.upper())

print("hello".capitalize())
 
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
print(file_name.endswith(("xlsx","xls")))


a = "hello world"
print(a.split(" "))

date = "2020-05-01"
print(date.split('-'))

data = "039490     "
print(data, data.rstrip())
print(len(data), len(data.rstrip()))


# 051 ~ 060 #######################################################

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(type(movie_rank), movie_rank)

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
movie_rank.append("배트맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"수퍼맨")
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]
print(movie_rank)

movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")
print(movie_rank)

























# 061 ~ 070 #######################################################



# 071 ~ 080 #######################################################



# 081 ~ 090 #######################################################



# 091 ~ 100 #######################################################



# 101 ~ 110 #######################################################

