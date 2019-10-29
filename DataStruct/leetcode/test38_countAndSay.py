# coding:utf-8
class Solution:
    def countAndSay(self, n: int) -> str:
        res_num = "1"
        for _ in range(1, n):
            curr_num = res_num[0]
            curr_count = 1
            curr_result = ""
            for i in range(1, len(res_num)):
                if res_num[i] == curr_num:
                    curr_count += 1
                else:
                    curr_result += str(curr_count) + curr_num
                    curr_num = res_num[i]
                    curr_count = 1

            curr_result += str(curr_count) + curr_num
            res_num = curr_result
        return res_num

    # 递归调用
    def countAndSay01(self, n: int) -> str:
        if n == 1:
            return "1"
        res_num = self.countAndSay(n - 1)
        curr_num = res_num[0]
        curr_count = 1
        curr_result = ""
        for i in range(1, len(res_num)):
            if res_num[i] == curr_num:
                curr_count += 1
            else:
                curr_result += str(curr_count) + curr_num
                curr_num = res_num[i]
                curr_count = 1

        curr_result += str(curr_count) + curr_num
        res_num = curr_result

        return res_num


if __name__ == '__main__':
    n = 4
    s = Solution()
    # print(s.countAndSay(n))
    print(s.countAndSay01(n))
