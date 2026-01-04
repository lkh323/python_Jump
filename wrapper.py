# wrapper.py

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

if __name__ == "__main__":
    mul3 = mul(3)
    mul5 = mul(5)

    print(mul3(10))  # 30 출력
    print(mul5(10))  # 50 출력




# 클로저는 함수가 생성될 때의 환경(변수 값)을 기억하는 특별한 함수
# 여기서 반환된 wrapper 함수가 바로 클로저이고,
# mul과 같이 클로저를 만들어내는 함수를 클로저 팩토리(closure factory) 함수라고 한다.