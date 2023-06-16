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
# class Person:      # = 클래스 선언
#     name = 'hong'  # = 속성

#     def hello(self):  # => 메소드 : 함수/기능
#         return self.name

# p = Person()  # 인스턴스화 / 객체 생성
# p.name # 속성 호출
# p.hello() # 메소드 호출

# self : 인스턴스객체 자기자신
#   - 특별한 상황을 제외하고는 무조건 메소드 첫번째 인자로 설정
#   - 인스턴스 메소드를 실행할떄 자동으로 첫번째 인자에 인스턴스를 할당한다
# p1 = Person()


# p2 = Person()

# print(p1.name)
# p1.name = "Park"
# print(p2.name)

# 생성자, 소멸자
# def __init__(self):
#   print(생성될때 호출되는 메소드)

# def __del__(self):
#   print('소멸될떄 호출되는 메소드')


# class Person():
#     def __init__(self,name="이름없음"):
#         self.name = name
#         print('생성됨')

# # class Person():
# #     def __init__(self):
# #         print('소멸됨')
#     def set_location(self, location):
#         self.location = location

# p1 = Person('seokjun')    # Person.__init__(p1, 'seokjun') 이런식으로 작동

# print(p1.name)

# p2 = Person('Park')
# print(p2.name)

# p3 = Person()
# print(p3.name)

# 연습

class Pikachu:
    def __init__(self, name = "pikachu"):
        self.name = name
        self.level = 1
        self.hp = self.level*100

    def attack(self,opponent):
        damege = self.level * 5
        opponent.hp -= damege
p1 = Pikachu()
print(p1.level)

p2 = Pikachu('chu')
# print(p2.name)
# print(p2.level)

# p1.attack(p2)
# print(p1.hp)

# print(p2.hp)



# 연습2
# Circle 클래스

# 속성
# pi : 원주율 (3.14)

# 인스턴스 속성
# r = 반지름 (필수입력)
# x : x좌표(defaulit = 0)
# y : y좌표(default = 0)

# class Circle:

#     pi = 3.14
#     def __init__(self,r,x=0,y=0):
#         self.r = r
#         self.x = x
#         self.y = y
    
#     def center(self):
#         return (self.x, self.y)
    
#     def area(self):
#         result = self.r**2 * Circle.pi
#         return result
#     def move(self, x,y):
#         self.x = x
#         self.y = y
#         print(f"원의 중심이({x},{y}로 이동했습니다)")
    
# c1 = Circle(2,1,2)
# print(p1.area())
# c1.move(100,100)


# 클래스 변수 : 클래스 선언 블록 최상단 위치
#   -ClassName.class_variable로 접근/할당
# 인스턴스 변수 
#   - self.instance_variable 로 접근/할당

# class TestClass:
#     class_variable = '클래스변수'

#     def __init__(self,arg):
#         self.instance_variable = arg

# 인스턴스 메소드
# class ClassName:
#   def func():
#    pass

# 클래스 메소드
# class ClassName:
#   @classmethod:
#       def func():
#            pass
 
# static method
# class ClassName:
#   @staticmethod:
#       def func():
#            pass
 

class MyClass:
    def instance_method(self):
        return self
    
    @classmethod
    def class_method(cls):
        return cls
    
    @staticmethod
    def static_method(arg):
        return arg

m1 = MyClass()
# print(m1.instance_method())
# print(m1.class_method())
# print(MyClass.class_method)
# print(m1.static_method('hello'))


# 연습 

class Puppy:
    num_of_dogs = 0

    def __init__(self,name):
        self.name = name
        Puppy.num_of_dogs += 1
    @classmethod
    def get_status(cls):
        return f"현재 강아지는 {cls.num_of_dogs}마리입니다"
    @staticmethod
    def bark(str='멍멍'):
        return '멍멍'

p1 = Puppy('인절미')
p2 = Puppy('초코')
# print(Puppy.get_status)
# print(p1.bark())
# print(p2.bark('그르릉'))

class Person:
    population = 0
    def __init__(self,name):
        self.name = name
        Person.population += 1
    def greeting(self):
        print(f"안녕하세여{self.name}입니다")

p1 = Person('홍길동')
p1.greeting()

class Student(Person):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        Person.population += 1

s1 = Student('이순신','12345')
s1.greeting()


class Soldier(Person):
    # method overriding
    def greeting(self):
        print('충성!!')

s2 = Soldier('국방이')
s2.greeting()

# super
class Person():
    def __init__(self,email,phone,location,name):
        self.email = email
        self.phone = phone
        self.location = location
        self.name = name

class Student(Person):
    def __init__(self,email,phone,location,name,id):
        self.email = email
        self.phone = phone
        self.location = location
        self.name = name
        self.id = id

class Soldier(Person):
    def __init__(self,email,phone,location,name,id):
        super().__init__(email,phone,location,name)
        self.id = id


# 다중상속  : 메소드 혹은 속성이 겹치면 첫번째 부모에게 상속받음

class Person():
    def __init__(self,name):
        self.name = name
    
    def breath(self):
        print('후하')

class Mom(Person):
    gene = 'XX'
    def swim(self):
        print('아푸아푸')
class Dad(Person):
    gene = "XY"
    def run(self):
        print('다다다')
class FirstBaby(Mom,Dad):
    pass
class SecondBaby(Dad,Mom):
    pass

b1 = FirstBaby('첫째')
b1.swim
b1.run
print(b1.gene)

b2 = SecondBaby('둘째')
b2.swim
b2.run
print(b2.gene)

class Pokemon():
    my_skill = []
    w_skill_list = ["pump","wave"]
    f_skill_list = ["fireball", "upperFire"]

    def __init__(self,type_name):
        self.level = 1
        self.hp = self.level*100
        self.exp = 0
        self.type_name = type_name
        if self.type_name == "불":
            self.my_skill = self.f_skill_list
        else :
            self.my_skill = self.w_skill_list
    
    def attack(self,opponent,skill_name) :
        print(f"{skill_name}을 사용했다!")
        if skill_name == self.my_skill[0]:
            damege = 10 
        else :
            damege = 20
        opponent.hp -= damege
        return opponent.hp
    
    def combat(self,opponent,skill_name="아무일도 일어나지 않았다"):
        self.attack(opponent,skill_name)
        if opponent.hp <= 0:
            print("적이 쓰러졌다")
        else:
            print(f"{opponent.hp}남았다")


    def check_hp(self):
        return True if self.hp <= 0 else False

    
class WaterPokemon(Pokemon) : 
    pass

class FirePokemon(Pokemon):

    pass
kobugi = WaterPokemon("물")
pairi = FirePokemon("불")

kobugi.attack(pairi,"pump")