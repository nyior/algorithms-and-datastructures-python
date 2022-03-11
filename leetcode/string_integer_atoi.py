"""
input: a string containing either of or combination of: integers, non-integers, '-', '+', and white spaces.

expected output: return 32-bit signed equivalent of the input string
key things:
    -ignore leading white spaces
    -ignore all chars after the last digit in the input string
    - result must be between -2**31 and 2**31+1
    - keep track of the result sign by readng in '-' or the '+' i the input string
    
Example input-output:
'234-' -> -234
'456ghtj8' -. 456


key operation: 
- parse the input string and return the integer equivalent of each digit entry, and ignore all non didgit entreis

simplest version

str = '1'
srt = ' 123 '
str = '123rt'

PSEUDOCODE:
sign = '+'
last_int_index = 0

lower_bound = -(2**31)
upper_bound = (2**31)-1

str = str.strip()

for i in str.length
    try
        if str[i] == '-' or str[i] == '+'
            sign = str[i]
            
        int(str[i])
        last_int_index = i
    except:
        break

str = [:last_int_index]
result = int(str) if sign == '+' else -int(str)

if result >= lowwer_bound and result <= upper_bound:
    return result
elif result < lower_bound:
    return lower_bound
elif result > upper_bound:
    return upper_bound

"""
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = '+'
        last_int_index = 0
        sign_index = None

        lower_bound = -(2**31)
        upper_bound = (2**31)-1

        s = s.strip()
        integer_read = False

        for i in range(len(s)):
            try:
                if s[i] == '-' or s[i] == '+':
                    sign = s[i]
                    sign_index = i
                    continue

                int(s[i])
                last_int_index = i
                integer_read = True
            except:
                break

        s = s[:sign_index] + s[sign_index+1:last_int_index+1]
        
        result = int(s) if integer_read else 0
        
        print(f"sign:{sign}")
        print(f"integer_read:{integer_read}")
        
        if sign == '-' and result !=0:   
            result == -result
            print(f"result-negative: {result}")
        
        # print(f"result: {result}")
        if result >= lower_bound and result <= upper_bound:
            return result
        elif result < lower_bound:
            return lower_bound
        elif result > upper_bound:
            return upper_bound

        