class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = []; 

        def backtrack(current,startindex): 
            output.append(current)

            for i in range(startindex,len(nums)): 
                backtrack(current+[nums[i]],i+1)

            return None 

        
        backtrack([],0)

        return output 
            
            


            