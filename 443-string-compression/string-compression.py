class Solution:
    def compress(self,chars: list[str]) -> int:
        i=0; 
        s = "";

        def num2chars(n):
            ans = []; 
            while n >0:
                ans.insert(0,n%10)
                n = n//10; 
            
            return ans 

        counter = 0; 

        while i<len(chars):
            
            c = chars[i]; 
            j = i;
            #print(f"Index i {i} has char {c}")
            #print("checking for multiple")
            while j<len(chars):
                if c == chars[j]:
                    chars.pop(j)
                    counter = counter+1; 
                    #j=j+1;
                else: 
                    print('w')
                    break; 

            #print(f"there are {counter} repetitions of {c}")
            
            if counter == 1: 
                s = s + str(c); 
                chars.insert(i,c)

                i = i +1; 
            
            if counter>1: 
                s = s +str(c)+str(counter); 
                chars.insert(i,c)
                i=i+1;

                numchars = num2chars(counter); 

                for k in numchars:
                    chars.insert(i,str(k))
                    i = i +1;

            #print("chars: "+str(chars))
            #print("compressed string: "+s)
            counter = 0; 

        return len(s)