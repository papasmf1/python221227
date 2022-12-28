# demoFile.py

url = "http://www.ycampus.co.kr/?page=" + str(1) 
print( url )

#출력포맷
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3)) 

print("---오른쪽정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3)) 

print("---서식지정문자---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.3f}".format(4/3))

#파일을 쓰기 
f = open("c:\\work\\demo.txt", "wt")
f.write("한줄쓰기\n")
f.close() 

