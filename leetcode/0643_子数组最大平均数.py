#给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

#请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

#任何误差小于 10-5 的答案都将被视为正确答案

def func( nums: List[int], k: int) -> float:

    current_sum = nums[0]
    max_sum = current_sum
    for i in range(1,len(nums)):
        if i < k :
            current_sum += nums[i]
            max_sum = current_sum
        else:
            current_sum = current_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum, current_sum)
    max_avg = max_sum / k
    return max_avg
# print(func([1,12,-5,-6,50,3,],k=4))
# print(func([-1,-2],1))
print(func([4,0,4,3,3],5))