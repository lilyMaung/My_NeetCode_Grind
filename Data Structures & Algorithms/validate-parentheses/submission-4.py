class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #understanding the problem 
        #if we have something like  <[({})]>
        #first we are going to loop through the string
        #if opening bracket, push it to the stack, if it's closing bracket, pop it
        #the only four paranthesis that we have
        pairs = { "}":"{", ">":"<",")":"(", "]":"[" }

        #looping through the string by char
        for char in s:
            if char in pairs:
                #we will see if the stack is empty or not and that the one that you pop from the stack has a value in the pairs, if there isn't then false, else treu
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                    stack.append(char)

            
        return not stack
            

