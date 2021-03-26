'''
12. Given a list of strings, find all the characters that appear exactly 3 times
Example:
["icecream","garlic","desk","downstairs"] -> ["e","c","i","r","a","s"]
'''
#两个循环
def f(n):
    d1 = {}
    res = []
    m = ''.join(n)
    for i in m:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1
    for i in d1:
        if d1[i] == 3:
            res.append(i)
    return res

str1 = ["icecream","garlic","desk","downstairs"]
a = f(str1)
print(a)

