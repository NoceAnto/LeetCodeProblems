class Solution:
    def reverseWords(self, s: str) -> str:
        
        first_index = [];
        last_index = []; 
        if s[0]!=' ': 
            first_index.append(0)
        
        # O(n)
        for i in range(1,len(s)):

            if s[i-1]== ' ' and s[i]!=' ': 
                first_index.append(i)

            if s[i-1]!=' ' and s[i]==' ': 
                last_index.append(i)
        if s[len(s)-1]!=' ': 
            last_index.append(len(s))
        
        #print(first_index)
        #print(last_index)

        output = "";
        for j in range(0,len(last_index)): 
            output = output + s[first_index[len(last_index)-j-1]:last_index[len(last_index)-j-1]] +" ";
        
        return output[0:-1]
            

        

