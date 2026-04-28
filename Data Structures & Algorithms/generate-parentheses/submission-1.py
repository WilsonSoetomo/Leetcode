class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(open_c, close_c):
            if open_c == close_c == n:
                res.append("".join(stack))
            
            if open_c < n:
                stack.append("(")
                backtrack(open_c + 1, close_c)
                stack.pop()
            
            if close_c < open_c:
                stack.append(")")
                backtrack(open_c, close_c + 1)
                stack.pop()
                

        backtrack(0, 0)
        return res

