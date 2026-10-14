class Solution:
    def isValid(self, s: str) -> bool:
        # push the brackets into the stack
        # hold all the brackets in a dictionary 

        stack = [] #empty stack
        bracket_dict = { ")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                #before poping check if stack is empty
                if not stack or stack[-1] != bracket_dict[c]: #the last element of the stack is not in bracket_dict[key] then cannot pop and therefore is not balanced
                    return False

                stack.pop()
            
        #return true only if the stack is empty after poping out all the brackets in the order they match in the bracket_dict
        return len(stack) == 0
        