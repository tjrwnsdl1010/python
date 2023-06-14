# 1. 문자열 메소드

# .capitalize() : 첫번째 글짜를 대문자로 바꿈 저장은 안함
# greeting  = 'hello my name is seokjun'
# print(greeting.capitalize())
# print(greeting)

# .title()
# print(greeting.title())

# .upper()
# print(greeting.upper())

# .lower()
# print(greeting.lower())

# .join(interable)
# a = ['hi','my','name']
# print(''.join(a))

# .replace(old, new[, count])
print('wow'.replace('0','!',3))

# .strip([chars])
str_1 = '        hello  \n'
# str_r = 'hellohihihihhhihihi'
# print(str_1.lstrip())
# print(str_1.rstrip('hi')) # 오른쪽부터 'hi'를 다 지움

# .find(x) : 문자열 찾기 에러를 -1로 알려줌
# a = 'apple'
# print(a.find('p'))
# print(a.find('z')) #범위안에 없는 문자열이라 에러남

# .index(x)
# a = 'apple'
# print(a.index('a'))
# print(a.index('z'))

# .split()
a = 'my name is seokjun'
print(a.split(' '))

# .isXXX => 확인, 참 거짓을 반환

# 2. 리스트 메소드
numbers = [5,5,5,1,2,3,4,5,5,5,5,5,5]
# .append(x)
numbers.append(6)
# print(numbers)


# .extend(iterable)
ex_nuber = [99,100]
numbers.extend(ex_nuber)
print(numbers)

# .insert(i, x)
numbers.insert(3, 3.5)
# print(numbers)

# .remove(x)
numbers.remove(3.5)
# print(numbers)
# numbers.remove(3.5) # 없는데 삭제하려하면 오류남

# .pop(i) : 인덱스 번호로 요소를 삭제함
numbers.pop(0)
# print(numbers)

# .index()
# print(numbers.index(3))
# print(numbers)

# .count(x) : x와 같은 요소 개수를 반환
print(numbers.count(5))

# .sort() 오름차순으로 정렬
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True) # 내림차순으로 정렬
# print(numbers)

# .reverse() : 배열의 앞과 뒤를 바꿈
# numbers.reverse()
# print(numbers)

# .copy : 같은 주소를 참조한다.

# origin_list = [1,2,3]
# copy_list = origin_list

# copy_list[0] = 100

# print(origin_list)
# print(copy_list)
# print(id(origin_list))
# print(id(copy_list))

# copy 복사 방법
# a = [1,2,3]
# b = a[:]
# b = list(a)
# b[0] = 100

# print(a)
# print(b)

# copy 얕은 복사
# a = [1,2,[3,4]]
# b = a[:]

# b[2][0]
# print[a]
# print[b]


# COPY 깊은 복사
# import copy
# a = [1,2,[3,4]]
# b = copy.deepcopy(a)

# b[2][0] = 100

# .clear() : 요소가 다 지워짐
# a = [1,2,3,4,]
# a.clear
# print(a)

# list comperration

# numbers = list(range(1,11))
# 세제곱 만들기 for
# result = []
# for i in numbers:
#     result.append(i**3)

# print(result)

# result2 = [i**3 for i in numbers]
# print(result2)

# 짝수만 고르기 for
# even_list = []
# for i in numbers:
#     if i % 2 == 0:
#         even_list.append(i)
# print(even_list)

# 짝수만 고르기 comp
# even_list2 = [i for i in numbers if i%2 == 0]
# print(even_list2)

# 연습
# words = 'my name is park'
# vowels = 'aeiou'

# 모음 제거하기
# for char in words:
#     if char not in vowels:
#         result.append(char)
    
# print(''.join(result))

# comp
# result2 = [char for char in words if char not in vowels]
# print(result2)

# 딕셔너리 메소드

# info = {
#     'name' : 'change',
#     'locatoin' : 'location',
#     'phone' : '123-123-123',
# }

# .pop(key[, default])
# info.pop('phon')
# print(info)
# print(info.pop('school', 'key가 없습니다'))
# print(info)

# .update()
# info.update(name='seok')
# # print(info)

# # .get(key[, default])
# print(info["name"])
# print(info.get('name'))

#  #dictionary comperation

# cube_dict = {}
# for i in range(1,4):
#     cube_dict[i] = i**3
# print(cube_dict)

# cube_dict2 = {i: i**3 for i in range(1,4)}

# 연습
dust = {
    '서울' : 100,
    '대전' : 12,
    '대구' : 70,
    '부산' : 20,
    '제주' : 0,
}

# 50 이상 지약만 뽑아서 새로운 dict 만들기
# for
f_dict = {}
for i, x in dust.items():
    if x >= 50:
        f_dict[i] = x
print(f_dict)

#comp
result2 = {x : i for i,x in dust.items() if x >= 50}
print(result2)

result3 = {x: '나쁨' if x >= 50 else '좋음' for i,x in dust.items()}
print(result3)


# 4. 세트 메소드 : {}이루어짐, 집합, 순서가 없음, 중복된 데이터가 없음

fruits = {'apple', 'banana','melon'}

# .add()
fruits.add('watermelon')
fruits.add('watermelon')
# print(fruits)

# .update(*object)
fruits.update('grape')
fruits.update({'orange','pear'})
# print(fruits)

# .remove(x) : 없는데이터를 지울때 에러남
fruits.remove('banana')
# print(fruits)

# .discard(x) : 없어도 에러안남
# print(fruits.discard('dog'))

# 5. map(), zip(), filter()

# map(function, iterable)
number = [1,2,3]

number_str = map(str, number)
# print(number_str)
# print(list(number_str))

def cube(x):
    return x**3

print(cube(3))

cube_list = list(map(cube, number))
# print(cube_list)

s
# 1 2 3 4 5 6 7 8 9 10
#=> 1 8 27 ... 1000

numbers = input().split()
result = map(int, numbers)
print(list(result))

result = list(map(int, numbers))

#zip 같은 인덱스의 자리를 튜플 형태로 합쳐줌
a_number = [1,2,3]
b_number = [100,200,300]

print(list(zip(a_number, b_number)))

# filter(func,iter)

def isodd(x):
    # if x % 2 == 1:
    #     return True
    # else:
    #     return False
    
    return bool(x % 2)

numbers = [1,2,3,4,5]
result = filter(isodd, numbers)
print(list(result))