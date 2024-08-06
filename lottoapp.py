import sys, math, random, warnings
import pandas as pd

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

# 경고 메시지 무시 
warnings.filterwarnings("ignore", message="To exit: use 'exit', 'quit', or Ctrl-D.")

def read_csv_file():
    old_df = pd.read_csv("lotto_after_refining.csv")
    return old_df

def generatedNumbers(number):
    generated_numbers_list = []
    for i in range(number):
        cnt = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
        cnt.sort()  # 선택된 숫자 정렬
        generated_numbers_list.append(cnt)  # 생성된 파일들을 리스트에 더함 
    return generated_numbers_list

def make_new_df(generated_numbers_list):
    new_df = pd.DataFrame(generated_numbers_list, columns=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"])
    return new_df

def calculate_match_rate(old_df, new_df):
    match_count = 0
    for i in range(len(old_df)):
        for j in range(len(new_df)):
            if any(old_df.iloc[i] == new_df.iloc[j]):
                match_count += 1
                break
    return match_count

def main():
    generated_numbers_list = generatedNumbers(100)
    old_df = read_csv_file()
    new_df = make_new_df(generated_numbers_list)
    match_count = calculate_match_rate(old_df, new_df)
    print(f"맞은 개수: {match_count}")

if __name__ == "__main__":
    main()