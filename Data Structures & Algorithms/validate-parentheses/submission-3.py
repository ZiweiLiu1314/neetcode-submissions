class Solution:
    def isValid(self, s: str) -> bool:
        # (), [], {}, every one is closed correctly without redundency
        # correct order: filo, stack, []
        # use stack a track them, and if the stack is empty in the end, it's valid 
        # one pass through s, O(n)
        # left = set(["(", "[", "{"])
        right2left = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in range(len(s)):
            if s[i] in right2left: # the right side 
                if not stack or right2left[s[i]] != stack.pop(): 
                    return False 
            else: # the left side 
                stack.append(s[i])
        if stack: 
            return False 
        else: 
            return True 

