#给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序
from collections import defaultdict
from typing import List
def func( nums1: List[int], nums2: List[int]) -> List[int]:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    s = set(nums1)
    res = []

    for num in nums2:
        if num in s:
            res.append(num)
            s.remove(num)

    return res

print(func([1,1,3],[1,1,6]))