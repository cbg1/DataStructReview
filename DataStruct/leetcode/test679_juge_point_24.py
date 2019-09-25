# coding:utf-8
from operator import truediv, mul, add, sub


class Solution:
    def jubge_point_24(self, A):
        if not A:
            return False
        if len(A) == 1:
            return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    #
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    print(B)
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.jubge_point_24(B): return True
                            B.pop()
        return False


if __name__ == '__main__':
    A = list(map(int, input().strip().split(" ")))
    s = Solution()
    result = s.jubge_point_24(A)
    print(result)
