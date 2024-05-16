###########Practice

# p58 변수 출력
message = 'Hello !'
print(message)

message = 'Hi !'
print(message)

# p65 개별 메시지, 대소문자
name = 'eric'

print(f'Hi {name}, Let\'s study Python !')
print(name.upper()) #대문자로 출력
print(name.capitalize()) #첫 글자만 대문자

name = 'ERIC'
print(name.lower()) #소문자로 출력

great_man = 'Ben Stein'
said = 'The first step to getting the things you want out of life is this: Decide what you want.'
print(f'{great_man}, said "{said}"') # f문자열

famouse_person = great_man
message = said
print(f'{famouse_person}, said "{message}"') # f문자열

fileNm = 'python_notes.txt'
print(fileNm.removesuffix('.txt')) # 특정 문자열 삭제

# p70 상수
print(5+3)
print(10-2)
print(4*2)
print(16/2)

# p78 list
names = ['jenny', 'jisu', 'lisa', 'rose']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

cars = ['tesla', 'volvo', 'benz']
for car in cars:
  print(f'I love car makers are {car}')

# p85 list
guests = ['mom', 'dad', 'sis', 'bro']
# for guest in guests:
  # print(f'{guest} ! come to for dinner')
guests.remove('bro')
guests.append('DDU')
# for guest in guests:
#   print(f'{guest} ! come to for dinner')

guests.insert(0, 'Suhyun')
guests.insert(2, 'Tai')
guests.append('Kani')
# for guest in guests:
#   print(f'{guest} ! come to for dinner')

guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()  #while 2 < len(names)  :
              #         names.pop()

# for guest in guests:
#   print(f'{guest} ! come to for dinner')

del guests[1]
del guests[0]
print(guests)