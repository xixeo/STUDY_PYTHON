# print('helllo~')

age = 5
pie = 3.14
mask = 'woooow'
data = [1, 2, 3, 4]
data = [1, 2, 3, 4]
mask = 'everything' or 'object'

# print(type(age), type(pie), type(mask), type(data), type(mask))
#파이썬은 어떤 변수든 다 넣을 수 있다

def calc(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** b)


a = 3.14
b = 1_000_000
print(a, b)

a = 5
b = 3


# #swap : a와 b의 값을 서로 바꾸기
# 일반적인 코딩 방법으로는
# temp = a #임시변수 temp를 만들어서 바꾸기 !
# a = b
# b = temp

# 파이썬에서의 swap 방법
b, a = a, b
print(a, b)
# a, b = map(int, input().split()) #한 줄로 출력하기


PI = 3.14 #대문자로 적는건 상수값으로 쓰라는 뜻
PI = 3.15 #값을 변경 할 수는 있긴 함

msg = 'hellllo world !'
print(msg, type(msg))
print(msg.find('l'))

print(msg[1])
# msg[0] = 'H' #스트링의 중간 값을 바꿀순 없다
print(msg)

msg = 'Hellllo world !' #새로운 값을 선언해야 한다

a = 'hello'
b = 'world'
print(f'{a}+{b}\nhahahah') #f스트링 : 문자열 안에서 변수나 함수 사용 가능

msg = '   he llo        '
print(len(msg.rstrip().lstrip())) #
print(len(msg)) # 결과값은 17로, strip()한것이 반영이 되지 않는다. bcs 스트링의 중간 값을 바꿀순 없기때문
msg = len(msg.rstrip().lstrip()) # 결과값을 바꾸고 싶으면 다시 대입해주기

msg= 'hello, hello, hello, world !'
print(msg.replace('hello', '').replace(',', '').lstrip().rstrip()) #hello제거, 쉼표제거, 공백제거
print(msg)

