#부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))

#자식 클래스 
class Student(Person):
    #상속받아서 내가 원하는 로직으로 덮어쓰기(재정의,override)
    def __init__(self, name, phoneNumber, subject, studentID):
        self.name = name
        self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "데이터사이언스", "201234")
print(p.__dict__)
print(s.__dict__)


