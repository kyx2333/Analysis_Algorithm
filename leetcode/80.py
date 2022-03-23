class Solution:
    def removeDuplicates(self, nums) -> int:
        for i in range(0,len(nums)):
            while i<len(nums)-1 and nums[i] !=nums[i+1]:
                i += 1
            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                if j< len(nums)-1 and nums[j+1] == nums[i]:
                    nums = nums[:j] +nums[j+1:]
                    #print(nums)
                else:
                    j += 1

            i = j
        print(nums)
        return len(nums)

s = Solution()
s.removeDuplicates([1,1,1,1,1,2])