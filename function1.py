# function1.py
#1)함수를 정의
def setValue(newValue):
    #지역변수 초기화
    x = newValue
    print("지역변수 x:", x)

#2)함수 호출
result = setValue(5)
print(result)

#함수 정의
def swap(x,y):
    return y,x 

#호출
print( swap(3,4) )

#디버깅 연습을 위한 교집합 문자 리턴 함수
def intersect(prelist, postlist):
    #지역변수로 list에 모아두기
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#호출
print( intersect("HAM", "SPAM") )

