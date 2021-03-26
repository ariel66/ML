'''
7. Given a list of numbers, move all zeros to the end while perserve the order of other numbers, return the new list
Example:
[0,3,0,1,12] -> [3,1,12,0,0]
'''
#暴力解法 可以优化
def f(n):
    i = 0
    res = []
    zero = []
    while i < len(n):
        if n[i] != 0:
            res.append(n[i])
        if n[i] == 0:
            zero.append(n[i])
        i += 1
    
    return res+zero

nums = [0,3,0,1,12]
a = f(nums)
print(a)