# print(dir('1'))

# 1. 문자열 메소드

# .capitalize()
greeting = 'hello my NAME is changhee'
# print(greeting.capitalize())
# print(greeting)

# .title()
# print(greeting.title())

# .upper()
# print(greeting.upper())

# .lower()
# print(greeting.lower())

# .join(interable)
a = ['hi', 'my', 'name']
# print('!!'.join(a))

# .replace(old, new[, count])
# print('woooooooow'.replace('o', '!', 3))

# .strip([chars])
str_l = '          hello \n'
str_r = 'hellohihihihihihi'
# print(str_l.strip())
# print(str_l.lstrip())
# print(str_r.rstrip('hi'))

# .find(x)
a = 'apple'
# print(a.find('p'))
# print(a.find('z'))

# .index(x)
a = 'apple'
# print(a.index('a'))
# print(a.index('z'))

# .split(x)
a = 'my_name_is_changhee'
# print(a.split('_'))

# .isXXX() => True, Fasle를 리턴한다.



# 2. 리스트 메소드

numbers = [5, 5, 5, 1, 2, 3, 4, 5, 5, 5, 5]

# .append(x)
numbers.append(6)
# print(numbers)

# .extend(iterable)
ex_numbers = [99, 100]
numbers.extend(ex_numbers)
# print(numbers)

# .insert(i, x)
numbers.insert(3, 3.5)
# print(numbers)


# .remove(x)
numbers.remove(3.5)
# print(numbers)


# .pop(i)
numbers.pop(0)
# print(numbers)


# .index(x)
# print(numbers)
# print(numbers.index(3))

# .count(x)
# print(numbers.count(5))

# .sort()
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)

# .reverse()
numbers.reverse()
# print(numbers)



# copy 같은 주소를 참조한다.

origin_list = [1, 2, 3]
copy_list = origin_list

# copy_list[0] = 100

# print(origin_list)
# print(copy_list)
# print(id(origin_list))
# print(id(copy_list))


# copy 복사 방법
a = [1, 2, 3]
# b = a[:]
b = list(a)

b[0] = 100

# print(a)
# print(b)


# copy 얕은복사
a = [1, 2, [3, 4]]
b = a[:]

b[2][0] = 100

# print(a)
# print(b)


# copy 깊은복사
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = 100

# print(a)
# print(b)


# .clear()
a = [1, 2, 3, 4]
a.clear()
# print(a)


# list comprehension

numbers = list(range(1, 11))

# 세제곱 만들기 for
result = []
for i in numbers:
    result.append(i**3)
# print(result)

# 세제곱 만들기 comp
result2 = [i**3 for i in numbers]
# print(result2)


# 짝수만 고르기 for
even_list = []
for i in numbers:
    if i % 2 == 0:
        even_list.append(i)
# print(even_list)

# 짝수만 고르기 comp
even_list2 = [i*2 for i in numbers if i % 2 == 0]
# print(even_list2)


# 연습
words = 'my name is hong'
vowels = 'aeiou'
# => my n m   s  h ng

# for
result = []
for char in words:
    if char not in vowels:
        result.append(char)

# print(''.join(result))


# comp
result2 = [char for char in words if char not in vowels]
# print(''.join(result2))



# 3. 딕셔너리 메소드

info = {
    'name': 'change',
    'location': 'seoul',
    'phone': '123-123-123',
}

# .pop(key[, default])
info.pop('phone')
# print(info)
# print(info.pop('school', 'key가 없습니다.'))
# print(info)

# .update(key=value)
info.update(name='changhee')
# print(info)

# .get(key[, default])

# print(info['name'])
# print(info.get('name'))
# # print(info['school'])
# print(info.get('school'))


# dictionary comprehension
# {1: 1, 2: 8, 3: 27}

cube_dict = {}
for i in range(1, 4):
    cube_dict[i] = i**3
# print(cube_dict)

cube_dict2 = {i: i**3 for i in range(1, 4)}
# print(cube_dict2)


# 연습
dust = {
    '서울': 100,
    '대전': 12,
    '대구': 70,
    '부산': 20,
    '제주': 0,
}

# 50이상 지역만 뽑아서 새로운 dict만들기
# for
result = {}
for k, v in dust.items():
    if v >= 50:
        result[k] = v
# print(result)

# comp
result2 = {k: v for k, v in dust.items() if v >= 50}
# print(result2)

result3 = {k: '나쁨' if v >= 50 else '좋음' for k, v in dust.items()}
# print(result3)


# 4. 세트 메소드

fruits = {'apple', 'banana', 'melon'}

# .add(x)
fruits.add('watermelon')
fruits.add('watermelon')
# print(fruits)


# .update(*objects)
fruits.update('grape')
fruits.update({'orange', 'pear'})
# print(fruits)


# .remove(x)
fruits.remove('banana')
# print(fruits)
# fruits.remove('dog')


# .discard(x)
# print(fruits.discard('dog'))


# .pop()
fruits.pop()
# print(fruits)



# 5. map(), zip(), filter()

# map(function, iterable)
number = [1, 2, 3]

number_str = map(str, number)
# print(number_str)
# print(list(number_str))


def cube(x):
    return x**3

cube_list = list(map(cube, number))
# print(cube_list)



# 1 2 3 4 5 6 7 8 9 10 => [1, 2, 3, 4, 5...]
# => 1 8 27 ... 1000

# numbers = input().split()
result = map(int, numbers)
# print(list(result))

# numbers = list(map(int, input().split()))
# print(numbers)



# zip
a_number = [1, 2, 3]
b_number = [100, 200, 300]

# print(list(zip(a_number, b_number)))


# filter(function, iterable)
# function은 참/거짓이 반환되는 함수여야함

def isodd(x):
    # if x % 2 == 1:
    #     return True
    # else:
    #     return False
    return bool(x % 2)


numbers = [1, 2, 3, 4, 5]
result = filter(isodd, numbers)
print(list(result))