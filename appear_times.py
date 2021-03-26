'''
11. Given a list of strings, find the all the strings that appear exactly 3 times
Example:
["hello","world","python","hello","python","study","hello","python"] -> ["hello","python"]
'''
def f(n):
    dict1 = {}
    res = []
    for i in n:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for i in dict1:
        if dict1[i] == 3:
            res.append(i)

    return res 

nums = ["hello","world","python","hello","python","study","hello","python"]
a = f(nums)
print(a)

        