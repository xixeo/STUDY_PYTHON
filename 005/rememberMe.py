from pathlib import Path
import json
import os

new_path = "005"
os.chdir(new_path)
path = Path('guest.txt')

username = input("What's ur name?")

path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"welcome, {username}")