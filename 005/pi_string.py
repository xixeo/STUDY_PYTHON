from pathlib import Path
import os

new_path = '005'
os.chdir(new_path)
path = Path('pi_million_digits.txt')

contents = path.read_text()
contents = contents.rstrip().lstrip() 
lines = contents.splitlines()
pi_string=''

for line in lines:
  print(f'{pi_string[:52]}')
  print(len(pi_string))