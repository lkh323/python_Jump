from faker import Faker
fake = Faker('ko-KR')
fake.name()

fake.address()

test_data = [(fake.name(), fake.address()) for i in range(30)]

import time
time.localtime(time.time())


import webbrowser

webbrowser.open_new('http://python.org')


from fractions import Fraction
import sympy

# 가지고 있던 돈을 x라고 하자.
x = sympy.symbols("x")

# 가지고 있던 돈의 2/5가 1760원이므로 방정식은 x * (2/5) = 1760 이다.
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식을 만족하는 값(result)을 구한다.
result = sympy.solve(f)  # 결괏값은 리스트

# 남은 돈은 다음과 같이 가지고 있던 돈에서 1760원을 빼면 된다.
remains = result[0] - 1760

print('남은 돈은 {}원 입니다.'.format(remains))



import sympy
x = sympy.symbols("x")
f = sympy.Eq(x**2, 1)
sympy.solve(f)

import sympy
x, y = sympy.symbols('x y')
f1 = sympy.Eq(x+y, 10)
f2 = sympy.Eq(x-y, 4)
sympy.solve([f1, f2])
{x: 7, y: 3}


