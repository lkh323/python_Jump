# calculator3.py
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print(cal1.sub(4))
print(cal1.sub(3))
print(cal2.add(3))
print(cal2.add(7))


class Cookie:
    pass

a = Cookie()
b = Cookie()

type(a)


class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result



a = Fourcal()
a.setdata(4,2)
Fourcal.setdata(a,4,2)

a.first
a.second

b = Fourcal()
b.setdata(3,7)
b.first
b.second
b.add()

a = Fourcal()
a.setdata(4,2)

a.add()
a.mul()
a.sub()
a.div()



# 생성자 ###########################################

a = Fourcal(4,2)
a.add()
a.first
a.second

# 클래스 상속 ###########################################

class Fourcal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

class MoreFourcal(Fourcal):  # 메서드 오버라이딩
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


a = MoreFourcal(4,2)
a.setdata(4,2)
a.pow()

# 메서드 오버라이딩 ###########################################

a = MoreFourcal(4,0)
a.div()

b = Fourcal(4,0)
b.div()

# 클래스 변수 (클래스변수는 객체변수와 달리 클래스로 만든 모든 객체에 공유된다는 특징이 있다.)

class Family:
    lastname = "Kim"

a = Family()    
b = Family()    

a.lastname
b.lastname

Family.lastname = "Lee"