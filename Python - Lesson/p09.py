def check(username, usernamelist):
    return username in usernamelist

def login(username, password, dictionary):
    if check(username, dictionary):
        if dic[username] == password:
            print("Ban da dang nhap thanh cong!")
    else:
        print("Ten dang nhap hoac mat khau khong dung, vui long nhap lai!")

if __name__ == "__main__":
    print("nhap so luong nguoi dung:")
    n = int(input())
    dic = {}
    for i in range(n):
        print("nhap ten nguoi dung: ", end="")
        username = input()
        while(check(username, dic)):
            print("ten dang nhap da ton tai, vui long nhap lai!")
            print("nhap ten nguoi dung: ", end="")
            username = input()
        print("nhap mat khau: ", end="")
        password = input()
        dic[username] = password
    print("da nhap thanh cong danh sach, xin hay dang nhap:", end="")
    print()
    print("----------------------",end="")
    print()
    print("Ten dang nhap: ", end="")
    user = input()
    print("Mat khau: ", end="")
    pas = input()
    login(user, pas, dic)
    
