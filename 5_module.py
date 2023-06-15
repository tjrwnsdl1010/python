# 모듈

# import fibo

# print(fibo.fib_for(5))

# # 함수도 변수에 저장가능
# my_fib = fibo.fib_for
# print(my_fib(4))

# 2. 패키지

# 패키지안에 __init__.py 가있어야 패키지로 인식함
# mypackage/
#   math/
#       __init__.py
#       fibo.py
#       formula.py
# import myPackage.math.fibo

# from 경로 import 모듈 ( as 변경할 이름 ) 
# print(myPackage)

# from myPackage.math.formula import * 

# print(formula)
# formula = 123

from myPackage.math import formula as f

# print(f)

# 모듈 사용하기

import math

# print(math.pi)
# print(math.e)

pi = math.pi
# 올림
# print(math.ceil(pi))
# 내림
# print(math.floor(pi))
# 버림
# print(math.trunc(pi))

# print(math.pow(2,5))
# print(math.sqrt(9))

# 2 random

import random

# print(random.random()) # 0~1 난수
# print(random.randint()) # 1~10 나수


# seed : 난수를 발생시키지만 동일한 순서로 발생시켜야할떄
random.seed(2)
# print(random.random())

# shuffle : 시퀀스 데이터 요소를 섞음
a = [1,2,3,4,5]
random.shuffle(a)
# print(a)

#choice : 무작위 하나를 지정
result = random.choice(a)
# print(result)

# simple 무장위 원하는 값만큼 지정
result = random.sample(a,2)
# print(result)

# 3.3 datetime

from datetime import datetime
now = datetime.now()
# print(now)

today = datetime.today()
# print(today)

utc = datetime.utcnow()
# print(utc)

result = now.strftime('%Y년 %m월 %d일' )
# print(result)

result2 = now.strftime('%d / %m %y')
# print(result2)

# 년
# print(now.year)
# 요일
# print(now.weekday())

birth = datetime(2023, 1, 1, 13, 30)
# print(birth.strftime('%m/%d는 내 생일이야'))


from datetime import timedelta

future = timedelta(days=3)
print(future)

print(birth+future)

print(now + timedelta(days = 100))

christmas = datetime(2023, 12, 25)
diff = christmas - now
print(diff.total_seconds())
