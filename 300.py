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


nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

nums = [1, 2, 3, 4, 5]
total = 0
for n in nums :
    total += n
print(total)      


nums = [1, 2, 3, 4, 5]
sum(nums)

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))


# 061 ~ 070 #######################################################

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])
print(nums[1::2])

nums = [1, 2, 3, 4, 5]
print(nums[::-1])

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("".join(interest))
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
print(string.split("/"))

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 리스트 객체 자체의 순서를 바꿉니다. 별도의 메모리를 추가로 사용하지 않아 효율적이지만, 원본 데이터가 사라진다는 점을 유의해야 합니다.

# 071 ~ 080 #######################################################

my_variable = ()
type(my_variable)

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

t = (1,)

t = 1, 2, 3, 4
type(t)

t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

interest = ['삼성전자', 'LG전자', 'SK Hynix']
type(interest)
type(tuple(interest))


temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

data = tuple(range(2,99,2))
type(data)
print(data)


# 081 ~ 090 #######################################################

a, b, *c = (0, 1, 2, 3, 4, 5)
a
b
type(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*a, b, c = scores
a
b
c

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *c = scores
a
b
c

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *b, c = scores
a
b
c

temp = {}
type(temp)

data1 = {"메로나":1000,"폴라포":"1200", "빵빠레":1800}
data2 = {"죠스바":1200,"월드콘":"1500"}
data1.update(data2)

ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}

ice["메로나"]
ice.get("메로나")


# 091 ~ 100 #######################################################


ice = {'메로나': [300,20],
       '비비빅': [400,3],
       '죠스바': [250,100]}

ice
ice.get("메로나")[1]
ice["메로나"][1]


inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory.update({"월드콘": [500, 7]})
inventory["누가바"] = [1500, 17]
inventory

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream.keys()
list(icecream.keys())

icecream.values()
sum(icecream.values())

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = list(zip(date,close_price))
close_table = dict(zip(date,close_price))


# 101 ~ 110 #######################################################

print(3 >= 4)
print(3 <= 4)

if 4 < 3:
    print("Hello World")

if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")


if True :
    print("1")
    print("2")
else :
    print("3")
print("4")


if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")


# 111 ~ 120 #######################################################

a = input("입력 :")
print(a*2)

a = input("입력 :")
print(int(a) + 10)

a = input("입력 :")
if int(a) % 2 == 0 :
    print("짝수 입니다.")
else :
    print("홀수 입니다.")

a = input("입력 :")
if int(a) <= 255 :
    int(a) + 20
else :
    print(255)

a = input("좋아하는 과일은 ? ")
fruit = ["사과", "포도", "홍시"]
if fruit.count(a) > 0:
   print("정답입니다.") 


a = input("좋아하는 과일은 ? ")
fruit = ["사과", "포도", "홍시"]
if a in fruit : 
    print("정답입니다.")
else :
    print("오답입니다.")

a = input("투자종목을 입력하세요 ? ")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
if a in warn_investment_list:
    print("투자 유의 종목입니다.")
else:
    print("투자 유의 종목이 아닙니다.")


a = input("제일 좋아하는 계절은 ? ")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
if a in fruit.values():
    print("정답")
else:
    print("오답")


# 121 ~ 130 #######################################################

a = input("문자를 입력하세요")
if a.isupper() :
    print(a.lower())
else:
    print(a.upper())



a = input("점수를 입력하세요")
if 81 <= int(a)  < 100:
    print("A")
elif  61 <= int(a)  < 80:
    print("B")
elif  41 <= int(a)  < 60:
    print("C")
elif  21 <= int(a)  < 40:
    print("D")
elif  0 <= int(a)  < 20:
    print("E")


country_money =  input("입력 : ")
money, country = country_money.split(sep=" ")

if country == "달러":
    print(1167*int(money))
elif country == "엔":
    print(1.096*int(money))
elif country == "유로":
    print(1268*int(money))
elif country == "위안":
    print(171*int(money))


환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

num1 = input("number 1 : ")
num2 = input("number 2 : ")
num3 = input("number 3 : ")

