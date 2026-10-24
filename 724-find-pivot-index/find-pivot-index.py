class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        prefixsum = [0];
        N = len(nums);
        allsum = sum(nums);

        for j in range(0,N):
            prefixsum.append(prefixsum[-1]+nums[j]);

            if (allsum-nums[j])/2 == prefixsum[j]:
                return j
        

        return -1