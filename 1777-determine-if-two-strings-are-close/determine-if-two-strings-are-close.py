class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        def freqword(word):

            freq={};

            for c in word: 
                freq[c] = freq.get(c,0)+1; 
            
            return freq
        
        if len(word1)!=len(word2): 
            return False
        else: 
            if set(word1)!=set(word2): ## operation 1
                return False
            else: 
                #operation 2 - frequencies should remain the same 

                #freq for word1
                freq1 = freqword(word1);
                #freq for word2
                freq2 = freqword(word2);
                print(freq1,freq2)
                lf2 = list(freq2.values())
                lf1 = list(freq1.values())
                lf2.sort()
                lf1.sort()
                print(lf1,lf2)

                if lf1==lf2:
                    return True
                else: 
                    return False
                