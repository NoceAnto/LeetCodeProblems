class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        
        def backtrack(current, indices): 

            if len(current) == len(nums): 
                output.append(current)
                return None 

            seen = set();
            
            for i in range(0,len(indices)):
                index = indices[i];  
                newindices = indices[0:i]+indices[i+1:len(indices)]; 
                #print(index,indices,newindices,current)

                if nums[index] not in seen: 
                    backtrack(current+[nums[index]],newindices)
                    seen.add(nums[index])

            return None
    
        allindices = list(range(0,len(nums)))
        #print(allindices)
        output = []
        backtrack([],allindices)

        return output 