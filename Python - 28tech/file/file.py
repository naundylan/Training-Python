import os
print("Thư mục làm việc hiện tại:", os.getcwd())
# Thay đổi thư mục làm việc
os.chdir(r"D:\Practice\Training-Python\Python - 28Tech\file")
print("Thư mục làm việc hiện tại:", os.getcwd())

with open(r"input01.txt", "r", encoding="utf-8") as file:
    content = file.read()
    alpabet, num, other = "", "", ""
    for i in content:
        if i.isalpha():
            alpabet += i
        elif i.isnumeric():
            num += i
        else:
            other += i
with open(r"result01.txt", "w", encoding="utf-8") as file:
    result = file.write(alpabet + "\n" + num + "\n" + other)