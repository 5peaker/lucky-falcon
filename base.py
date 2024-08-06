import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

class LottoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Lotto Number Generator')
        self.setGeometry(300, 300, 300, 200)

        # 버튼 생성
        self.btn = QPushButton('Generate Lotto Numbers', self)
        self.btn.clicked.connect(self.generateNumbers)

        # 로또 번호를 표시할 레이블 생성
        self.lottoLabel = QLabel('', self)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.lottoLabel)

        self.setLayout(layout)

    def generateNumbers(self):
        numbers = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
        numbers.sort()  # 선택된 숫자 정렬
        self.lottoLabel.setText('Lotto Numbers: ' + ', '.join(map(str, numbers)))  # 레이블에 표시

def main():
    app = QApplication(sys.argv)
    ex = LottoApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()