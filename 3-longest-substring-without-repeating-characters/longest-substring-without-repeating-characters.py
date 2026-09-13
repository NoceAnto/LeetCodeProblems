class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringset = set(s);
        if len(stringset) <=2:
            print("Stringset less than 2")
            return len(stringset)
        
        if len(stringset) == len(s):
            print("Stringset equal to string length")
            return len(s)

        substring_l_vect = []; 
        for i in range(0,len(s)):
            news = s[i:len(s)];
            seen = set();

            for item in news:
                if item in seen:
                    #print("Duplicate:", item)
                    #print(len(seen))
                    
                    break;

                seen.add(item)
            #print("Iteration:"+str(i)+";Duplicate:"+str(item)+";Substring:"+str(seen))
            substring_l_vect.append(len(seen))

            
        #print(substring_l_vect)
        return max(substring_l_vect)