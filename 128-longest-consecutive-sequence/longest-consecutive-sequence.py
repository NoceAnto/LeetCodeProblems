class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: 
           return 0 
        nums.sort() #O(nlog(n))
        output = 1;
        maxoutput = 1; 
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] +1: 
                output = output +1; 
                if maxoutput < output: 
                    maxoutput = output;
            else: 
                if nums[i] == nums[i-1]:
                    continue;
                else:
                    output = 1;

        
        return maxoutput 