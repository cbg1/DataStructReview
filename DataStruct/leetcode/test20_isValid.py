class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["#"]
        key_dict = {"(": ")", "{": "}", "[": "]", "#": "#"}
        for c in s:
            if c in list(key_dict.keys()):
                stack.append(c)
            elif c != key_dict[stack.pop()]:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    # kuohao = "()[]{}"
    kuohao = "]"
    s = Solution()
    print(s.isValid(kuohao))
