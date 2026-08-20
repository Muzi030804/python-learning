from collections import defaultdict
#遍历时只保留与当前下标距离不超过 k 的元素，已经超出距离范围的元素及时移除；
# 当前元素若已在保留范围内，就满足条件。
nums = [1,2,3,1]
k = 3
def solution(nums, k):
    # dict = defaultdict(list)
    # for i in range (len(nums)):
    #     if dict[nums[i]] == []:
    #         dict[nums[i]].append(i)
    #     else:
    #         dict[nums[i]].append(i)
    #         if i - k <= dict[nums[i]][-2] :
    #             return True
    # return False
    dic = defaultdict(int)
    for i in range (len(nums)):
        if nums[i] in dic:
            if i - dic[nums[i]] <= k:
                return True
            else:
                dic[nums[i]] = i
        else:
            dic[nums[i]] = i
    return False
print(solution([1,0,1,1], 1))