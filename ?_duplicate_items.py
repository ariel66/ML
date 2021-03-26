'''
2. Given a list of numbers, determine if it contains duplicate
Example:
[4,5,7,3,2,0,-4] -> False
[4,5,7,3,3,0,-2] -> True
#set/ dict
'''

def f(n):
    s = set()
    for i in n:
        s.add(i)
    if len(s)<len(n):
        return True
    else:
        return False

nums = [4,5,7,3,3,0,-2]
a = f(nums)
print(a)

























# def f(n):
#     i = 0
#     while i < len(n):
#         j = i+1
#         while j < len(n):
#             if n[i] == n[j]:
#                 return True
#             j+=1
#         i += 1
#     return False

# nums = [4,5,7,3,3,0,-2]
# a = f(nums)
# print(a)


