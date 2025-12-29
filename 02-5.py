# 파이썬 3.7 이후 딕셔너리 순서 보장
# 파이썬 3.7 이전 버전에서는 딕셔너리에 데이터를 저장할 때 입력한 순서가 보장되지 않았다.
# 하지만 파이썬 3.7부터는 딕셔너리에 아이템을 삽입한 순서가 유지된다.
# 즉, 딕셔너리를 순회할 때 아이템이 추가된 순서대로 나온다.


dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])  # pey

dic['name'] = 'junho'
print(dic['name'])  # junho 

dic['address'] = 'seoul'
print(dic)  # {'name': 'junho', 'phone': '010-9999-1234', 'birth': '1118', 'address': 'seoul'}

del dic['birth']
print(dic)  # {'name': 'junho', 'phone': '010-9999-1234', 'address': 'seoul'}
print(dic.keys())  # dict_keys(['name', 'phone', 'address'])
print(dic.values())  # dict_values(['junho', '010-9999-1234', 'seoul'])
print(dic.items())  # dict_items([('name', 'junho'), ('phone', '010-9999-1234'), ('address', 'seoul')])

{'name': 'junho', 'phone': '010-9999-1234', 'address': 'seoul'}.clear()
print(dic)  # {}

type({'name': 'junho'})  # <class 'dict'>
type({'': ''}) # <class 'dict'>
type(())    # <class 'tuple'>
type([])    # <class 'list'>
type(set())  # <class 'set'>    


# 딕셔너리에는 동일한 Key가 중복으로 존재할 수 없다.
a = {1:'a', 1:'b'}
print(a)  # {1: 'b'}

a = {1:'a', 1:'b', 1:'c'}
print(a)  # {1: 'c'}    

# Key에 리스트는 쓸 수 없다는 것이다. 
# 하지만 튜플은 Key로 쓸 수 있다. 
# 딕셔너리의 Key로 쓸 수 있느냐, 없느냐는 Key가 변하는(mutable) 값인지, 
# 변하지 않는(immutable) 값인지에 달려 있다

a = {[1,2] : 'hi'}  # TypeError: unhashable type: 'list'

a = {(1,2) : 'hi'}
print(a)  # {(1, 2): 'hi'}
b = {(1,2) : 'hello', (3,4) : 'world'}
print(b)  # {(1, 2): 'hello', (3, 4): 'world'}
print(b[(1,2)])  # hello
print(b[(3,4)])  # world


a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a["birth"]  # '1118'
a.get("birth")  # '1118'    

a.keys()  # dict_keys(['name', 'phone', 'birth'])
a.values()  # dict_values(['pey', '010-9999-1234', '1118'])
a.items()  # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

for k in a.keys():
    print(k)
# name
# phone
# birth

a.clear()
print(a)  # {}

# a['nokey']처럼 딕셔너리에 존재하지 않는 키로 값을 가져오려고 할 경우, 
# a['nokey'] 방식은 오류를 발생시키고 a.get('nokey') 방식은 None을 반환한다는 차이가 있다.

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
a.get('nokey') # None
type(a.get('nokey')) # <class 'NoneType'>
a['nokey']  # KeyError: 'nokey'

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
'name' in a  # True
'email' in a  # False
'pey' in a  # False

a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print(phone)  # 010-9999-1234
print(a)  # {'name': 'pey', 'birth': '1118'}






























