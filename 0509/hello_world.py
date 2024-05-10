# JAVA와 다르게 데이터 타입을 선언하지 않아도 된다
# print("HELLO !")
n = 10
# print(n)
n = "hello ~~"
# print(n)
n = 1.2
n = "today Thursday"
# print(n)

message = 'hello\'s python'
print(message)

name = "ada lovelace"
print(name.capitalize()) #문장의 첫글자
print(name.title()) #단어의 첫글자

number = 10
print(number.as_integer_ratio())
#같은 변수명(name)이어도 값에 따라 뒤에 추천하는 함수(문자열일땐 .title(), 숫자 일땐 .as_integer_ratio())가 다르게 나타난다 

first_name = " DDU "
last_name = " Jang "
full_name = f"{last_name.strip()} {first_name.strip()}" #f-문자열 #.strip() : 공백제거
print(full_name)