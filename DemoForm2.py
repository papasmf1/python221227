# DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

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
        self.label.setText("첫번째 버튼")
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