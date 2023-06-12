# 주석처리 (ctrl + /)

# 키워드 
# import keyword
# print(keyword.kwlist)

# 1.1 number
# integer(정수형)

# a = 10
# print(type(a))

# float(실수형)
# b = 1.1
# print(type(b))

# 실수 => 부동소수점으로 관리
# c = 1.1
# d = 1.12

# print(c-d)

# 1.2 boolean

# a = True
# b = False
# print(type(a))

# c = 1 
# d = 0 

# print(bool(1)) #컨버팅

# e = None
# print(type(e))

# 1.3 String 문자열 ("")
# greeting = "helo"
# name = "change"

# print(greeting,name)
# print(type(name))

# age = input() # 사용자가 입력한 값을 문자열값으로 저장한다.
# print(age)

# String interpolation
# dust = 10
# messege = "오늘 미세먼지 농도는 10입니다"

# messege1 = "오늘 미세먼지 농도는 %s입니다" %dust
# messege2 = "오늘 미세먼지 농도는 {}입니다".format(dust)
# messege3 = f"오늘 미세먼지 농도는 {dust}입니다"
# print(messege1,messege2,messege3)

# 2. 연산자
# + - * /
# a = 10
# b = 3

# // (몫) 
# print(a // b)

# % (나머지)
# print(a%b)

# divmod (몫과 나머지)
# print(divmod(a,b))

# ** (거듭제곱)
# print(a**b)

# 2.2 비교연산자
# > < == !
# a = 1
# b = 2

# print(a >= b)
# print(a == b)
# print(a != b)
# print("hi" == "hi")


# 2.3 논리연산자
# a = True
# b = False

# print(a and b) # 둘 다 True면 True

# or (둘중 하나라도 True면 True)
# print(a or b) #True
# print(b or b) #False

# not 
# print(not a) #반대로 값을 바꿈

# 2.4 복합연산자
# += -= /= *= //= **=
# n = 0
# while n < 5:
#     print(n)
#     n += 1

# 2.5 기타연산자
# concatenation
# print("hi" + "gh") # 문자열을 연결    

# in 
# print("hi" in "high") # 앞에 데이터에 뒤에 데이터값에 포함돼 있는지 확인


# is
# a = "hi"
# b = "hi"
# print(a is b)

# 우선순위
# print((-3) ** 5) #()로 우선순위를 설정가능

# 3. 형변환

# 3.1 임시적 형변환
# print(True + 3) # True를 1로 자동으로 형변환함

# a = 3
# if a % 2: # 결과는 1, 1은 True, 0은 False
#     print("홀수입니다")

# 3.2 명시적 형변환
# print("미세먼지 농도 :" + 10) # 문자열 끼리만 concatnation 사용가능
# print("미세먼지 농도 :" + str(10))
# print(10 + int("20"))
# print(float("3.4"))
# print(float(2))
# print(int(2.5)) # int는 10진수 안에수만 형변환가능

# 4. 시퀀스 데이터
# 리스스(list), 튜플(tuple), 레인지(range), 문자열(String)

# 4.1 리스트(list)
# 수정가능(mutable)
# a = [val1, val2, val3, ...]
# a[index]

# a = []
# b = list()
# print(type(a), type(b))

# location = ["서울", "대전", "대구"]
# print(location[2])
# location[0] = "부산"

# 리스트안 리스트 형태 : 다양한 타입을 저장할 수 있음
# a = [
#     [1,2,3],
#     {4,5,6},
#     (7,8,9),
# ]

# 4.2 튜플
# a = (val1, va2, val3, ...) # 수정이 불가능함 (immutable)
# a += 1; a[1] = 3 불가능함

# b, c = (1, 2)
# print(b, c) #자동으로 값이 분리되어 할당됨

# b, c = c, b
# print(b, c)

# 4.3 레인지
# range(n) : 0부터 n-1까지
# range(n,m) : n부터 m-1까지
# range(n, m, s) : n부터 m까지 간격으로

# a = range(5, 10, 2)
# print(list(a))

# 4.4 시퀀스에서 사용 할 수 있는 연산

# in
# a = "a"
# b = ["a", "p", "p", "l", "e"]
# c = 5
# d = range(10)
# print(a in b)
# print(c in b)

# concatenation

# a = [1, 2]
# b = [3, 4]

# print(a + b)

# 반복
# a = [1,2,3]
# print(a*5) 

# indexing
# a = "hello"
# print(a[1]) 문자열도 시퀀스데이터타입이기 때문에 가능

# slicing
# a = "hello"
# print(a[1:3]) 1부터 3-1까지 자른 값을 반환함
# c = "123456789"
# print(c[1:10:2])
# print(c[::2]) 공란은 맨처음부터 끝까지를 의미함

# 함수 
# a = [1,2,3,4,5]
# print(len(a)) len() 요소의길이를 확인하는 함수, 파이썬 내장함수
# print(a.count(1)) 요소에 개수를 세어줌, 변수의 기능메소드 호출함

# 5. 시퀀스가 아닌 자료

# 5.1 set 똑같은 요소가 없다를 전제로함
# a = {val1, val2, ...}
# a = {1,2,3,4,5}
# b = {2,4,6,8}

# print(a | b) 합집합
# print(a - b) 차집합
# print(a & b) 교집합

# a = {1,2,3,4,5,1,2,3,4,5}
# print(set(a))

# 5.2 dictionary
# a = {key : val1, key2 : val2, ...}
# key는 immutable한것만 가능

a = {}
# a = dict()

book = { 1 : "사과,", "banana" : "바나나"}
print(book[1])

b = {1:1,2:2,3:3}
print(b.keys())
print(b.values())

# 정리

# 1. 시퀀스(order)
# - String : im
# - list : mu
# - tuple : im
# - range :mu

# 2. 시퀀스가 아닌것(unordered)
# - {set} : mu
# - {dict : val} : mu