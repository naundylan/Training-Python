def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string) - len(sub_string) + 1):
        if sub_string[0] == string[i]:
            for j in range(len(sub_string)):
                if string[i + j] != sub_string[j]:
                    break
            cnt += 1
    return cnt