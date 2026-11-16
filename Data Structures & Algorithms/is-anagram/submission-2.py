class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #even though we could use brute force which would be going through each string and keeping counts and sorting and comparing them which would be O(n log n)
        #we can use hash map to keep track of our frequencies so that it could be optimized to O(n)

        #created a hash map
        myMap = {}

        #to save trouble 
        if len(s) != len(t):
            return False

        #after that we loop through the first string
        for char in s:
            #if it's in the map already then it's incremented

            myMap[char] = myMap.get(char, 0) +1

        #now we have all the characters of s string in the hashmap
        #so all we need to do is compare with t string

        for char in t:
            #if characters in t are not in the hashmap
            if char not in myMap:
                return False
            #if it's in the character we need to keep count of the characters
            myMap[char] -=1

            if myMap[char] <0:
                return False

        return True
             

        
    
