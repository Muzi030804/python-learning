"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""

def func(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []

    for i in range(len(nums) - 2):

        # nums[i] 去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 排序后，如果当前最小值都大于0，后面不可能再凑成0
        if nums[i] > 0:
            break

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total > 0:
                right -= 1

            elif total < 0:
                left += 1

            else:
                res.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # left 去重
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # right 去重
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res
print(func([-1,0,1,2,-1,-4]))
print(func([1,1,-2]))
print(func([1,-1,-1,0]))
print(func([0,0,0,0]))
print(func([-2,0,0,2,2]))
print(func([1,1,-2,-2,-2]))