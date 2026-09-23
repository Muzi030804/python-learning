"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
"""
from collections import defaultdict


class Solution:
    def bitSquareSum(self, n: int) -> int:
        sum_n = 0
        while n > 0:
            b = n % 10
            n = n // 10
            sum_n += b**2
        return sum_n

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while slow != 1:
            slow = self.bitSquareSum(slow)
            fast = self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False
        return True



        # result = set()
        #
        # def get_next(n):
        #     s = str(n)
        #     sum_s = 0
        #     for num in s:
        #         sum_s += (ord(num) - ord('0')) ** 2
        #     if sum_s in result:
        #         return False
        #     else:
        #         result.add(sum_s)
        #     print(result)
        #
        #     print(sum_s)
        #     if sum_s == 1:
        #         return True
        #     if get_next(sum_s):
        #         return True
        #     else:
        #         return False
        # return get_next(n)

f = Solution()
print(f.isHappy(19))
print(f.isHappy(2))
# n = 314
# s = str(n)
# li = list(s)
# for num in li:
#     print(num)
#     print(ord(num)-ord('0'))
#     print(type(num))