# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。

def func(target: int, nums: List[int]) -> int:
    right = 0
    left = 0
    length = len(nums)
    sum_current = 0
    min_length = length
    while right <= length  and left <= length:
        if right == length and left ==0 and sum_current < target:
            return 0
        if right == length  and sum_current < target:
            return min_length
        if sum_current < target and right < length:
            sum_current += nums[right]
            right += 1
        elif sum_current >= target:
            min_length = min(min_length, right - left )
            sum_current -= nums[left]
            left += 1
    return min_length




# print(func(213, [12,28,83,4,25,26,25,2,25,25,25,12]))
print(func(15,[1,2,3,4,5]))
print(func(7, [1,1,1,1]))