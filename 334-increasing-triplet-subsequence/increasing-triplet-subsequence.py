class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = nums[0]; 
        secondfound = False; 

        for i in range(1,len(nums)): 

            temp = nums[i];

            if temp<first: 
                first = temp; 
            
            if not(secondfound): 
                if temp>first: 
                    second = temp; 
                    secondfound = True; 
            else: 
                if temp>first and temp<second: 
                    second = temp;  

                if temp>first and temp>second:
                    return True


             

        

        return False


            

            
            
            

