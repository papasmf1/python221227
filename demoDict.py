# demoDict.py 
device = {"아이폰":5, "아이패드":10, "윈도우타블렛":15}
print( type(device) )
print( device )
#검색
print( device["아이패드"] )
#입력
device["맥북"] = 20 
print( device )
#수정
device["아이폰"] = 6
print( device )
#삭제
del device["아이폰"] 
print( device )

#참조만 복사
device2 = device 
device2["에어팟"] = 3 
print( device )
print( device2 )
print( id(device), id(device2) )

print("---items()---")
#중단점(Break Point) 디버깅할 때 잠시 멈추기 
for item in device.items():
    print(item)

print("---keys()---")
for item in device.keys():
    print(item)

print("---values()---")
for item in device.values():
    print(item)

print("---bool---")
print( bool(0) )
print( bool("") )
print( bool([]) )
print( bool(3) )
print( bool("test") )
print( bool([1,2,3]) )
isRight = True 
print( type(isRight) )
print( 1 < 2 )
print( 1 != 2 )
print( True and True and True )
print( True and True and False )
print( True or False or False ) 
print("---나누기연산---")
print(5/2)
print(5//2)
print(5%2)

