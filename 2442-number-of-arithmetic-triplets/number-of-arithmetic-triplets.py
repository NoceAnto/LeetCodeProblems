class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        
        output = 0; 
        N = len(nums);
        for i in range(0,N-2): 

            firstnum = nums[i]; 
            #print(set(nums[i+1:N]))
            if firstnum+diff in set(nums[i+1:N]) and firstnum+2*diff in set(nums[i+1:N]): 
                output = output + 1; 


        return output 
