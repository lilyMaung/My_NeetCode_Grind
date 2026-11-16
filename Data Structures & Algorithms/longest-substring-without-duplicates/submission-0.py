class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we have to go through the string
        #let's just say the string is "abcabcbb"

        left = 0
        seen = set()
        max_len = 0

        #we looping through the string 
        for right in range(len(s)):
            #Shrink: while the character is already in our window
            while s[right] in seen:
                seen.remove(s[left])
                #then the left move forward
                left +=1

            #Grow: add the new character to our window
            seen.add(s[right])

            #Track: update the answer if this window is the biggest so far
            max_len = max(max_len, right - left + 1)

        return max_len
        

       

    
