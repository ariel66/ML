'''
1. Given 2 lists, find the intersection of them, return it as a new list
Example:
input:
[2,4,6,8,9]
[1,3,4,5,7,8,10]
return:
[4,8]
#set 找独一无二的元素 都可以用set做
'''
def f(n,m):
    i = 0
    res = []
    while i < len(n):
        j = 0
        while j < len(m):
            if n[i] == m[j]:
                res.append(n[i])
            j += 1
        i += 1
    return res

nums1 = [2,4,6,8,9] 
nums2 = [1,3,4,5,7,8,10]
a = f(nums1,nums2)
print(a)
