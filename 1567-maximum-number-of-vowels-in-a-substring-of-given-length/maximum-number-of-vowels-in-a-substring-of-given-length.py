class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        sum_v = 0; 
        vowels = set(["a","e","i","o","u"]);
        sum_vector = []; 

        for n in range(0,k):
            if s[n] in vowels:
                sum_v+=1; 
        sum_vector.append(sum_v)
        i = k; 
        while i<len(s): 

            if s[i-k] in vowels: 
                sum_v-=1; 
            if s[i] in vowels: 
                sum_v+=1; 
            
            if sum_v == k: 
                return k 
            
            sum_vector.append(sum_v)
            i = i +1;

            
            
        return max(sum_vector)