class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_dict ={}; 

        i = 0; 
        for s in strs:

            key = "".join(sorted(s)); 

            if key in anagram_dict.keys(): 
                anagram_dict[key].append(s)
            else: 
                anagram_dict[key] = [s]; 



            i = i +1; 

        return list(anagram_dict.values())