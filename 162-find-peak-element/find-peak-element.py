class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        N =len(nums);

        if N>=2:
            if nums[0]>nums[1]:
                return 0 
            
            if nums[N-1]>nums[N-2]:
                return N-1
        else:
            return 0
        
        i=0
        while i<N-2:
            
            if nums[i]<nums[i+1] and nums[i+1]>nums[i+2]:
                return i+1
            i=i+1;

