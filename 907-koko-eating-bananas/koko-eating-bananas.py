class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        maxspeed = max(piles);

        start = 1; 
        end = max(piles); 

        minspeed = end; 

        while start<=end: 

            speed = start + round((end-start)/2);
            #print(start,end,speed)

            counter = 0; 
            for p in piles: 
                if speed!=1:
                    counter = counter + floor(p/speed) + min(p%speed,1);
                    #print(counter)
                else: 
                    counter = counter + p; 

            if counter <= h: 
                if minspeed>speed: 
                    minspeed = speed; 
            if counter > h: 
                start = speed+1; 
            else: 
                end = speed-1; 

        return minspeed




