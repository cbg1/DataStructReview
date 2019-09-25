# coding:utf-8
def is_str(s1, s, i, t):
    num = 0
    if s[i].isalpha():
        s1 = s1[:t] + s[i] + s1[t + 1:]
        t += 1
    elif s[i].isdigit():
        while s[i].isdigit():
            num *= 10
            num += ord(s[i]) - 48
            i += 1

    if s[i] == "[":
        i += 1
        n = 0
        while num:
            num -= 1
            n = i
            while n < lenght and s[n] != "]":
                if s[n].isdigit():
                    n = is_str(s1,s, n, t)
                    if s[n] == "]":
                        break
                s1 = s1[:t] + s[n] + s1[t + 1:]
                t += 1
                n += 1

        i = n
    return i


if __name__ == '__main__':
    s = input().strip()
    lenght = len(s)
    t = 0
    s1 = ""
    i = 0
    for i in range(lenght):
        i = is_str(s1, s, i, t)
    print(s1)
    for j in range(t):
        print(s1[j], end="")
