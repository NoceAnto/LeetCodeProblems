class Solution:
    def maxArea(self, height: list[int]) -> int:
        i=0; 
        j = len(height)-1; 

        ma = 0; 

        while i<j: 
            print(i,j,len(height),ma)

            h1 = height[i]; 
            h2 = height[j]; 

            maxAreatemp = min(h1,h2)*(j-i); 
            if maxAreatemp>ma: 
                ma = maxAreatemp; 

            if h1<h2: 
                i=i+1; 
            if h2<h1: 
                j=j-1; 
            
            if h1==h2: 
                i=i+1; 
                j=j-1; 
        
        return ma
