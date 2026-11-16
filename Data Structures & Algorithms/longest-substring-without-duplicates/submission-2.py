class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #left = 0
    #for right in range(len(s)):
     #   add s[right] to the window
    #while window is invalid:
    #    remove s[left]; left += 1
    #update the answer

        # the goal is to find the longest substring that we can get  without repeating any characters
        
    # we are using set so that we don't have any duplicates
        ourSet = set()
        left=best=0

        for right in range(len(s)):
            while s[right] in ourSet:
                ourSet.remove(s[left])
                left+=1
            
            ourSet.add(s[right])

            best = max(best, right-left+1)
        return best
