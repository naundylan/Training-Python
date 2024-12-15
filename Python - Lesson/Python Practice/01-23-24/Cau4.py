import os
# lấy đường dẫn hiện tại chỉ đến file này
current_dir = os.path.dirname(__file__)
os.chdir(current_dir)
with open("data.txt", "r") as file_in, open("preprocessed_data.txt", "w") as file_out:
    data = file_in.read()
    data = data.lower().split(".")
    for item in data:
        new = "".join([char for char in item if char.isalnum() or char.isspace()])
    print(new)
    for item in data:
        file_out.write(item + "\n")
            