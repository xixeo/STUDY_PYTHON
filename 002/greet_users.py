def greet_users(names):
  """리스트의 사용자에게 단순한 인사말을 출력"""
  for name in names:
    msg = f"hello, {name.title()}"
    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)