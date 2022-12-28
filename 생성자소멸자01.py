# -*- 생성자와 소멸자 -*-
class MyClass:
    #초기화메서드(생성자)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소멸자메서드(마지막 정리)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스
d = MyClass(5)
#명시적으로 인스턴스 삭제 
#del d 

print("전체 코드 실행 종료")



