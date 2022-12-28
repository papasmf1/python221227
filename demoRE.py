# demoRE.py
#정규표현식(특정한 패턴, 규칙)
import re 
#처음부터 끝까지 지독하게 패턴을 검색 
result = re.search("[0-9]*th", "35th")
#매칭 오브젝트(문자열이 아니다!)
print( result )
print( result.group() )

#정확한 패턴을 일치하는 경우
result = re.match("[0-9]th", "35th")
print( result )
print( result.group() )


