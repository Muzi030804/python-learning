"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]]
（若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案
"""
def func(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []
    for i in range(len(nums)-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            if j > i +1 and nums[j] == nums[j-1]:
                continue

            left = j+1
            right = len(nums) - 1
            other = nums[i] + nums[j]
            while left < right:

                if nums[left] + nums[right] > target - other:
                    right -= 1
                elif nums[left] + nums[right] < target - other:
                    left += 1
                else:
                    res.append([nums[i],nums[j],nums[left],nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
    return res
print(func(nums = [1,0,-1,0,-2,2], target = 0))
print(func(nums = [2,2,2,2,2], target = 8))