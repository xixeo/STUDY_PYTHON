from pathlib import Path
import os

new_path = "005"
os.chdir(new_path)
path = Path('guest.txt')

names = []

while(True):
  name = input("이름이 무엇인가요? (q입력시 종료)")
  names.append(name)
  if name == 'q':
    break;
  elif name != '':
    with open('guest.txt', 'a', encoding="UTF-8") as file:
      file.write(name +"\n")