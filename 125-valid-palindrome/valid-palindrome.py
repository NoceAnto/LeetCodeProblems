class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        listcharacters = s.lower(); 
        i = 0;
        j = len(listcharacters)-1;
        while i<=j:
            #print(listcharacters[i],listcharacters[j])


            if listcharacters[i].isalnum() and listcharacters[j].isalnum(): 
                if  listcharacters[i] == listcharacters[j]: 
                    i+=1
                    j-=1
                else: 
                    return False 

            elif not(listcharacters[i].isalnum()): 
                i = i +1; 
            else: 
                j = j -1;
                

        return True 
            
            

