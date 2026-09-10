class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        two_sum_dict={}; 
        #seen = set(); 


        for i in range(0,len(nums)): 

            if target-nums[i] in two_sum_dict.keys():
                return [two_sum_dict[target-nums[i]],i]

            #seen.add(nums[i]);
            two_sum_dict[nums[i]] = i; 

        