import sys, math, random, warnings
import pandas as pd

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
warnings.filterwarnings("ignore", message="To exit: use 'exit', 'quit', or Ctrl-D.")

"""
Disclaimer: This code is not working.
It was impossible to reach the initial goal of the code.
See the comments below for more information.
"""

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
        
        self.generatedNumbersLabel = QLabel('Generated Numbers:', self)

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.addWidget(self.btn)
        layout.addWidget(self.lottoLabel)
        layout.addWidget(self.generatedNumbersLabel)
        self.setLayout(layout)

    def read_csv_file(self):
        try:
            old_df = pd.read_csv("lotto_after_refining.csv")
            return old_df
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return None
        
    def generateNumbers(self, number):
        generated_numbers_list = []
        for i in range(number):
            cnt = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
            cnt.sort()  # 선택된 숫자 정렬
            generated_numbers_list.append(cnt)  # 생성된 파일들을 리스트에 더함 
        return generated_numbers_list   

    def make_new_df(self, generated_numbers_list):
        new_df = pd.DataFrame(generated_numbers_list, columns=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"])
        return new_df

    def calculate_match_rate(self, old_df, new_df):
        match_count = 0
        for i in range(len(old_df)):
            for j in range(len(new_df)):
                if any(old_df.iloc[i] == new_df.iloc[j]):
                    match_count += 1
                    break
        return match_count

"""
It was possible to generate 6(six) random numbers as the real Lotto 
It was also possible to compare the generated numbers with the real Lotto numbers
However, every number of Lotto is drawn by the human hand, without any pattern or machine help
It is meaningless to calculate winning rate of each number
It is IMPOSSIBLE to calculate what numbers will be drawn in the next Lotto
"""
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LottoApp()
    ex.show()
    sys.exit(app.exec_())