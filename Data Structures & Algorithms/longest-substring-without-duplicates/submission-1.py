class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        max_len = 0
        # we use set() instead of list because set will be
        seen = set()
        result =0

        # we start looping through the string and each time we are adding new characters to the window
        for right in range(len(s)):
            #only if the characters is in the set
            #if you see the characters in the set,shrink your window
            while s[right] in seen:
                #shrinking the window 
                seen.remove(s[left])
                #growing the window 
                left +=1

            seen.add(s[right])

                #keeping track of the size
            result = max(result, right-left + 1 )
            
        return result





        