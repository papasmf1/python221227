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
        #부모의 초기화 메서드 호출
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #상속받아서 재정의
    def printInfo(self):
        print("Info(이름:{0}, 핸드폰: {1})".format(self.name, 
            self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, 
            self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "데이터사이언스", "201234")
#문제점 
p.printInfo()
s.printInfo()


