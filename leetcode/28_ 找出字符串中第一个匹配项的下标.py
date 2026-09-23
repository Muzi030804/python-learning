"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。
如果 needle 不是 haystack 的一部分，则返回  -1 。
"""
def func( haystack: str, needle: str) -> int:

    needle_index = 0
    res = 0
    head_list = []
    for index, char in enumerate(haystack):
        if char == needle[needle_index]:
            head_list.append(index)
    if not head_list:
        return -1
    slow = head_list[0]
    while slow < len(haystack):
        if needle[needle_index] == haystack[slow]:
            slow += 1
            needle_index += 1
        else:
            needle_index = 0
            if res < len(head_list) - 1:
                res = res + 1
                slow = head_list[res]
            else:
                return -1

        if needle_index == len(needle):
            return head_list[res]
    return -1
print(func( haystack="hello", needle="ll"))
print(func(haystack = "sadbutsad", needle = "sad"))
print(func(haystack = "leetcode", needle = "leeto"))
print(func(haystack = "mississippi", needle = "issip"))
