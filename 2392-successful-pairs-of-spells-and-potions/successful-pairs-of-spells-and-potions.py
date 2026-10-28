class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:

        def findpotion(potions,success,spell): 
            low = 0;
            high = len(potions)-1; 
            good_pi = [];
            while low<=high: 
                pi = low + round((high-low)/2); 
                #print(f"This are low,medium and high: {low},{pi},{high}")
                p = potions[pi]; 
                #print(f"The potion value at medium pos is: {p}")
                if p*spell>=success:
                    good_pi.append(pi)
                    high = pi-1; 
                else: 
                    low = pi+1; 

            #print(good_pi)
            if len(good_pi)==0:
                return len(potions)
            else:
                return min(good_pi)
        
        ans = [0]*len(spells); 

        # sort potions 
        potions.sort()

        for i,s in enumerate(spells): 
            # find the potions with least strength that gives success
            ans[i] = ans[i] + len(potions)-findpotion(potions,success,s)

        return ans