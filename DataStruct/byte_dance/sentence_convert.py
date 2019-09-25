# coding:utf-8
'''
要求输入www.toutiao.com.cn输出cn.com.toutiao.www,空间复杂度为O(1)，时间复杂度为最小
'''
s = "www.toutiao.com.cn"
print(id(s))
s = s.split(".")
s = s[::-1]
s = ".".join(s)#使用前面得符号将list中的元素链接成字符串
print(s)
print(id(s))
