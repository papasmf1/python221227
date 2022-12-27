# demoLoop.py 
#다중 라인 주석처리:ctrl+/
# score = int(input("점수를 입력:"))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5 
while value > 0:
    print(value)
    value -= 1 

d = {"apple":100, "orange":200, "banana":300}
for item in d.items():
    print(item)

print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("---continue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

print("---수열함수---")
print( list(range(10)) )
print( list(range(2000, 2023)) )
print( list(range(1,32)) )

print("---리스트 내장---")
#파이썬스럽다! 
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )

d = {100:"apple", 200:"banana", 300:"kiwi"}
print( [v.upper() for v in d.values()] )

print("---필터링---")
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

#함수 정의(이름 규칙 사용)
def getBiggerThan20(i):
    return i > 20 

print("---필터링함수---")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다함수---")
iterL = filter(lambda i:i>20, lst)
for item in iterL:
    print(item)

