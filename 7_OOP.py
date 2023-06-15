# 객체지향 프로그래밍
# - 클래스(class) : 같은 종류의 집단에 속하는 속성(attribute)과 행위(method)를 정의한것
# - 인스턴스(instance) : 클래스를 실제로 메모리상에 할당한 것
# - 속성(arrtibute) : 클래스/인스턴스가 가지고 있는 데이터 / 값
# - 행위(method) : 클래스/인스턴스 가지고 있는 함수/기능

# number = 1+2j
# print(type(number))

# print(number.real)
# print(number.imag)

# my_list = [1,4,2,3]
# my_list.sort()
# print(type(my_list))



# 클래스가 없다면

# power = False
# number = "010-1234-1234"
# book = {
#     '박석준' : "010-2345-2345",
#     '이순신' : '010-2341-2341'
# }
# model = 'iphon'

# def on():
#     global power
#     if power == False:
#         power = True
#         print('폰이 켜짐')
# def off():
#     global power
#     if power == True:
#         power = False
#         print('폰이 꺼짐')
# def set_my_number(n):
#     number = n

# on()
# off()

# 클래스
# class ClassName:
#   attribute
#   method

# 선언
class TestClass:
    a = 1

    def b(self):
        print('b')

# 인스턴스화
class_a = TestClass
# print(class_a.a)
# class_a.b()

# 클래스가 있다면
class Phone:
    power = False
    number = '010-0000-0000'
    book = {}
    model = ''

    def on(self):
        if self.power == False:
            self.power = True

    def off(self):
        if self.power ==True:
            self.power = False
    
    def call(self, target):
        if self.power == True:
            print(f'내번호는 {self.number}')
            print(f'{target} 전화거는중')
        else:
            print('핸드폰을 켜주세여')


# my_phone = Phone()
# your_phone = Phone()

# my_phone.on()
# print(my_phone.power)
# print(your_phone.power)
# my_phone.call("010-2222-2222")
# your_phone.call('010-1111-1111')


p1 =Phone()
Phone.on(p1)

# 연습
class MyList:
    data = []

    def append(self, item):
        self.data += [item]

    # data 안에 맨 마지막요소를 삭제하고, 삭제된 요소 하나를 리턴
    def pop(self):
        num = self.data[-1]
        self.data = self.data[:-1]
        return num

list_a = MyList()
print(list_a.data)
list_a.append(123)
list_a.append(456)
list_a.append(789)
print(list_a.data)
list_a.pop()
print(list_a.data)

# 정리 
class Person:      # = 클래스 선언
    name = 'hong'  # = 속성

    def hello(self):  # => 메소드 : 함수/기능
        return self.name

p = Person()  # 인스턴스화 / 객체 생성
p.name # 속성 호출
p.hello() # 메소드 호출