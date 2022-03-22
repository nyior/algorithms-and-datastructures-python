class Solution:
    # s = "ohomm"
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        result = 0
        
        for string in s:
            if string not in sub:
                sub.append(string)
                result = max(result, len(sub))
                
            else:
                sub = sub[sub.index(string)+1:]
                sub.append(string)
                
        return result