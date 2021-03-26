'''
5. Given a string, like "someone took my bag", parse it to a list by its white spaces
Example:
"someone took my bag" -> ["someone","took","my","bag]
"   there are   more spaces than you thought!  " -> ["there","are","more","spaces","than","you","thought!"]

'''
#判断是不是空格
def f(s):
    s1 = s.split(",")
    return s1

s2 = "someone took my bag"
a = f(s2)
print(a)

