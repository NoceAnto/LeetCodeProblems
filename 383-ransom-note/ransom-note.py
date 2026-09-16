class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        for c in ransomNote: 
            isthere = False; 
            #print("Selected character in ransomNote:"+str(c))

            if c not in magazine: 
                return False
            else: 
                newmagazine = "";
                firsttime = False; 
                for i in range(0,len(magazine)): 

                    if c == magazine[i] and not(firsttime): 
                        newmagazine += "";
                        firsttime = True; 
                    else:
                        newmagazine+=magazine[i]
                
                magazine = newmagazine; 
                #print(magazine)
                
        
        return True
                
