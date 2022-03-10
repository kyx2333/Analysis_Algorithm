nums = [59,43,35,34,31,20,10,8,9,22,11,17,12,3,5]
def rise_up(start,end):
    parent = start
    child = parent * 2
    while child <= end :
        if child+1 <= end and nums[child+1] > nums[child]:
            child += 1
        if nums[parent] < nums[child]:
            nums[parent],nums[child] = nums[child],nums[parent]
            parent = child
            child = parent * 2
        else:
            return
def heap_init():
    nums.insert(0,0)
    for i in range((len(nums)-1)//2,0,-1):
        rise_up(i,len(nums)-1)
def heap_sort():
    for i in range(len(nums)-1,0,-1):
        nums[1],nums[i] = nums[i],nums[1]
        rise_up(1,i-1)
heap_init()
heap_sort()
print(nums)
