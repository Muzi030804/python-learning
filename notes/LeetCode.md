# Note

## 未见过的方法:

max_s = -inf	表示初始化max_s为负无穷,遇到有负数的题目可以这样初始化

min_s = inf	表示初始化min_s为正无穷,

## 哈希表

哈希表,可以用字典表示,`if num in dict` 的平均时间复杂度是 `O(1)`。

字典底层使用哈希表。它不会从头遍历所有键，而是：

1. 计算 `num` 的哈希值。
2. 根据哈希值直接定位可能存放的位置。
3. 检查该位置是否存在这个键。

因此平均只需要常数时间。

与字典不同，列表不能通过哈希值直接定位元素。if num in 列表  时时间复杂度为O(n)

**hash.get(x, 0) ：**使用哈希表（字典）`hash` 可以统计元素 x 的出现次数。如果没有出现过，就返回 `0`。这里的hash是一个自己定义的字典

**defaultdict(int)**:设置默认字典.    使用 `defaultdict` 前需要：

```python
from collections import defaultdict
```

`defaultdict(int)` 和普通字典有一点区别。普通字典：

```python
dic = {}
dic["a"] += 1
```

会报错，因为 `"a"` 还不存在。

而：

```python
dic = defaultdict(int)
```

访问不存在的键时，会自动给它默认值：

```
0
```

所以可以直接：

```python
dic["a"] += 1
```

等价于：

```python
dic["a"] = 0 + 1
```

## 集合

集合判断一个元素是否存在：

```
nums[i] in s
```

平均时间复杂度是：

```
O(1)
```

# 题目

## 1.两数之和

​	数组	哈希表

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** *`target`* 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

**示例 1：**

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

**示例 2：**

```
输入：nums = [3,2,4], target = 6
输出：[1,2]
```

**示例 3：**

```
输入：nums = [3,3], target = 6
输出：[0,1]
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums and nums.index(target - nums[i]) != i :
                index_other = nums.index(target - nums[i])
                return [index_other,i]
```





## 217.存在重复元素    

​	数组    	哈希表	排序

给你一个整数数组 `nums` 。如果任一值在数组中出现 **至少两次** ，返回 `true` ；如果数组中每个元素互不相同，返回 `false` 。

 

**示例 1：**

**输入：**nums = [1,2,3,1]

**输出：**true

**解释：**

元素 1 在下标 0 和 3 出现。

**示例 2：**

**输入：**nums = [1,2,3,4]

**输出：**false

**解释：**

所有元素都不同。

**示例 3：**

**输入：**nums = [1,1,1,3,3,4,3,2,4,2]

**输出：**true

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num in hash:
                return True

            hash[num] = 1

        return False
```

利用集合的一行写法:

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
```

原理是因为题目没有具体要求出现几次,只要数组和集合长度不同就说明有重复

## 242.有效的字母异位词

​	哈希表	字符串	排序

给定两个字符串 `s` 和 `t` ，编写一个函数来判断 `t` 是否是 `s` 的 字母异位词。

字母异位词是通过重新排列不同单词或短语的字母而形成的单词或短语，并使用所有原字母一次 

**示例 1:**

```
输入: s = "anagram", t = "nagaram"
输出: true
```

**示例 2:**

```
输入: s = "rat", t = "car"
输出: false
```

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        for c in t:
            dic[c] -= 1
        for val in dic.values():
            if val != 0:
                return False
        return True
```

用默认字典记录字符串中每一个字符出现的次数,然后减去第二个字符串中字符出现的次数,如果 `t` 是 `s` 的 字母异位词,那么字典中的每一个键对应的值都应该是0

## 121.买卖股票的最佳时机

给定一个数组 `prices` ，它的第 `i` 个元素 `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

**示例 1：**

```
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
```

**示例 2：**

```
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
```

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price - min_price)
```

## 0219_存在重复元素 2

 	数组	哈希表	滑动窗口

给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引** `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

 

**示例 1：**

```
输入：nums = [1,2,3,1], k = 3
输出：true
```

**示例 2：**

```
输入：nums = [1,0,1,1], k = 1
输出：true
```

**示例 3：**

```
输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        s = set()
        for i in range(n):
            if i > k:
                s.remove(nums[i - k - 1])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
```

整理题意：是否存在长度不超过的 k+1 窗口，窗口内有相同元素。

可以从前往后遍历 nums，同时使用 Set 记录遍历当前滑窗内出现过的元素。核心思想就是`s` 中始终只保存当前元素前面最多 `k` 个元素。

假设当前遍历的元素为 nums[i]：

下标小于等于 k（起始滑窗长度还不足 k+1）：直接往滑窗加数，即将当前元素加入 Set 中；
下标大于 k：将上一滑窗的左端点元素 nums[i−k−1] 移除，判断当前滑窗的右端点元素 nums[i] 是否存在 Set 中，若存在，返回 True，否则将当前元素 nums[i] 加入 Set 中。

## 0643_子数组最大平均数 1

给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为 `k`** 的连续子数组，并输出该最大平均数。

任何误差小于 `10-5` 的答案都将被视为正确答案。

 

**示例 1：**

```
输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
```

**示例 2：**

```
输入：nums = [5], k = 1
输出：5.00000
```

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = 0

        # 先计算第一个完整窗口
        for i in range(k):
            current_sum += nums[i]

        max_sum = current_sum

        # 开始滑动窗口
        for i in range(k, len(nums)):
            current_sum += nums[i]
            current_sum -= nums[i - k]

            max_sum = max(max_sum, current_sum)

        return max_sum / k
```

