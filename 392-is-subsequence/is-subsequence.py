class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0; 
        j = 0; 
        counter = 0;
        while i<len(s) and j <len(t):
            c1 = s[i]
            c2 = t[j]; 

            if c1==c2: 
                counter = counter + 1; 

                i = i + 1; 
                j = j + 1; 
            
            else: 
                j = j +1; 
        
        if counter == len(s): 
            return True 
        else: 
            return False