class Solution:
    def romanToInt(self, s: str) -> int:
        
        output = 0; 
        i = 0;

        while i <len(s):
            if s[i] == "M":
                #print("index "+str(i)+" M so sum 1000")
                output = output + 1000; 
                i = i +1
                continue; 
            
            if s[i:i+2] == "CM":
                #print("CM so sum 900")
                output = output + 900; 
                i = i +2
                continue; 
            
            if s[i] == "D":
                output = output + 500; 
                i = i +1
                continue; 
            
            if s[i:i+2] == "CD":
                output = output + 400; 
                i = i +2
                continue; 
            
            if s[i] == "C":
                output = output + 100; 
                i = i +1
                continue; 
            
            if s[i:i+2] == "XC":
                print("XC so sum 90")

                output = output + 90; 
                i = i +2
                continue; 
            
            if s[i] == "L":
                output = output + 50; 
                i = i +1
                continue;
            
            if s[i:i+2] == "XL":
                output = output + 40; 
                i = i +2
                continue;

            if s[i] == "X":
                output = output + 10; 
                i = i +1
                continue;

            if s[i:i+2] == "IX":
                output = output + 9; 
                i = i +2
                continue;

            if s[i:i+2] == "IV":
                output = output + 4; 
                i = i +2
                continue;

            if s[i] == "V":
                output = output + 5; 
                i = i +1
                continue;
            
            if s[i] == "I":
                output = output + 1; 
                i = i +1
                continue;
        
        return output 