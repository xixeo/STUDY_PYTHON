# data = [1, 2, 3]
# for d in data:
#   print(d, end='  ') #한 줄로 출력하는 방법
# data[1] = 5 #List는 값이 바뀐다.

# string = 'hello'
# for s in string:
#     print(s,  end='  ')
# print(string[1])
# string[1] = 'E' #string은 한 번 만들면 값을 바꿀 수 없다.

data = (1, 2, 3)
for d in data:
  print(d, end='  ') #한 줄로 출력하는 방법
# data[1] = 5 #tuple은 한 번 만들면 값을 바꿀 수 없다.


#1
data2 = [i**2 for i in data] # 3번과 같은 값이 나옴
print(data2, type(data2))

#2
data2 = [i**2 for i in data if i**2 < 5] #if문이 추가된 for문
print(data2, type(data2))

#3
data3 = [] # 1번과 같은 값이 나옴
for i in data:
  data3.append(i**2)
  print(data3)

# for (int i=0; i<10; i++) # 데이터가 몇 갠지 알고 쓰는 거, 옛날방식
  
data = []
for d in data: # 데이터가 몇 갠지 몰라도 쓸 수 있는거, 더 선호하는 방식
  print(d)

# [1, 5)
for i in range(1, 6): #1부터 5까지
  print(i, end= ' ')


#### for i in range(len(data)): #파이썬에선 이렇게 안쓴다~
####   print(data[i], end= '')

############ 파이썬의 for문
for _ in range(10): # i값을 비워놓고도 for문 돌려짐
  print('a', end=' ')
  for d in data:
    print(d)

for idx, d in enumerate(data): #index값 불러오기 idx, enumerate
  print(idx, d)

  data_2d = [[1, 2, 3], [4, 5, 6]]
  for data in data_2d:
    for d in data:
      print(d, end= ' ')
    print()

data = [1, 3.14, 'hello', max, range]
for d in data:
  print(d, type(d))

for i in range(len(data)):
  print(data[i])

for i in range(3, 31, 3):
  print(i, end= ' ')

print([i**3 for i in range(1, 11)])

# [1, 11)
data = list(range(1, 11))
# [1, 5)
print(data, data[1:5], sep='\n')
print(data, data[1:-1], sep='\n')
print(data, data[:5], data[5:], sep='\n')

def swap(a, b):
  temp = a
  a = b
  b = temp

a, b = 1, 2

print(a, b)
swap(a, b)
print(a, b)

data = [1, 2, 3]
data2 = data[:]
data2 = data.copy()
print(data2)
data2[1] = 5
print(data, data2, sep='\n')