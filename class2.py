# class1.py 
#1)클래스(원본) 정의
class Person:
    #초기화메서드 
    def __init__(self):
        #멤버변수 초기화 
        self.name = "default name"
        self.title = "default title"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스(복사본)을 생성
p1 = Person() 
p2 = Person() 
p1.name = "전우치"
#3)메서드 호출
p1.print() 
p2.print()
#실행시간에 추가
# Person.title = "new title"
# print(p1.title)


