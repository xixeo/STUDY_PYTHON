
current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

prompt = "\n Tell me something"
prompt += "\nEnter 'quit' to end the program"


# flag 추가
active = True
while active:
  message = input(prompt)

  if message == 'quit':
    active = False
  else:
    print(message)