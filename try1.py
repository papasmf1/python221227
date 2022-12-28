# try1.py 
#함수 정의
def divide(a,b):
    return a/b 

try:
    #에러 처리
    result = divide(5, 2)
except ZeroDivisionError:
    print("0으로 나누면 안됩니다")
except TypeError:
    print("숫자만 연산이 가능합니다.")
else:
    print("연산결과:{0}".format(result))
finally:
    print("무조건 실행(이중으로 체크)")

print("===전체 실행 종료===")