numbers = [num1, num2, num3]
print(max(numbers))

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)


phone = input("휴대전화 번호 입력 : ")
data ={"011":"SKT","016":"KT","019":"LGU","010":"알수없음"}
a = phone.split("-")
if a[0] == "011":
    prnt("SKT")
elif a[0] == "016":
    print("KT")
elif a[0] == "019":
    print("LGU")
elif a[0] == "010":
    print("알수없음.")


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
opening_price = float(btc.get("opening_price"))
max_price = float(btc.get("max_price"))
range_money = float(btc.get("max_price")) - float(btc.get("min_price"))

if (opening_price - range_money) > max_price :
    print("상승장")
else :
    print("하락장")


# 131 ~ 140 #######################################################

for 변수 in [10, 20, 30]:
    print(변수)
    print("---------")


for 변수 in [10, 20, 30, 40]:
    print("---------")

# 141 ~ 150 #######################################################

리스트 = [100, 200, 300]
for data in 리스트 :
    print(int(data) + 10)

리스트 = ["김밥", "라면", "튀김"]
for data in 리스트 :
    print("오늘의 메뉴 " + data)

리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for data in 리스트 :
    print(len(data))

리스트 = ['dog', 'cat', 'parrot']
for data in 리스트 :
    print(data, str(len(data)))

리스트 = ['dog', 'cat', 'parrot']
for data in 리스트 :
    print(data[0])
    
리스트 = [1, 2, 3]
for data in 리스트 :
    # print("3 * %s " % data)
    # print(f"3 * {data}")
    print("3 * {} = {}".format(data, data *3))


리스트 = ["가", "나", "다", "라"]
n = 0
for data in 리스트 :
    n += 1 
    if n > 1 :
        print(data)

리스트 = ["가", "나", "다", "라"]
리스트 = 리스트[1:]
for data in 리스트 :
    print(data)

리스트 = ["가", "나", "다", "라"]
for data in 리스트[1:] :
    print(data)

리스트 = ["가", "나", "다", "라"]
for data in 리스트[0::2] :
    print(data)

리스트 = ["가", "나", "다", "라"]
for data in 리스트[::-1] :
    print(data)


# 151 ~ 160 #######################################################

리스트 = [3, -20, -3, 44]
for data in 리스트 :
    if data < 0 :
        print(data)


리스트 = [3, 100, 23, 44]
for data in 리스트 :
    if data % 3 == 0 :
        print(data)

리스트 = [13, 21, 12, 14, 30, 18]
for data in 리스트 :
    if data % 3 == 0 and data < 20:
        print(data)


리스트 = ["I", "study", "python", "language", "!"]
for data in 리스트 :
    if len(data) > 3 :
        print(data)


리스트 = ["A", "b", "c", "D"]
for data in 리스트 :
    if data.isupper() :
        print(data)

리스트 = ["A", "b", "c", "D"]
for data in 리스트 :
    if data.islower() :
        print(data)

리스트 = ['dog', 'cat', 'parrot']
for data in 리스트 :
    print(data.capitalize())

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for data in 리스트 :
    print(data.split(".")[0])

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for data in 리스트 :
    if data.endswith(("h","c")) :
        print(data)


# 161 ~ 170 #######################################################

for data in range(2002, 2051, 4):
    print(data, end = " ")

for data in range(1, 31):
    if data % 3 == 0 :
        print(data, end = " ")

for data in range(1, 31, 3):
    print(data, end = " ")


for data in range(99, -1, -1):
    print(data, end = " ")

for data in range(100):
    print(99 - data, end = " ")

for data in range(10):
    print(data * 0.1)

for data in range(10):
    print(f"3 * {data} =", 3*int(data))

hap = 0
for data in range(1,11):
    hap = hap + data
print(hap)


hap = 0
for data in range(1,11,2):
    hap = hap + data
print(hap)


gop = 1
for data in range(1,11):
    gop = gop * data
print(format(gop,","))
print(f"{gop:,}")


# 171 ~ 180 #######################################################

price_list = [32100, 32150, 32000, 32500]
for data in price_list:
    print(data)

