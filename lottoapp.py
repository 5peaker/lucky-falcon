import sys, math, random, warnings
import pandas as pd

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

df = pd.read_csv('lotto_after_refining.csv')

# 경고 메시지 무시 
warnings.filterwarnings("ignore", message="To exit: use 'exit', 'quit', or Ctrl-D.")

# 기계에게 학습시키지 않고 랜덤으로 숫자를 뱉게 함 (어차피 복권번호는 독립시행이므로)

# 번호 생성 함수를 포함하는 클래스 
class LottoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.generated_numbers_list = []
        self.initUI()
        
    # UI 초기화 함수    
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

    # 임의의 로또 번호를 생성하는 함수
    def generateNumbers(self):
        numbers = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
        numbers.sort()  # 선택된 숫자 정렬
        self.lottoLabel.setText('Lotto Numbers: ' + ', '.join(map(str, numbers)))  # 레이블에 표시
        self.generated_numbers_list.append(numbers)  # 생성된 파일들을 리스트에 더함 
    
        df = pd.DataFrame(self.generated_numbers_list, columns=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"])
    
        # 기존 파일에 존재하는 열을 체크함 
        try:
            existing_df = pd.read_csv('generated_lotto_numbers.csv', names=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"], usecols=[0, 1, 2, 3, 4, 5])
            total_rows = len(existing_df) + len(df)
        
        # 파일의 열 수가 1100개를 넘어가면 가장 오래된 열을 제거 
            if total_rows > 1100:
                rows_to_remove = total_rows - 1100
                existing_df = existing_df.iloc[rows_to_remove:]
            
            updated_df = pd.concat([existing_df, df])
        except FileNotFoundError:
            updated_df = df
    
        # 업데이트된 csv 파일을 저장 
        updated_df.to_csv('generated_lotto_numbers.csv', mode='w', header=False, index=False)
    
        self.compare_csv()
    
    #  생성된 파일을 csv 파일과 비교하여 몇 개가 맞았는지 퍼센트로 출력
    def compare_csv(self):
        try:
            generated_df = pd.read_csv('generated_lotto_numbers.csv', names=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"], usecols=[0, 1, 2, 3, 4, 5])
        except pd.errors.ParserError as e:
            print(f'Error while reading generated_lotto_numbers.csv: {e}')
            return

        try:
            data = pd.read_csv('lotto_after_refining.csv', names=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"], usecols=[0, 1, 2, 3, 4, 5])
        except pd.errors.ParserError as e:
            print(f'Error while reading lotto_after_refining.csv: {e}')
            return

        identical_counts = []

        for column in generated_df.columns:
            identical_count = (generated_df[column] == data[column]).sum()
            identical_counts.append(identical_count)
            print(f'Identical rows in column {column}: {identical_count}')

        return identical_counts

# 메인 함수 실행
def main():
    app = QApplication(sys.argv)
    exe = LottoApp()
    exe.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()