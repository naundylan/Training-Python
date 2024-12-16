def xacsuat(s):
    listStr = s.split()
    length = len(listStr)
    list = {}
    for tmp in listStr:
        count = listStr.count(tmp)
        list[tmp] = count
    for tmp in list:
        print(f"p({tmp}): {'%.1f' % ((count / length) * 100)}%", end=" ")
if __name__ == "__main__": 
    xacsuat(input())