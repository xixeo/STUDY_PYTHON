def ten_times(func):
  for i in range(5):
    func()

def print_hello():
  print("hello")

ten_times(print_hello) #함수를 parameter로 전달

###### part 2
def add(x, y):
  return x+y

def apply_operation(operation, x, y):
  return operation(x, y)

result = apply_operation(add, 3, 4)

###### part 3
def power(item):
  return item**2

def under_three(item):
  return item < 3

lst = [1, 2, 3, 4, 5]
map_list = map(power, lst)
print(list(map_list))

filter_list = filter(under_three, lst)
print(list(filter_list))

###### part 4 람다식
m_list = map(lambda x: x**2, lst) #  map_list = map(power, lst)와 같음
