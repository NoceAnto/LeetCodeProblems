class Solution:
    def compress(self,chars: list[str]) -> int:
    
        read = 0; 
        write = 0;
        counter = 0; 

        while read<len(chars): 
            c = chars[read]
            #print(f"Read character {c} at position {read}")
            #print("... checking repetitions")

            while read<len(chars):
                if c == chars[read]:
                    counter = counter+1; 
                    read = read +1; 
                else: 
                    break; 

            #print(f"There are {counter} repetitions of character {c}")
            
            if counter > 1:
                chars[write] = c; 
                #print(f"Write character {c} at position {write}")

                write = write + 1; 
                for nc in list(str(counter)): 
                    chars[write] = nc; 
                    #print(f"Write character {nc} at position {write}")
                    write = write +1; 
            
            if counter == 1: 
                chars[write] = c; 
                #print(f"Write character {c} at position {write}")
                write = write +1; 
            
            counter = 0; 
            #print(read,write)

        #while write < len(chars): 
        #    chars.pop(write)
        #    write = write + 1

        return write
                 
                         
