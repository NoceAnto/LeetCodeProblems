class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = float('inf');
        second = float('inf')

        for x in nums: 
            #print(x)
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


            

            
            
            

