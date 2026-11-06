class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prefix = []; 
        suffix = []; 
        p = 1; 
        for n in nums: 
            p = p*n; 
            prefix.append(p);
        p = 1; 

        for i in range(len(nums)-1,-1,-1): 
            p = p * nums[i];

            suffix.append(p)

        print(suffix,prefix)

        output = [0]*len(nums);     
        for j in range(0,len(nums)): 
            if j == 0: 
                output[j] = suffix[len(nums)-2]
            elif j == len(nums)-1: 
                output[j] = prefix[len(nums)-2]
            else:
                output[j] = prefix[j-1]*suffix[len(nums)-j-2]

        return output 
                
        