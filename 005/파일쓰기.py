# 파일 생성 및 쓰기
from pathlib import Path
import os
print(f"현재경로 = {os.getcwd()}")

with open('example.txt', 'w') as file: #file변수는 open 파일 객체
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")

print("File created and written successfully.")
path = Path('example.txt')
path.write_text("path 객체를 사용한 쓰기")

# 파일에 내용 추가하기
with open('example.txt', 'a') as file:
    file.write("Adding a new line.\n")
    file.write("Appending another line.\n")

print("Content appended to the file successfully.")

# 새로운 파일 생성하기
try:
    with open('new_file.txt', 'x') as file:
        file.write("This is a newly created file.\n")
    print("New file created and written successfully.")
except FileExistsError:
    print("File already exists.")