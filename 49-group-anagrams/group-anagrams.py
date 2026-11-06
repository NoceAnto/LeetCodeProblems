class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        group_anagram_dict = {}; 

        for i,s in enumerate(strs): 
            sorteds = "".join(sorted(s))

            if sorteds in group_anagram_dict.keys():
                group_anagram_dict[sorteds].append(s)
            else: 
                group_anagram_dict[sorteds] = [s]; 


        output = [""]*len(group_anagram_dict.keys())
        j = 0; 
        for k in group_anagram_dict.keys(): 
            output[j] = group_anagram_dict[k];
            j = j +1; 

        return output 