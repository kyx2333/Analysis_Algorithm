# 方法1 元素范围确定
count = [0]*51
nums,result = [1,1,3,19,35,49,50,5,10,16],[]
for i in nums:
    count[i] += 1
for i in range(1,len(count)):
    if count[i]:
        result += [i]*count[i];
print(result)

# 方法2 元素范围不确定
nums,result = [19,21,23,14,35,49,37,59,10,16],[]
min,max = min(nums),max(nums)
count = [0]*(max-min+1)
for i in nums:
    count[i-min] += 1
for i in range(1,len(count)):
    if count[i]:
        result += [i+min]*count[i]
print(result)