#给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。
# 如果是，返回 true ；否则，返回 false 。
from collections import defaultdict
#换句话说，s1 的排列之一是 s2 的 子串 。

def func(s1: str, s2: str) -> bool:
    s1_dict = defaultdict(int)
    left = 0
    right = 0
    for c in s1:
        s1_dict[c] += 1
    non_zero_count = len(s1_dict)
    while right < len(s2):
        if right - left < len(s1):
            if s2[right] in s1_dict:
                s1_dict[s2[right]] -=1
                if s1_dict[s2[right]] == 0:
                    non_zero_count-=1
            right += 1
        else:
            if s2[left] in s1_dict:
                if s1_dict[s2[left]] == 0:
                    non_zero_count+=1
                s1_dict[s2[left]] += 1
            left += 1
        if non_zero_count==0:
            return True
    return False

print(func("adc","dcda"))

print(func("ab","abc"))
print(func("ab","eidbobaoo"))
print(func("hello","ooolleoooleh"))