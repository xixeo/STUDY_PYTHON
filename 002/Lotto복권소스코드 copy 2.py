import random
# 로또 복권 번호 생성 함수
def generate_lotto_numbers():
    # 1부터 45까지의 숫자 리스트 생성
    numbers = list(range(1, 46))    
    # 무작위로 숫자 6개 선택하여 세트로 변환 (중복 없음)
    lotto_numbers = set(random.sample(numbers, 6))    
    # 무작위로 숫자 1개 선택하여 보너스 번호 생성
    bonus_number = random.choice(numbers)    
    return lotto_numbers, bonus_number

def generate_lotto_list(num_list):
    lotto_list = []
    for _ in range(num_list):
        lotto_numbers, lotto_bonus_number = generate_lotto_numbers()
        lotto_list.append((lotto_numbers, lotto_bonus_number))
    return lotto_list  

def check_winner(lotto_list, winning_numbers, winning_bonus_number):
    for idx, (lotto_numbers, lotto_bonus_number) in enumerate(lotto_list, 1):
    # 100장 복권을 가져와 당첨번호와 비교
        if lotto_numbers == winning_numbers and lotto_bonus_number == winning_bonus_number:
            print(f"{idx}번째 로또 복권: 1등 당첨!")
        elif lotto_numbers == winning_numbers:
            print(f"{idx}번째 로또 복권: 2등 당첨! (보너스 번호 불일치)")
        elif lotto_bonus_number == winning_bonus_number:
            print(f"{idx}번째 로또 복권: 3등 당첨! (5개 일치 + 보너스 번호 일치)")
        elif len(lotto_numbers.intersection(winning_numbers)) == 5:
            print(f"{idx}번째 로또 복권: 4등 당첨! (5개 일치)")
        elif len(lotto_numbers.intersection(winning_numbers)) == 4:
            print(f"{idx}번째 로또 복권: 5등 당첨! (4개 일치)")
        else:
            print(f"{idx}번째 로또 복권: 꽝")

lotto_list = generate_lotto_list(5)

# 당첨 번호 생성
winning_numbers, winning_bonus_number = generate_lotto_numbers()
print("당첨 번호:", winning_numbers, "보너스 번호:", winning_bonus_number)

check_winner(lotto_list, winning_numbers, winning_bonus_number)
