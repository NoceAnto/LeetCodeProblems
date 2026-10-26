class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        uniques_val = set(arr); 

        unique_val_dict = {}

        for a in uniques_val: 
            unique_val_dict[a]=0;
        
        for a in arr: 
            unique_val_dict[a]+=1; 
        
        seen = set(); 

        for k in unique_val_dict.keys(): 
            if unique_val_dict[k] in seen: 
                return False
            else: 
                seen.add(unique_val_dict[k])

        return True
            