# coding:utf-8
# 给字符串如“aaeefssgyyy”，输出“a2e2f1s2g1y3”
def continue_str_count(s):
    count = 1
    single_str = s[0]
    res = ""
    for i in range(1, len(s)):
        if s[i] == single_str:
            count += 1
        else:
            res = res + single_str + str(count)
            single_str = s[i]
            count = 1

    res += single_str + str(count)
    return res


if __name__ == '__main__':
    s = input()
    result = continue_str_count(s)
    print(result)
