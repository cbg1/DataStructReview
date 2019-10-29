# coding:utf-8
'''
有效括号
用栈解决
1.如果为正括号则入栈
2.如果为反括号，如果这是栈空了则false，否则与出栈的对比不对则false。
'''


class Solution:
    def isValid(self, s: str) -> bool:
        kuohao_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c in list(kuohao_dict.keys()):
                stack.append(c)
            else:
                if len(stack) > 0:
                    if c != kuohao_dict[stack.pop()]:
                        return False
                else:
                    return False
        return len(stack) == 0

    def isValid01(self, s: str) -> bool:
        kuohao_dict = {'(': ')', '{': '}', '[': ']', "#": "#"}
        stack = ["#"]
        for c in s:
            if c in list(kuohao_dict.keys()):
                stack.append(c)
            elif c != kuohao_dict[stack.pop()]:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    # kuohao = "()[]{}"
    kuohao = "]"
    s = Solution()
    print(s.isValid(kuohao))
