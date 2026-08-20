# from collections import defaultdict
# def func(s: str) -> int:
#     dic = defaultdict(int)
#     for c in s:
#         dic[c] += 1
#     for i in range(len(s)):
#         if dic[s[i]] == 1:
#             return i
#     return -1
#
# print(func("aabbc"))

s = "abd"
for i,c in enumerate(s):
    print(i,c)