#给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
from typing import List
def func( nums: List[int]) -> List[int]:
    neg = len(nums) - 1
    for i in range(len(nums)):
        if nums[i] >= 0:
            neg = i - 1
            break
    left, right = neg , neg + 1
    new_nums = []
    while left >= -1 and right <= len(nums):
        if left == -1 and right == len(nums):
            break
        if left < 0:
            new_nums.append(nums[right]**2)
            right += 1
        elif right > len(nums) - 1:
            new_nums.append(nums[left]**2)
            left -= 1
        elif nums[left]**2 <= nums[right]**2:
            new_nums.append(nums[left]**2)
            left -= 1
        else:
            new_nums.append(nums[right]**2)
            right += 1
    return new_nums

print(func([-5,-3,-2,-1]))
print(func(nums = [-7,-3,2,3,11]))

