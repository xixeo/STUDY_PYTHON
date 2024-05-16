data = [1, 2, 3]
# print(data, type(data))

# data = list() #list라는 객체를 생성하기. java에서는 data = new List()
# print(data, type(data))

# print(data[0])
# print(data[1])
# print(data[2])
# print(len(data))

data.append(6) # 배열에 값 추가
data.append(7)
data.append(8)
# print(len(data))

data[3] = 4
data[4] = 5
# print(data, len(data), sum(data), min(data), max(data))

data = list(range(10, 0, -1)) #거꾸로 출력하기
# print(data, type(data), sorted(data))

# 10
# 10 9 8 7 6 5 4 3 2 1
# 합계를 구하시오, 정렬하시오, 최대값을 찾으시오, 최소값을 찾으시오

# data = input()
# data = data.split() # list 쪼개기
# data = list(map(int, data)) # 숫자로 변환
# # print(data, type(data), type(data[0]))
# print(sum(data)) # 합계 출력

# data = list(map(int, input().split())) #한 줄로 축약
# print(sum(data)) # 합계 출력

# data = [1, 2, 3]
# del data[1] # 배열에 값 삭제
# print(data)

# data = [1, 2, 3.14, 'hello', len, range(5)]
# print(data, type(data))
# for d in data:
#   print(d, type(d))

data = [1,2,3,4,5]
print(data[len(data)-1])
print(data[::-1]) # print(data.reverse())  와 같음

data = data[::-1]
print('data', data)

data.append(1) # 배열의 마지막에 값 추가
print(data)
data.pop() # 배열의 마지막 값 빼기
print(data)
data.insert(0,333) # 배열의 특정 위치 값 추가
print(data)
del data[1] # 배열의 특정 위치 값 삭제
print(data)
data.remove(3) # 배열의 특정 값 삭제
print(data)

print(sorted(data))
print(data)

sorted_data = sorted(data)
print(sorted_data) #값을 새로운 변수에 할당해서 쓰는게 안전