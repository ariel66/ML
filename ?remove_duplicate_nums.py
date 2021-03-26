'''
4. Given a list of numbers, remove duplicate numbers and return the new list
Example:
[1,-4,5,10,8,3,1,10,6,9,-2,-4] -> [1,-4,5,10,3,8,6,9,-2]
'''
#return new list/set

def f(n):
    s = set()
    for i in n:
        s.add(i)
    return s

nums = [1,-4,5,10,8,3,1,10,6,9,-2,-4]
a = f(nums)
print(a)
























# def f(n):
#     i = 0
#     while i < len(n):
#         j = i+1
#         while j < len(n):
#             if n[i] == n[j]:
#                 del n[j]
#                 print(n)
#             j += 1
#         i += 1
#     return n

# nums = [1,-4,5,10,8,3,1,10,6,9,-2,-4]
# a = f(nums)
# print(a)