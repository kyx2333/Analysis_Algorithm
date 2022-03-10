nums = [5,3,6,4,1,2,8,7]
def ShellSort(num):
    step = len(num)//2
    while step > 0:
        for i in range(step,len(num)):
            index = i
            while index - step >= 0 and num[index-step] < num[index]:
                num[index],num[index-step] =num[index-step],num[index]
                index -= step
        step //=2
ShellSort(nums)
print(nums)