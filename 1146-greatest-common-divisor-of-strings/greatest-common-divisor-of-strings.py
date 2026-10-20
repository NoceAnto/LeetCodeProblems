class Solution:
    
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            #print(a,b)
            while b != 0:
                a, b = b, a % b
                #print(a,b)

            return abs(a)

        def find_divisors(n): 
            divisors = []; 
            for i in range(1,round(n**0.5)+1): 
                if n%i == 0:
                    divisors.append(i)

            divisors.append(n)

            return divisors

        def check_stringGCD(word,word_gcd): 
            l = len(word_gcd)
            print("WORD: "+word)
            if len(word)>len(word_gcd):
                for i in range(0,len(word)-l,l): 
                    print(word[i:i+l], word[i+l:i+2*l])
                    if word[i:i+l] != word[i+l:i+2*l]: 
                        return False
            else: 
                if word!=word_gcd: 
                    return False
                
            return True

        L2 = len(str2); 
        L1 = len(str1); 

        print("Strings lengths:"+str(L1)+", "+str(L2))

        # find GCD of length

        if L2>L1: 
            gcd_l = gcd(L2,L1); 
        else: 
            gcd_l = gcd(L1,L2);

        print("Maximum gcd string length: "+str(gcd_l))


        # the length of the GCD string is at maximum gcd_l or a divisor

        possibile_string_l = find_divisors(gcd_l); 
        print(possibile_string_l)
   
        for j in range(0,len(possibile_string_l)): 
            l = possibile_string_l[len(possibile_string_l)-j-1]
            print("Iteration "+str(j)+", string length "+str(l))

            if str1[0:l] == str2[0:l]:
                temp_gcd = str1[0:l];
                print("Temp gcd "+temp_gcd)
                ### check it 
                if check_stringGCD(str1,temp_gcd) and check_stringGCD(str2,temp_gcd):
                    return temp_gcd 
                

            else: 
                temp_gcd = ""; 
        
        return ""
               