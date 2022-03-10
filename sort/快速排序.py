nums = [5,3,6,4,1,2,8,7]
def QuickSort(num):
    if len(num)<=1 :
        return num
    key = num[0]
    L_list, R_list ,mid_list = [],[],[key]
    for i in range(1,len(num)):
        if num[i] > key:
            L_list.append(num[i])
        else :
            R_list.append(num[i])
    return QuickSort(L_list) + mid_list + QuickSort(R_list)

print(QuickSort(nums))

#快速排序空间优化采用双指针
def optimize_sort(num,left,right):
    if left >= right:
        return
    l,r,key = left,right,num[left]
    while l < r:
        while l < r and num[r] >= key:
            r -= 1
        num[l] = num[r]
        while l < r and num[l] < key:
            l += 1
        num[r] = num[l]
    num[l] = key
    optimize_sort(num,left,l-1)
    optimize_sort(num,r+1,right)

optimize_sort(nums,0,len(nums)-1)
print(nums)