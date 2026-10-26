class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        unique_val_dict = {}

        for a in arr: 
            unique_val_dict[a] = unique_val_dict.get(a,0)+1
        
        
        return len(unique_val_dict.values())==len(set(unique_val_dict.values()))
            