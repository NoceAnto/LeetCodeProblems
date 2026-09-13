class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        steps = 0; 

        def backtrack(current,steps):

            if current == 0:
                return steps 
            
            if current%2 == 0:
                steps = backtrack(current/2,steps+1)
            else: 
                steps = backtrack(current-1,steps+1)
            
            return steps
        
        steps = backtrack(num,0)


        
        return steps
                