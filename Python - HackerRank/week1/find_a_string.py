def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string) - len(sub_string) + 1):
        status = True
        for j in range(len(sub_string)):
            if string[i + j] != sub_string[j]:
                status = False
                break
        if status:
            cnt += 1
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)