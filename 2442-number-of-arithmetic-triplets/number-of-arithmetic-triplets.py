class Solution:
    def binarysearch(self,nums: list[int], target: int) -> bool:
        low,high = 0,len(nums)-1

        while low<=high: 
            
            mid = low + (high-low)//2;
            if nums[mid] == target: 
                return True
            
            if nums[mid]<target: 
                low = mid+1; 
            else: 
                high = mid-1; 

        return False


    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        
        output = 0; 

        for num in nums: 
            if self.binarysearch(nums,num+diff) and self.binarysearch(nums,num+2*diff):
                output +=1


        return output 
