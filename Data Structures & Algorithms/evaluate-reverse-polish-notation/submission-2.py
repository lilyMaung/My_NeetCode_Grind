class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # we are given the operators and numbers 
        # we have to read through the token one by one 
        #if it's number we push it to the stack and we see an operator then we pop off and perform those two numbers and push it back into the stack
        ourStack = []

        for num in tokens:
            if num == "+" :
                num1 = ourStack.pop()
                num2 = ourStack.pop()
                ourSum =num1 + num2
                ourStack.append(ourSum)
            
            elif num == "-" :
                num1 = ourStack.pop()
                num2 =ourStack.pop()
                ourStack.append(num2 - num1)
            elif num == "*" :
                num1 = ourStack.pop()
                num2 = ourStack.pop()
                ourStack.append(num2 * num1)
            elif num =="/":
                num1 = ourStack.pop()
                num2 =ourStack.pop()
                ourSub = int(num2 / num1)
                ourStack.append(ourSub)
            else:
                ourStack.append(int(num))
            
        return ourStack[0]

            

        
        