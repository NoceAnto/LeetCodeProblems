class Solution:
    def binarysearch(self,nums: list[int], target: int,low:int) -> bool:
        high = len(nums)-1
        if nums[high] == target: 
            return True

        while low<=high: 
            
            mid = low + (high-low)//2;
            #print(low,high,mid,nums[mid],target)

            if nums[mid] == target: 
                return True
            
            if nums[mid]<target: 
                low = mid+1; 
            else: 
                high = mid-1; 

        return False


    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        
        output = 0; 
        N = len(nums)
        for i in range(0,N): 
            num = nums[i]
            if self.binarysearch(nums,num+diff,i+1) and self.binarysearch(nums,num+2*diff,i+1):
                #print(nums[i])
                output +=1


        return output 
