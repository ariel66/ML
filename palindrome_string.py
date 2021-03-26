'''
3. A palindrome is a string with symmetric characters, given a string, 
use a function to determine if the string is a palindrome
Example:
"acbbca" -> True
"1agyga1" -> True
"tdfhflt" -> False
'''

def isPalindrome(x):
        if x < 0:
            return False
        s = str(x)
        i = 0
        j = len(s)-1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                return True
            i += 1
            j -=1



b = 0
a = isPalindrome(b)























# def f(m):
#     i = 0
#     j = len(m)-1
#     while j > i + 2:
#         if m[i] != m[j]:
#             return False
#         j -= 1
#         i += 1
#     return True

# str1 = "abc"
# a = f(str1)
# print(a)


# #注意点在于距离