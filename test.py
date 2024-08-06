import pandas as pd
import sys, math, random, warnings

# 1. 기존의 로또 번호 데이터를 csv 파일을 읽어서 df으로 만들기
def read_csv_file():
    old_df = pd.read_csv("lotto_after_refining.csv")
    return old_df

# 2. 랜덤 로또 번호를 생성하는 함수 만들기 (매개변수로 원하는 개수를 받기, 리턴값은 리스트)
def generatedNumbers(number):
    generated_numbers_list = []
    for i in range(number):
        cnt = random.sample(range(1, 46), 6)  # 1부터 45까지의 숫자 중 6개를 무작위로 선택
        cnt.sort()  # 선택된 숫자 정렬
        generated_numbers_list.append(cnt)  # 생성된 파일들을 리스트에 더함 
    return generated_numbers_list

# 3. 2번의 생성된 리스트를 반환 받아서 새로운 df를 만들고
def make_new_df(generated_numbers_list):
    new_df = pd.DataFrame(generated_numbers_list, columns=["첫번째", "두번째", "세번째", "네번째", "다섯번째", "여섯번째"])
    return new_df

# 4. 기존 로또 df, 새로운 로또 df 매개변수로 입력 받아서 승률 비교해서 계산값을 리턴하는 함수 만들기
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
