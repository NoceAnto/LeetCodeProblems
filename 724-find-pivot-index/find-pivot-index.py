class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        

        prefixsum = [0];
        sufixsum = [0];
        N = len(nums);
        #print(N)

        for i in range(0,N):
            prefixsum.append(prefixsum[-1]+nums[i]);
            sufixsum.append(sufixsum[-1]+nums[N-1-i]);
        #print(prefixsum,sufixsum)

        for j in range(0,N):
            #print(j, prefixsum[j],sufixsum[N-1-j])
            if prefixsum[j]==sufixsum[N-1-j]:
                return j
        

        return -1