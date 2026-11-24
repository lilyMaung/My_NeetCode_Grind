class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we are given two strings if two strings have the same frequency of char we return true
        # we will assume there is no edge cases such as white spaces
        if len(s) != len(t):
            return False
        
        # so we have to keep count of the char frequency we will pair each char with their frequency

        ourMap = {}

        for char in s:
                ourMap[char] = ourMap.get(char,0)+1

        for char in t:
            if char not in ourMap:
                return False

            ourMap[char] -=1

            if ourMap[char] < 0:
                return False

        return True    
