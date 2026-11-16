class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        while front < back:
            #this is skipping the non alphabets
            while front < back and not s[front].isalnum():
                front +=1
            while front < back and not s[back].isalnum():
                back -=1

            #now checking the lower cases
            if s[front].lower() != s[back].lower():
                return False

            front +=1
            back -=1
        return True
            