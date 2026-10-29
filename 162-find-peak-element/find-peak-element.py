class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        
        start = 0; 
        end = len(nums)-1; 
        mid = start + round((end-start)/2); 

        while start<end:
            #print(start,mid,end)
            mid = start + round((end-start)/2); 

            if nums[mid]>nums[mid+1]:
                if nums[mid]>nums[mid-1]:
                    return mid
                else: 
                    end = mid-1; 
            else:
                start = mid+1;

        return start

