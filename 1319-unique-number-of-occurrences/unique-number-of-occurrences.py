class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        unique_val_dict = {}

        for a in arr: 
            if a in unique_val_dict.keys():
                unique_val_dict[a]+=1; 
            else: 
                unique_val_dict[a]=0; 
        
        
        return len(unique_val_dict.values())==len(set(unique_val_dict.values()))
            