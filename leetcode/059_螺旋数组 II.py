"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix
"""

from typing import List
def func( n: int) -> List[List[int]]:
    count = 1
    answer = []
    start_x = 0
    start_y = 0
    loop = n // 2
    mid = n // 2
    side_length = 1
    for i in range(n):
        answer.append([])
        for j in range(n):
            answer[i].append(0)
    while loop > 0:
        i = start_x
        j = start_y
        loop -= 1


        while j < n - side_length:
            answer[i][j] = count
            count += 1
            j += 1


        while i < n - side_length:
            answer[i][j] = count
            count += 1
            i += 1

        while j > start_y:
            answer[i][j] = count
            count += 1
            j -= 1

        while i > start_x:
            answer[i][j] = count
            count += 1
            i -= 1

        start_x += 1
        start_y += 1
        side_length += 1
    if n % 2 == 1:
        answer[mid][mid] = n ** 2

    return answer
# print(func(1))
# print(func(3))
print(func(4))

