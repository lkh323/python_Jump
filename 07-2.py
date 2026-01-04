# def mul3(n):
#     return n * 3

# def mul5(n):
#     return n * 5

# mul3(3)
# mul5(5)

import closure

mul3 = closure.Mul(3)
mul3.mul(10)

mul5 = closure.Mul(5)
mul5.mul(10)

# def __call__(self, n):
mul3(10)  


def myfunc():
    print("함수가 실행됩니다.")


import time
def myfunc():
    start = time.time()
    print("함수가 실행됩니다.")
    end = time.time()
    print("함수 수행시간: %f 초" % (end-start))
myfunc()