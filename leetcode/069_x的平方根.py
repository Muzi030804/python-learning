"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
"""
def func( x: int) -> int:
    left = 0
    right = x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif  x < mid * mid:
            right = mid - 1

        elif x >= (mid + 1) * (mid + 1):
            left = mid + 1
print(func(1))
print(func(0))
print(func(2))
print(func(8))