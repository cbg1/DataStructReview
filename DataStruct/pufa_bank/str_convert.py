# coding:utf-8
# 输入几个单词，将字母变换成另外一组单词输出？如果字母是i，则变换后的字母是26+i-1
# ord(ch) 字符转化为ASCII码
# chr(n) ASCII码转化为字符
# ch = "a"
# if ord(ch) in range(97, 123):
#     print(chr(ord(ch) - 32))
if __name__ == '__main__':
    s = input()
    s1 = [" " for _ in range(len(s))]
    for i in range(len(s)):
        if s[i] >= "a" and s[i] <= "z":
            s1[i] = chr(ord("z") - (ord(s[i]) - ord("a")))
        elif s[i] >= "A" and s[i] <= "Z":
            s1[i] = chr(ord("Z") - (ord(s[i]) - ord("A")))
    print("".join(s1))
