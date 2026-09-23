#给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
from collections import defaultdict

#优化思路：不必把离开范围的字符逐个从字典中删除。考虑只保存每个字符最近出现的位置；遇到重复字符时，只更新左边界，
# 并保证左边界永远不向后退。当前长度可以直接根据左右边界计算。
def func(s: str) -> int:
    max_length = 0
    right = 0
    left = 0
    dict = defaultdict(int)
    while right < len(s):
        if s[right] in dict:
            if left <= dict[s[right]]:
                left = dict[s[right]] + 1
        dict[s[right]] = right
        right += 1
        current_length = right - left
        max_length = max(max_length, current_length)
    return max_length
print(func("abcabcbb"))
print(func("bbba"))
print(func("1R1T7"))
print(func("bbbb"))
print(func("pwwkew"))
print(func("pw"))
print(func("ccbbcc"))


