class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        output = [];
        def backtrack(current,remaining):

            if remaining==0:
                output.append(current)
                return None 
            

            for digit in nums: 
                if digit not in current:
                    backtrack(current+[digit],remaining-1)

        
        backtrack([],len(nums))


        return output
