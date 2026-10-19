class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = 0; 
        j =0;
        output = "";

        while i<len(word1) and j<len(word2): 
            
            if i==j:
                output = output + word1[i]; 
                i = i +1; 
            
            if i>j: 
                output = output + word2[j]; 
                j = j +1; 
            print(i,j,output)


        if j<len(word2):
            output = output + word2[j:len(word2)]
            #print(word2[j:len(word2)],output)
        if i<len(word1):
            output = output + word1[i:len(word1)]


        return output 




