#给你两个整数数组 nums1 和 nums2 ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，
# 应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。
from collections import defaultdict


#
# 示例 1：
#
# 输入：nums1 = [1,2,2,1], nums2 = [2,2]
# 输出：[2,2]
# 示例 2:
#
# 输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出：[4,9]
def func(nums1: List[int], nums2: List[int])->List[int]:
    # nums1.sort()
    # nums2.sort()
    # n1 = 0
    # n2 = 0
    # l = []
    # while n1 < len(nums1) and n2 < len(nums2):
    #     if nums1[n1] < nums2[n2]:
    #         n1 += 1
    #     elif nums1[n1] > nums2[n2]:
    #         n2 += 1
    #     else:
    #         l.append(nums1[n1])
    #         n1+=1
    #         n2+=1
    # return l
    l = []
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    dict = defaultdict(int)

    for num in nums1:
        dict[num] += 1
    for num in nums2:
        if num in dict and dict[num] > 0:
            dict[num] -= 1
            l.append(num)
    return l


print(func([1,2,2,1],[2]))
