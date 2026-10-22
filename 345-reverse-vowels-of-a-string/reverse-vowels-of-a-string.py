class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = set(["a","e","i","o","u","A","E","I","O","U"]); 

        i=0; 
        j = len(s)-1;

        while i<j:
            #print(i,j)

            if s[i] in vowels and s[j] in vowels: 
                s = s[0:i]+s[j]+s[i+1:j]+s[i]+s[j+1:len(s)]
                #print(s)
                j= j-1;
                i = i+1;

            if s[i] in vowels and s[j] not in vowels:
                j = j -1; 
            
            if s[i] not in vowels and s[j] in vowels:
                i = i +1; 
            
            if s[i] not in vowels and s[j] not in vowels:
                i = i + 1; 
                j = j - 1;

        return s


        
        return s
