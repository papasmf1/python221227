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


