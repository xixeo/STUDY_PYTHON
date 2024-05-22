from pathlib import Path

import os
#print(os.getcwd) #현재 경로를 알려줌

# path = Path('005/pi_digits.txt')
# contents = path.read_text()

# lines = contents.splitlines()
# for line in lines:
#     print(line)

new_path = "005"
os.chdir(new_path)
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip().lstrip() 
lines = contents.splitlines()
pi_string=''

for line in lines:
    line = line.lstrip()
    pi_string += line
    print(f'각 줄은 = {pi_string}')