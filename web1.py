# web1.py 
#웹에 데이터를 수집 
from bs4 import BeautifulSoup

#웹페이지를 로딩(함수나 메서드를 연속으로 부르는 메서드체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read() 
#검색을 할 객체(xml문서, xml) 
soup = BeautifulSoup(page, "html.parser")
#전체를 보기 
#print( soup.prettify() )
#문서 <p> 몽땅 검색 
#print( soup.find_all("p") )
#첫번째 <p>만 검색
#print( soup.find("p") )
#조건 <p class=outer-text> class키워드 
#print( soup.find_all("p", class_='outer-text') )
#내부 컨텐츠만 출력<p>컨텐츠</p> 
for item in soup.find_all("p"):
    title = item.text.strip()
    title = title.replace("\n", "")
    print(title)



