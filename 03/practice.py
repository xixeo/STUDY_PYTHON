# # 백준 2557 print
# # print('Hello World!')

# # # 백준 10869 사칙연산
# # a, b = list.map(int, input().split())
# # print(a + b)
# # print(a - b)
# # print(a * b)
# # print(a // b)
# # print(a % b)

# # 백준 10171 고양이
# # print("\    /\ " )
# # print(" )  ( ')")
# # print("(  /  )")
# # print(" \(__)|")

# # 백준 2557
# # a = int(input())
# # b = input()
# # s = 0
# # for idx, n in enumerate(b[::-1]):
# #   r = a * int(n)
# #   print(r)
# #   s += r * (10**idx)
# #   print(s)

# # 구구단 만들기
# for i in range(1, 10):
#   for j in range(1, 10):
#     print(f'{i} * {j} = {i*j}')
#   print()

# # 합계
# print(sum(range (1, 11)))

# # 최대
# print(max(range(1, 11)))

# # 최소
# print(min(range(1, 11)))

# # 평균 : sum/max
# # print(sum())

# #p102 4-1 피자
# pizzas = ['치즈', '마르게리따', '하와이안']
# for pizza in pizzas:
#   print(f'나는 {pizza}피자가 좋다')
# print('나 피자 짱 좋아해')

# #p102 4-2
# animals = ['곰', '호랑이', '악어']
# for animal in animals:
#   print(f'{animal}은(는) 무서운 동물이다')
# print('얘네는 사람을 찢어')

# data = list(range(2, 101, 2)) #짝수 만들기
# print(data, type(data))

# #p113 4-10
# players = ['charles', 'martina', 'michael', 'florence', 'eli']

# #p129
# car = 'subaru'
# print("Is car == 'subaru' ? I predict True.")
# print(car == 'subaru')

# print("\nIs car == 'audi' ? I predict False.")
# print(car == 'audi')

# #p137
# alien_color = 'red'

# if alien_color == 'green':
#   print('player get 5 point')
# else:
#   print('player get 10 point')

# # if alien_color == 'green':
# #   print('player get 5 point')
# # elif alien_color == 'yellow':
# #   print('player get 10 point')
# # elif alien_color == 'red' :
# #   print('player get 15 point')
  
#   age = 32
#   if age < 2 :
#     print('baby')
#   elif 2<= age < 4:
#     print('todler')
#   elif 4<= age < 13:
#     print('kid')
#   elif 13<= age < 20:
#     print('teenager')
#   elif 20<= age < 65:
#     print('adult')
#   elif 65<= age:
#     print('elder')

n = int(input())
for i in range(1, n+1):
  print(" "*(n-i) + "*"*i)
# 별 왼쪽 정렬

n = int(input())
for i in range(1, n+1):
  print(" "*(n-1) + "*"*i)
#별 오른쪽 정렬
