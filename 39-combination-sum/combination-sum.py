class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []; 

        candidates.sort(reverse=True)
        #seen_candidates = set()

        def backtrack(current):
            #print(sum(current),current,target)
            if (sum(current) == target): 
                    output.append(current) 
                    
                    return None     
            if sum(current)>target: 
                return None

            if sum(current)<target:
                for digit in candidates: 
                    if sum(current)==0:
                        if target-sum(current)>=digit:
                            
                            backtrack(current+[digit])
                    if sum(current)>0 and current[-1]>=digit:
                        if target-sum(current)>=digit:
                            
                            backtrack(current+[digit])
        
        backtrack([])


        return output 
