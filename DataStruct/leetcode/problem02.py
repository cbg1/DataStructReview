def big_happy(array):
    left = 0
    right = len(array) - 1
    smallMI = 0
    bigMI = 0
    while left < right:
        if array[left] > array[right]:
            smallMI += array[left]
            left += 1
        else:
            smallMI += array[right]
            right -= 1
        if array[left] > array[right]:
            bigMI += array[left]
            left += 1
        else:
            bigMI += array[right]
            right -= 1
    if smallMI >= bigMI:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    array_str = input()
    if array_str == "" or len(array_str.strip().split(" ")) <= 2:
        print("YES")
    else:
        array = []
        for item in array_str.split(" "):
            array.append(int(item))
        result = big_happy(array)
        print(result)
