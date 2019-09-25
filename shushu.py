def ditui2(input_list, n):
    result = 0
    while (n > 4):
        result = input_list[0] + input_list[1] + input_list[3]
        input_list.append(result)
        input_list = input_list[1:]
        n -= 1
    print(result % (10 ** 9 + 7))


if __name__ == '__main__':
    input_list = list(map(int, input().strip().split(" ")))
    n = input_list[-1]
    input_list = input_list[:-1]
    ditui2(input_list, n)
