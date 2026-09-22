class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        output = []

        candidates.sort()

        if sum(candidates)<target:
            return output

        def backtrack(current,startindex): 
            seen = set();
            if sum(current)==target: 
                output.append(current)
                return None 
            if sum(current)>target:
                return None
            
            for i in range(startindex,len(candidates)):
                if candidates[i] not in seen: 
                    backtrack(current+[candidates[i]],i+1)
                    seen.add(candidates[i])



        backtrack([],0)

        #check if output is already present 

        return output 