price_list = [32100, 32150, 32000, 32500]
for data in range(4):
    print(price_list[data])

price_list = [32100, 32150, 32000, 32500]
i = len(price_list) - 1
for data in range(4):
    print(i - data, price_list[data])
    # print(price_list[data])
    # print(price_list[data])


price_list = [32100, 32150, 32000, 32500]
for data in range(1,4):
    print(100 + 10*(data-1), price_list[data])

price_list = [32100, 32150, 32000, 32500]
for data in range(1,4):
    print(90 + 10*data, price_list[data])

my_list = ["가", "나", "다", "라"]
for data in range(0,3):
    print(my_list[data], my_list[data+1])
 

my_list = ["가", "나", "다", "라"]
for data in range(3,0,-1):
    print(my_list[data], my_list[data-1])
 
my_list = ["가", "나", "다", "라", "마"]
for data in range(0,4):
    print(my_list[data], my_list[data+1], my_list[data+2])
 

my_list = [100, 200, 400, 800]
for data in range(3):
    print(my_list[data + 1] - my_list[data])
 
for data in range(0,4):
    print((my_list[data] + my_list[data+1] + my_list[data+2])/3)
 

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])

# 181 ~ 190 #######################################################

apart = [["101호","102호"], ["201호","202호"], ["301호","302호"]]

stock = [["시가", 100, 200, 300], ["종가", 80, 210, 330]]

stock = {"시가":[100, 200, 300],"종가":[80, 210, 330]}

stock = {"10/10":[80, 110, 70, 90],"10/11":[210, 230, 190, 200]}

apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(str(col) + "호")

apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row:
        print(str(col) + "호")

apart = [[101, 102], [201, 202], [301, 302]]
apart.reverse()
for i in list(apart):
    print(str(i[0]) + " 호")
    print(str(i[1]) + " 호")

apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart[::-1]:
    for col in row[::-1]:
        print(str(col) + "호")


apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(str(col) + "호")
        print("-"*5)

apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(str(col) + "호")
    print("-"*5)


# 191 ~ 200 #######################################################

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for row in data:
    for col in row:
        print(col*1.00014) 
    print("-"*5)


data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for row in data:
    for col in row:
        result.append(col*1.00014) 

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for row in data:
    result_sub = []
    for col in row:
        result_sub.append(col*1.00014) 
    result.append(result_sub)

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc:
    print(i[1][-1])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[-1])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[-1] > 150 :
        print(i[-1])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    if i[3] >= i[0] :
        print(i[3])

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []        
for i in ohlc[1:]:
    volatility.append(i[1] - i[2])
print(volatility)


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum = 0        
for i in ohlc[1:]:
    sum += (i[0] - i[3])
print(sum)    


# 201 ~ 210 #######################################################

def print_coin():
    return "비트코인"

print_coin()

for i in range(100):
    print_coin()


def print_coin():
    for i in range(100):
        print_coin()    


# 211 ~ 220 #######################################################

def print_with_smile(a):
    print(a , ":D")

print_with_smile("Hi")    


def print_upper_price(num):
    print(int(num)*1.3)

print_upper_price(1000)


def print_sum(num1, num2):
    print(num1 + num2)

print_sum(100, 200)


def print_arithmetic_operation(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

print_arithmetic_operation(40, 10)

def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)

print_max(1,2,3)
print_max(3,2,1)
print_max(2,3,1)


# 221 ~ 230 #######################################################

def print_reverse(str):
    print(str[::-1])

print_reverse("python")    


def print_score(list):
    sum = 0
    for data in list:
        sum += data
    print(sum / len(list))

print_score([1,2,3])


def print_score(list):
    print(sum(list) / len(list))

print_score([1,2,3])


def print_even(list):
    for data in list:
        if data % 2 == 0:
            print(data)

print_even([1, 3, 2, 10, 12, 11, 15])






# 231 ~ 240 #######################################################
# 241 ~ 250 #######################################################
# 251 ~ 260 #######################################################
# 261 ~ 270 #######################################################
# 271 ~ 280 #######################################################
# 281 ~ 290 #######################################################
# 291 ~ 300 #######################################################


