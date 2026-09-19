class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()#O(logn)
        output = sum(nums[0:3]);

        for i in range(0,len(nums)): # fix a number 

            j = i+1; 
            k = len(nums)-1; 
            while j < k: 
                thisoutput = nums[i] + nums[j] + nums[k];

                if abs(thisoutput-target) < abs(output-target):
                    output = thisoutput; 

                if target-thisoutput == 0:
                    return target

                if target-thisoutput<0:
                    k=k-1; #smaller values 
                if target-thisoutput>0:
                    j=j+1; # greater values 
                           
        return output 
