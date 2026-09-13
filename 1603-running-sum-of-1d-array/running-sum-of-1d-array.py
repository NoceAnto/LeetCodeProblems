class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:


        runningsum = 0; 
        output = []; 

        for n in nums: 
            runningsum = runningsum + n; 
            output.append(runningsum)

        return output 
        