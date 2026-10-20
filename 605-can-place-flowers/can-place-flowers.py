class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        counter = 0; 

        if len(flowerbed) == 1: 
            if flowerbed[0] == 0: 
                counter = counter + 1; 
            
            if counter >= n: 
                return True
            else: 
                return False


        isprevious_empty = True; 
        for i in range(0,len(flowerbed)-1): 
            print(i,flowerbed[i],isprevious_empty)

            if flowerbed[i] == 0 and isprevious_empty and flowerbed[i+1]==0: 
                print("Before is empty, after is empty, let's add 1")
                counter = counter + 1; 
                isprevious_empty = False; 
                continue; 
            if flowerbed[i] == 0 and not(isprevious_empty): 
                print("Before is not empty, this is empty")
                isprevious_empty = True; 
                print("... so is previous empty? True")
                continue; 
            if flowerbed[i] == 1: 
                isprevious_empty = False; 
                continue; 

        if len(flowerbed)>2 and flowerbed[-2] == 0 and flowerbed[-1] ==0 and isprevious_empty:
            counter = counter + 1; 

        if counter >= n: 
            return True 
        else: 
            return False