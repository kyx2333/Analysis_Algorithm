nums = [5,3,6,4,1,2,8,7]
for i in range(len(nums),0,-1):
    for j in range(i-1):
        if nums[j+1] > nums[j]:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp
print(nums)
