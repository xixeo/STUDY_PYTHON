def build_person(first_name, last_name):
  """사람에 대한 정보를 딕셔너리로 반환합니다"""
  person = {'first' : first_name, 'last' : last_name}
  return person

musician = build_person('jimi', 'hendrix')
print(musician)