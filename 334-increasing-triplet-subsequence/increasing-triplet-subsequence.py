class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf');
        second = float('inf')
        secondfound = False; 

        for i in range(0,len(nums)): 

            x = nums[i];
            print(x)
            if x <= first:
                first = x
                #print(f"{x} first ")
            elif x <= second:
                second = x
                #print(f"{x} second ")
            else:
                #print(f"{x} third ")
                return True


             

        

        return False


            

            
            
            

