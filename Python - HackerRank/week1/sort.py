def order(records):
    records.sort(key = lambda x : x[1])
    li = [element[1] for element in records]
    m = records[0][1]
    tmp = max(li)
    for item in li:
        if item != m and item < tmp:
            tmp = item
    second_lowest = [name for name, score in records if tmp == score]
    second_lowest.sort()
    return second_lowest

if __name__ == '__main__':
    record = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record.append([name, score])
    result = order(record)
    for item in result:
        print(item)