class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '{':'}','[':']'}

        stack = []

        # if it's open bracket then its going in the stack

        # if the s's length is odd it is invalid
        if len(s) % 2 != 0:
            return False
        
        # if not then we start looping through the string char by char

        
        for char in s: 
            if char in pairs:
                # we have to check if it's empty or does not have a value in the stack
                stack.append(char)
            else:
                if not stack or pairs[stack.pop()]!=char:
                    return False
            
        return not stack






