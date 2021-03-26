'''
15. Given a lowercase string,
find the index of first unique character in the string
Example:
"programming in python is popular" -> 16      
#'y' is the first unique character, its index is 16
 '''
# #set
# def f(n):
#     s = set()
#     for i in n:
#         s.add(i)


def f(str1):
    d1 = {}
    for i in str1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1  
    print(d1)
    for i in range(len(str1)):
        if d1[str1[i]] == 1:
            return i
    
nums = "programming in python is popular"
a = f(nums)
print(a)