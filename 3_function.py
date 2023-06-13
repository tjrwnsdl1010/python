# 함수

height = 100
width = 50
# 사각형의 들레: 300, 넓이 500입니다.
permeter = (height+width)*2
area = height*width
# print(f"사각형의 둘레: {permeter}, 넓이 {area}입니다")


# 함수의 선언
# parameter = 매개변수
# def func(parameter1, parmeter2, ...):
#   code line1
#   code line2  
#   ...
#   return value 

# def rectangle(height, width):
#     permeter = 2*(height+width)
#     area = height * width

#     print(f"사각형의 둘레: {permeter}, 넓이 {area}입니다")

# 함수의 호출
# func(params1, params2)

# rectangle(100,100)
# rectangle(200,100)

# 3. 연습

# print(max(1,5))

# def my_max(n1,n2):
#     if n1 > n2:
#         print(n1)
#     elif n1 < n2:
#         print(n2)
#     else:
#         print("same")

# my_max(10,10)

# return

# def my_max(n1,n2):
#     if n1 > n2:
#         return n1
#     elif n1 < n2:
#         return n2
#     else:
#         return n1

# result = my_max(10,10)
# print(result)

# 5. 인자 (parameter)

# 5.1 위치 인자

# def cylinder(r,h):
#     return r**2 * h *3.14
# print(cylinder(5,10))

# 5.2 기본값
# def func(args = value) 위치 인자 맨뒤에 두어야함 {func(n1="",n2) [x]}
# def greeting(name, location= "이름없음"):
#     print(f"{name}님이 {location}에서 접속하셨습니다.")

# greeting("박석준")
# greeting()

# 키원드 인자
# greeting(name = "박석준", location = "인천")

# print 함수

# 5.3 가변 인자 리스트
# def func(*args):
#   code
#   return


# def my_max(*numbers):
#     result = 0
    

#     for idx, number in enumerate(numbers):
#     #만약 for문에 첫번째 라면 제일 큰수로 설정
#         if idx == 0:
#             result = number
#         else:
#             if result < number:
#                 result = number
#     return result

#     return result
        
    
# result = my_max(1,2,3,4,5)
# print(result)

# result = my_max(-1,-2,-3,-4,-5)
# print(result)

# 5.4 정의되지 않는 키워드 인자 처리

# def func(**kwargs):
#   code ...

def fake_dict(**kwargs):
    result = []
    for k,v in kwargs.items():
        result.append(f"{k}: {v}")
    print(result)
# fake_dict(name= "박석준", location= "인천")

def user(username, password, password_confirm):
    if password == password_confirm:
        print(f"{username}님 회원가입이 완료되었습니다")
    else :
        print("비번틀림")

user("홍길동", "1234", "12345")

my_user = {
    "username" : "이순신",
    "password" : "1234",
    "password_confirm" : "12345"
}
user(**my_user)