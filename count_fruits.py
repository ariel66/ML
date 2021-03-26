'''
14. Given a list of strings which representing number of fruits, 
like ["Apple 4", ...] , find the fruit with total maxium count
Example:
["3 Apple", "1 Orange", "4 Pear","5 Apple","2 Pear"] 
-> "Apple"  #Coz there are 8 apples in total
'''
def f(n):
    n1 = []
    dict1 = {}
    for i in n:
        n1.append(i.split(' '))
    for kv in n1:
        if kv[1] not in dict1:
            dict1[kv[1]] = int(kv[0])
        else:
            dict1[kv[1]] += int(kv[0])
    maxValue = 0
    maxKey = ''
    for k, v in dict1.items():
        if v > maxValue:
            maxValue = v
            maxKey = k
    return maxKey
    

nums = ["3 Apple", "1 Orange", "4 Pear","5 Apple","2 Pear"]
a = f(nums)
print(a)