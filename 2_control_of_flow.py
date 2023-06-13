# 1. if 제어문

# 1.1 조건문
# if <조건식>:
#   참인경우 실행하는 코드
# elif<조건식>:
#   elif의 조건식이 참인 경우 실행하는 코드
# else:
#   거짓인 경우 실행하는 코드

# a = 10
# if a > 5:
#     pass # 실행내역에 아무것도 없을 시 오류가 남 그래서 pass를 사용
# else:
#     pass

# 연습1
# 사용자에게 날짜입력을 받아서 크리스마스인지 확인

# a = input("날짜를 입력하세요(ex : 1/1, 12/12) : ")

# if a == "12/25":
#     print("메리크리스마스")
# else:
#     print(a+"입니다")

# 연습2
# 사용자에게 숫자하나를 입력 받아서 홀수인지 짝수인지 확인

# num = int(input("숫자를 입력해주세요 : "))
# if (num) % 2 == 1:
#     print('홀수입니다')
# else:
#     print('짝수입니다')

# if num % 2:
#     print('홀수')
# else:
#     print('짝수')

# if num % 3:
#     print("3의 배수가 아님니다")
# else:
#     print("3의 배수입니다")

# 연습3
# 사용자에게 1~100 까지 점수을 받아서
# 100~90 A, 89~80 B, 79~70 C, 나머지는 F
# 95점 이상인 사람에게는 good이라는 문장 출력
# class1 = int(input("점수를 입력해주세요"))
# if 100>= class1 >=90:
#     print("A")
#     if class1 >= 95:
#         print("good")
# elif 89>= class1 >= 80:
#     print("B")
# elif 79>= class1 >= 70:
#     print("C")
# else:
#     print("F")

# 1.2 조건표현식
# true_value if <조건식> else false_value

# num = int(input("숫자를 입력해주세요 : "))

# result = '홀수' if num % 2 else '짝수'

# num = int(input('숫자를 입력하세요'))
# value =  "0 이상" if num >= 0 else  0
# print(value)

# 1.2 반복문

# 1.2.1 while
# while 조건식이 참인 경우 반복적으로 코드를 실행

# n = 0
# while n < 5:
#     print(n+1,'아직은 5보다 작습니다')
#     n += 1

# greeting = ''
# while greeting != 'hi':
#     greeting = input('안녕! \n')

# 1.2.2 for
# for variable in sequence:
#   실행할 코드

# for i in range(5):
#     print(i)

# 연습1
# 사용자에게 영단어 하나를 입력받아서 알파벳 출력

# word = input('영단어 입력해주세요 :')
# print(word)

# for char in word:
#     print(char)

# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)

# print(number)

# 연습2
# 반복문과 조건문을 같이 사용해서 1~20까지의 숫자중에
# 홀수만 저장장된 numbers 리스트를 출력해야함

# result = []
# for i in range(1,21):
#     if i % 2 == 1:
#         result.append(i)
#     else:
#         pass

# print(result)

#연습3 
# 점심메튜 리스를 작성해서 하나씩 출력

# menus = ['라면','김밥','돈까스']

# for i in range(len(menus)):
#     print(menus[i])

# for idx, menu in enumerate(menus):
#     print(idx, menu)

# max = 0
# min = 0
# val = []
# for i in range(4):
#     num = int(input("점수를 입력해주세요"))
#     val.append(num)
#     if num > max:
#         max = num
#         min = max
#     elif num < min:
#         min = num
# print("max : ", max,"\n", "min : ", min)
# print(list(val))

# 1 2 3 dictionary 반복 

# info = {
#     "name" : "change",
#     "location" : "seoul"
# }

# # Key 반복
# for i in info:
#     print(i)
#     print(info[i])

# for key in info.keys():
#     print(key)

# 3. value 반복
# for value in info.values():
#     print(value)

# # 4. key, value 반복
# for key, value in info.items():
#     print(key,value)

# print(info.keys())

# blood_type = {
#     "A" : 10,
#     "B" : 8,
#     "C" : 5,
#     "AB" : 5
# }

# 혈액형 종류는 다음과 같습니다 ABOAB

# 1,2
# result = []
# for key in blood_type:
#     result.append(key)
# result = ", ".join(result)
# print(f"혈액형의 종류는 다음과 같습니다. {result} ")

# # 3
# result = 0
# for value in blood_type.values():
#     result = result + value
#     print(f"학생수는 {result}명 입니다")

# 4.
# for  k, v in blood_type.item():
#     print(f"{k}형은 {v}명입니다")

# 1.2.4 break

# for i in range(10):
#     print(i)
#     if i > 2:
#         print("2초과입니다")
#         break

# 연습
# 보리 =>, 쌀 = 잡았다 for 문 종료

# bori = ["보리", "보리", "보리","쌀","보리","보리"]

# for i in bori:
#     if i == "쌀":
#         print("잡았다")
#         break
#     print(i)

# 1.2.5 comtinue

# for i in range(5):
#     if i % 2:
#         continue
#     print(f"{i}는 짝수입니다.")

# 연습

# age = [6, 10, 30, 20, 60, 4]

# for i in age:
#     if i < 20:
#         print("미성년자입니다")
#         continue
#     print(f"{i}세, 성인입니다")

# 1.2.6 else

# for i in range(50):
#     print(i)

#     if i == 5:
#         print(f"{i}번쨰에서 break")
#         break
# else:
#     print("break를 만나지 않았습니다.")

# 연습


# numbers = []

# for i in range(10):
#     inp = input('숫자를 입력하세요')
#     numbers.append(inp)
#     if i == 5:
#         print("true")
#         break
# else:
#     print("false")

# 1.2.7 match


