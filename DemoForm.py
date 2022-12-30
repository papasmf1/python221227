# DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#폼 클래스(윈도우를 정의)
class DemoForm(QDialog, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모~~")

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