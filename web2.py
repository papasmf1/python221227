# web2.py
#웹서버에 페이지 실행을 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

data = urllib.request.urlopen(
    "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")

soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
print("갯수:{0}".format( len(cartoons) ))
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

# <td class="title">
#   <a href="/webtoon/detaili">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
for item in cartoons:
    title = item.find("a").text.strip()
    print(title)


