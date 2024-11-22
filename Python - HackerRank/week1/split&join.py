def split_and_join(input):
    input = input.split(" ")
    return "-".join(input)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)