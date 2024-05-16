alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0)

# new_point = alien_0['points'] #키 값을 찾기 > 값을 리턴
# del alien_0['points']
alien_0['x_position'] = 0 #dictionary에 키를 추가하기
alien_0['y_position'] = 25

alien_0['color'] = 'yellow'
# print(alien_0)

# point_value = alien_0['point'] #point가 없어서 에러남
point_value = alien_0.get('point', 'no point') # point값이 없으면 no point 출력됨
print(point_value)

user_0 = {
  'username' : 'efermi',
  'first' : 'enrico',
  'last' : 'fermi'
}

for key, value in user_0.items():
  print(f'\nKey: {key}')
  print(f'Value: {value}')

favorite_languages = {
  'jen' : 'python',
  'sarah' : 'c',
  'edward' : 'rust',
  'phil' : 'python'
}

for v in favorite_languages.values(): # value값 전부 출력
  print(v.title())

for v in favorite_languages.keys(): # key 값 전부 출력1
  print(v.title())

for language in set(favorite_languages.values()):
  print(language.title())


alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]
for a in aliens:
  print(a)

use_languages = {
  'jen' : ['python', 'rust'],
  'sarah' : ['c'],
  'edward' : ['rust', 'go'],
  'phil' : ['python', 'haskell'],
}

for name, languages in use_languages.items():
  print(f"\n{name.title()}'s favorite langues are :")
  for language in languages:
    print(f"\t{language.title()}")
