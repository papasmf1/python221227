# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 작업 
    def __init__(self, id, name, balance):
        #클래스 내부에 이름 숨김
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금 메서드 
    def deposit(self, amount):
        self.__balance += amount 
    #출금 메서드 
    def withdraw(self, amount):
        self.__balance -= amount
    #객체 문자열 리턴(toString())
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#외부에서 접근(테스트, 백도어): _클래스명__balance
print(account1._BankAccount__balance)

