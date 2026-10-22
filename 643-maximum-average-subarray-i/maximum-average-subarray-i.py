class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        i=0; 
        j = i+k; 
        ma = sum(nums[i:j]); 

        temp= ma;
        while j<len(nums):
            #print(i,j,nums[i],nums[j],temp,ma)
            temp = temp - nums[i] + nums[j]
            if temp > ma: 
                ma = temp;
            i = i + 1; 
            j = j + 1;
            
        
        return ma/k