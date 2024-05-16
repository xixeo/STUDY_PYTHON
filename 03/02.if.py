score = 83
if (90 <= score) and (score <= 100):
  print('A')
elif (80 <= score) and (score < 90):
  print('B')
else:
  print('F')

msg = 'hello'
a = 5
if a == 5:
  print('right')

if msg == 'hello':
  print('right!')

data = [1, 2, 3]
if data == [1, 2, 3]:
  print('right!')

if data:
  print('right !!!!')

if 3 in data:
  print('Here !')

data = [] #출력 안됨
if data:
  print('right !!!!!')

a = 3
if a < 5 or a < 10:
  print('a') 

data = [1,2,3]
for d in data:
  if d < 2:
    print(d)
  else:
    print('wrong !')

# user_ids_lower = [id.lower() for id in user_ids]
# for id in new_ids:
#   if id.lower() in user_ids_lower:
#     print(f'{id} is ')
