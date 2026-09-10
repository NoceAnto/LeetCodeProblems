class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum_dict={}; 
        seen = set(); 


        for i in range(0,len(nums)): 

            needed = target-nums[i];

            if needed in seen:
                return [two_sum_dict[needed],i]

            seen.add(nums[i]);
            two_sum_dict[nums[i]] = i; 
            
        