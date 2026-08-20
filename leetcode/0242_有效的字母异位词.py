
# s = "car"
# t = "rar"
# print(s)
# print(sorted(s))
#
# s_list = list(s)
# t_list = list(t)
# print(s_list)
# print(t_list)
# s_list = sorted(s_list)
# t_list = sorted(t_list)
#
# print(s_list)
# print(t_list)


def is_anagram(s: str, t: str) -> bool:
    # return sorted(s) == sorted(t)
    count1 = []
    count2 = []
    for i in range(26) :
        count1.append(0)
        count2.append(0)
    for c in s:
        count1[ord(c) - ord('a')] += 1
    for c in t:
        count2[ord(c) - ord('a')] += 1
    for i in range(26) :
        if count1[i] != count2[i] :
            return False
    return True



print(is_anagram(s="rar",t="rar"))


