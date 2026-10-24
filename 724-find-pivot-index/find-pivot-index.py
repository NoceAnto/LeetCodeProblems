class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        prefixsum = 0;
        N = len(nums);
        allsum = sum(nums);

        for j in range(0,N):
            
            if (allsum-nums[j])/2 == prefixsum:
                return j
            prefixsum = prefixsum +nums[j];

        

        return -1