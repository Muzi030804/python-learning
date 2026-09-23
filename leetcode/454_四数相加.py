"""
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
"""
from collections import defaultdict
from typing import List
def solution( nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
    count = 0
    dic1 = defaultdict(int)
    for i in nums1:
        for j in nums2:
            dic1[i+j] += 1
    for i in nums3:
        for j in nums4:
            count += dic1.get(i+j, 0)

    return count
print(solution(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(solution(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))

