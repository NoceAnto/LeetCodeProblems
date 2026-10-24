class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prefixsum = [nums[0]];
        sufixsum = [nums[len(nums)-1]];

        for i in range(1,len(nums)):

            prefixsum.append(prefixsum[-1]*nums[i]);
            sufixsum.append(sufixsum[-1]*nums[len(nums)-1-i]);
        print(prefixsum,sufixsum)

        output = []; 

        for k in range(0,len(nums)):
            if k == 0:
                output.append(sufixsum[len(nums)-2])
            elif k == len(nums)-1:
                output.append(prefixsum[len(nums)-2])
            else:
                output.append(prefixsum[k-1]*sufixsum[len(nums)-2-k])

        return output 

            