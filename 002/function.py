def greet_user():
  """단순한 인사말을 표시합시다"""
  print("helloooo")

greet_user()

def describe_pet(pet_name, animal_type='dog'): #animal_type을 특정하지 않을시 default로 dog가 출력
  """반려동물 정보를 표시합니다"""
  print(f"\nI have a {animal_type}")
  print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name='harry', animal_type='hamster')