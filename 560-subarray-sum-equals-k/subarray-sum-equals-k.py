class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0;

        mydict = {}
        cum_sum = 0;
        for i in range(0,len(nums)): #O(n)
            cum_sum = cum_sum + nums[i];  #O(1)
            if cum_sum-k in mydict.keys(): #O(1) #CHECK IF DIFFERENCE BETWEEN CUMULATIVE SUM is FINE
                output = output + mydict[cum_sum-k]  #O(1)
                
            if cum_sum in mydict.keys(): #O(1) #SAVE CUMULATIVE SUM
                mydict[cum_sum] =  mydict[cum_sum] + 1; 
            else: 
                mydict[cum_sum] = 1;

        if k in mydict.keys(): #O(1)
            return  output + mydict[k]
        else: 
            return output 
