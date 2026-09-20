class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        
        output = 0; 
        N = len(nums);

        seen = set();
        for i in range(0,N): 

            lastnum = nums[i]; 
            
            if lastnum-diff in seen and lastnum-2*diff in seen: 
                output = output +1; 

            seen.add(lastnum)


        return output 
