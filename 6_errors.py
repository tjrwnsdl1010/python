# Error

# 1. syntax error : 문법오류
# if True:
#     pass
# else

# print('hi)

# if True print('hello') : 대충 이쯤 오류난거니까 맹신하지말자

# 2. exception(예외)

# ZeroDivisionError
# print(5/0)

# NameError
# print(my_name)

# TypeError
# print(1+'1')
# print('1'+ 1) # 뒤에 오는것에 따라 에러표기함


import random
# missing 1 required positional argument: 'k'
# random.sample([1,2])
# takes 3 positional arguments but 7 were given
# random.sample([1,2],1,1,1,1,1,)

# ValueError
# int('3,3')

# numbers = [1,2,3]
# numbers.index(100)

# IndexError : list index out of range
# numbers = [1,2,3]
# numbers[100]

# KeyError
# my_dict = {'apple' : '사과','banana' : '바나나'}
# my_dict = ['melon']

#ModuleNotFoundError
# import asdf

# ImportError
# from datetime import asdf

# KeyboardInterrupt (ctrl+ c로 종료)
# while True:
#     continue

# 3. 예외 처리

# try - except
# try:
#   code
# except 예외:
#   code

# try:
#     num = int(input('숫자를 입력해주세요 : '))  
#     print(f'입력하신 숫자의 제곱은 {num**2}입니다')
# except ValueError:
#     print(f'숫자를 입력해!')

# try 
# try:
#   code
# except (예외1, 예외2):
#   code

# try:
#     num = input('나눌 값을 입력해주세요 : ')
#     100/int(num)
# except(ValueError, ZeroDivisionError):
#     print('문제 발생')

# try:
#     num = input('나눌 값을 입력해주세요 : ')
#     100/int(num)
# except ValueError:
#     print('입력한 정보는 숫자가 아닙니다')
# except ZeroDivisionError:
#     print('수학적으로 0으로 나누는것은 불가능합니다')


# try:
#     my_list = []
#     print(my_list[5])
# except IndexError as err:
#     print(f'{err}가 발생했습니다')


# try:
#     my_list = [1,2,3]
#     print(my_list)
# except IndexError:
#     print('인덱스 에러')
# else:                               # 에러가 발생하지 않으면 실행됨
#     print(my_list[2] * 100)


# try:
#     my_list = [1,2,3]
#     print[my_list[2]]
# except IndexError:
#     print('인덱스 에러')
# finally:                            # 오류가 있던 없든 강제적으로 실행됨
#     print('finally')


# raise ValueError('테스트입니다')


# 연습
# 양의 정수 두개를 받아 몫과 나머지로 출력하는 함수를 정의

def my_div(a,b):
    try:
        result1 = a//b
        result2 = a%b
    except ZeroDivisionError:
        print('0으로 나눌 수 없습니다')
    except: 
        print('숫자를 입력해야합니다.')
    else:
        return (result1, result2)

my_div(1,0)
my_div('1','5')
print(my_div(6,2))    