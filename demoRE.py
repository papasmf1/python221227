# demoRE.py
#정규표현식(특정한 패턴, 규칙)
import re 
#처음부터 끝까지 지독하게 패턴을 검색 
result = re.search("[0-9]*th", "  35th")
#매칭 오브젝트(문자열이 아니다!)
print( result )
print( result.group() )

#정확한 패턴을 일치하는 경우
# result = re.match("[0-9]*th", "  35th")
# print( result )
# print( result.group() )

result = re.search("apple", "this is Apple".lower() )
print( result.group() )
result = re.search("\d{4}", "올해는 2022년입니다.")
print( result.group() )

result = re.search("\d{5}", "우리 동네는 52123")
print( result.group() )

print("---다중 라인---")
s = """이 문자열은
다음과 같이

빈줄도 있습니다. """
#^시작할때 .글자하나 +하나라도(출현회수)
c = re.compile("^.+", re.M)
print( c.findall(s) )
