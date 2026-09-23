"""
给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符，再重新计数。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""
def func( s: str, k: int) -> str:
    slow, fast = 0, 0
    ch = list(s)
    while fast < len(s):
        slow = fast

        cur = slow
        for i in range(k):
            if slow < len(ch):
                slow += 1
                fast += 1
                fast += 1
        while cur < slow:
            temp = ch[cur]
            ch[cur] = ch[slow-1]
            ch[slow-1] = temp
            slow -= 1
            cur += 1
    s = "".join(ch)
    return s
print(func(s = "abcdefghijk", k = 3))
print(func(s = "abcd", k = 2))