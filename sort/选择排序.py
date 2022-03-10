nums = [5,3,6,4,1,2,8,7]
res = []
while len(nums):
    maxIndex = 0
    for i in range(1,len(nums)):
        if nums[maxIndex] < nums[i]:
            maxIndex = i
    temp = nums[maxIndex]
    res.append(temp)
    nums.pop(maxIndex)
print(res)