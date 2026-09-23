"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
"""
from typing import List
def func(nums: List[int], target: int) -> List[int]:
    left = 0
    right = len(nums)-1
    min_target = -1
    max_target = -1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            left = mid + 1
            max_target = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            right = mid - 1
            min_target = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return [min_target, max_target]


print(func([5,7,7,8,8,10],8))
print(func([5,7,7,8,8,10],6))
print(func([],6))
print(func([1],1))
print(func([2,2],2))
