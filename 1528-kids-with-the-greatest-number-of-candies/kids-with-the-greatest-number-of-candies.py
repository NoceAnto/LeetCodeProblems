class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        
        output = []

        for i in range(0,len(candies)): 
            candies[i] = candies[i]+extraCandies 
            if max(candies) == candies[i]: 
                output.append(True)
            else:
                output.append(False)
            candies[i] = candies[i]-extraCandies 

        return output 