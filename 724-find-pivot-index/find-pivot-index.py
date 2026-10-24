class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        
        prefixsum = [0];
        N = len(nums);
        #print(N)

        for i in range(0,N):
            prefixsum.append(prefixsum[-1]+nums[i]);

        for j in range(0,N):

            if (prefixsum[-1]-nums[j])/2 == prefixsum[j]:
                return j
        

        return -1