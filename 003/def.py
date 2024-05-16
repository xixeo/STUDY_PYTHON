def modify_string(number):
  # s = s+"world"
  number = number+10 
  print(f"함수 내 출력 = {number}")

# st = "hello"
num = 10
modify_string(num)
print(f"함수 종료 후 출력 = {num}") #hello만 출력됨, 함수밖에서 st값이 변경되지 않음