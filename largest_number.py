'''
13. Given a list of numbers, find the largest number that only appears once
Example:
[12,3,5,8,5,9,12,8] -> 9
#set做
'''
#用set

def f(n):
    s = set()
    for i in n:
        s.add(i)
        





















# def f(n):
#     d1 = {}
#     res = []
#     for i in n:
#         if i not in d1:
#             d1[i] = 1
#         else:
#             d1[i] += 1
#     for i in d1:
#         if d1[i] == 1:
#             res.append(i)
#     return max(res)
           

# nums = [12,3,5,8,5,9,12,8]
# a = f(nums)
# print(a)