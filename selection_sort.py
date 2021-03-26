def selection_sort(nums):
    l = len(nums)
    #travese all elements in nums
    for i in range(l):
        small = i 
        for j in range(i+1 , l):
            if nums[small] > nums[j]:
                small = j
        nums[i],nums[small] = nums[small],nums[i]
    return nums

lst = [1,4,6,3,7,8,2,9]
a = selection_sort(lst)
print(a)