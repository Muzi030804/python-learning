"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
"""
from collections import defaultdict


def func(nums: List[int], k: int) -> int:
    current_sum = 0
    prev_sums = defaultdict(int)
    count = 0
    for num in nums:
        current_sum += num
        if current_sum - k in prev_sums:
            count += prev_sums[current_sum - k]
        if current_sum == k:
            count += 1
        prev_sums[current_sum] += 1
    return count

print(func(nums=[1,2,3,4,5],k=3))
print(func(nums=[1,1,1],k=2))
print(func(nums=[1], k=0))