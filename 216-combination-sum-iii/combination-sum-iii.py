class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        output = []; 
        def backtrack(current,currentk):

            if sum(current)==n and currentk==0: 
                output.append(current[1:len(current)])
            if sum(current)>n:
                return None
            if sum(current)==n and currentk>0:
                return None
            
            if currentk>0:
                for i in range(1,10):
                    if i not in current and i>current[-1]:
                        backtrack(current+[i],currentk-1)
            else:
                return None
        
        backtrack([0],k)

        return output 
