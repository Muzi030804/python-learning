#给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
from collections import defaultdict
def func(s: str, p: str) -> List[int]:
    l = []
    p_dict = defaultdict(int)
    left = 0
    right = 0
    for c in p:
        p_dict[c] += 1
    non_zero_count = len(p_dict)
    while right < len(s):
        if right - left < len(p):
            if s[right] in p_dict:
                p_dict[s[right]] -= 1
                if p_dict[s[right]] == 0:
                    non_zero_count -= 1
            right += 1
        else:
            if s[left] in p_dict:
                if p_dict[s[left]] == 0:
                    non_zero_count += 1
                p_dict[s[left]] += 1
            left += 1
        if non_zero_count == 0:
            l.append(left)
    return l
print(func("cbaebabacd","abc"))
print(func("abab","ab"))