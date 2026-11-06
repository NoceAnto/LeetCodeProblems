class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {};

        for i,n in enumerate(nums): 
            if target-n in seen.keys():
                return [i,seen[target-n]]
            else:
                seen[n] = i
