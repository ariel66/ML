def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

nums = [23,46,75,12,3,45,66,32]
a = bubble_sort(nums)
print(a)

