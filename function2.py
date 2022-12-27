# function2.py
print("---불변형식---")
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

print("---입력+출력---")
def change(x):
    x[0] = "H"

wordlist = ["J","A","M"]
change(wordlist)
print("호출후:", wordlist)

print("---수정된 코드---")
def change(x):
    #복사본을 생성(Deep copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

wordlist = ["J","A","M"]
change(wordlist)
print("호출후:", wordlist)

#리스트가 아닌 경우를 Deep copy하는 경우(기본은 Shallow copy)
import copy 

lst = [100,200,300]
lst2 = copy.deepcopy(lst)
lst2[0] = 101 
print( lst )
print( lst2 )
print( id(lst), id(lst2) )

#함수내부의 이름 해석 순서(Local, Global, Built-in: LGB) 
#전역변수
x = 5 
def func(a):
    return x+a 

#호출
print( func(1) )

def func2(a):
    #지역변수 
    x = 10
    return x+a 
    
#호출
print( func2(1) )
