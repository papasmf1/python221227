# DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 페이지 실행을 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#화면을 로딩(파일이름 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스(QMainWindow를 상속)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모~~")
    def firstClick(self):
        #파일로 저장
        f = open(r"c:\work\webtoon.txt", "wt", encoding="utf-8")
        #페이징처리
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
            print( url )
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")
            for item in cartoons:
                title = item.find("a").text.strip()
                print(title)
                f.write(title + "\n")
        f.close()
        self.label.setText("네이버 웹툰 크롤링 종료~~")
    def secondClick(self):
        self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭클릭~~")

#진입점을 체크
if __name__ == "__main__":
    #실행 프로세스를 생성(Excel.exe)
    app = QApplication(sys.argv)
    #폼클래스 생성
    demoWindow = DemoForm()
    #화면에 출력
    demoWindow.show()
    #이벤트 처리 대기(실행중)
    app.exec_()