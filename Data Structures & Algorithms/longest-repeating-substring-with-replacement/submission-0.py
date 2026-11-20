class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #MAIN IDEA- whenever we start the window we have to ch

        left = 0
        answer = 0

        ourMap = {}

        #looping through the string
        for right in range(len(s)):

            #first we have to count character we see in the window and get the character with the most frequency

            ourMap[s[right]] = ourMap.get(s[right],0) + 1

            # now we have to start our window to be valid

            while (right - left + 1) - max(ourMap.values()) > k:
                # then we have to drop the left and its count and move forward
                ourMap[s[left]] -=1

                left +=1
            
            #we also have to keep track of the longest window that is valid
            answer = max(answer, right - left + 1)
        
        return answer





    
        