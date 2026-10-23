class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        i = 0; 
        j = len(nums)-1; 
        counter = 0; 
        nums.sort()

        while i < j: 

            if nums[i]+nums[j] == k: 
                counter+=1; 
                i = i+1; 
                j = j-1; 
            
            if nums[i]+nums[j]>k: 
                j = j-1; 
            
            if nums[i]+nums[j]<k:
                i = i+1; 

    
        return counter 
            
        