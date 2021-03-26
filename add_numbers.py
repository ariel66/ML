'''
10. Given a number, add all its digits and return the sum
Example:
30967 -> 3+0+9+6+7 -> 25
'''
#重做 str不要这么用
def f(digits):
    res = 0
    lendigits = len(str(digits))
    while lendigits > 0:
        remainder = digits % 10
        digits = digits // 10
        res += remainder
        lendigits -= 1
    return res

nums = 30967
a = f(nums)
print(a)


