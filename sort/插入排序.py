nums = [5,3,6,4,1,2,8,7]
for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] >nums[j]:
            ins  = nums[i];
            nums.pop(i);
            nums.insert(j,ins);
            break;
print(nums)
