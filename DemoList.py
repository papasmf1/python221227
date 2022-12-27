# DemoList.py 
colors = ["red","green","blue"]
print(colors)
print( type(colors) )
#입력
colors.append("white")
print(colors)
colors.insert(1, "yellow")
colors += "red"
print(colors)
#삭제
print( colors.pop() )
print( colors.pop() )
print(colors)
#삭제할 때 remove()
colors += ["red"]
count = colors.count("red")
for i in range(count):
    colors.remove("red")

print("---결과---")
print(colors)

#set
a = {1,2,3,3}
b = {2,3,3,4}
print( a )
print( b )
print( a.union(b) )
print( a.intersection(b) )

print("---tuple---")
args = (2,3)
#함수 정의(튜플에 담아서 리턴)
def times(a,b):
    return a+b, a*b 

print( times(*args) )
result = times(3,4)
print(result[0])
print(result[1])

print("---형식변환(type casting)---")
a = set((1,2,3))
print( type(a) )
b = list(a)
b.append(4)
print( type(b) )
print( b )






