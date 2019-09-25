def MoreThanHalfNum_Solution(numbers):
    len1 = len(numbers)
    if len1 == 0:
        return 0
    elif len1 >= 1:
        res = numbers[0]
        count = 1
        for i in range(1, len1):
            if count == 0:
                res = numbers[i]
                count = 1
            if res == numbers[i]:
                count += 1
            if res != numbers[i]:
                count -= 1

        counts = 0
        for num in numbers:
            if res == num:
                counts += 1
        if counts > len1 // 2:
            return res
        else:
            return 0


if __name__ == '__main__':
    try:
        while True:
            print("please input list:")
            arr = list(map(int, input().strip().split(" ")))
            print(MoreThanHalfNum_Solution(arr))
    except:
        pass


