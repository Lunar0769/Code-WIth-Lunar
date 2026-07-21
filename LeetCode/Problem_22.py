# 22. Generate Parentheses
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s="("
        e=")"

        res=[]
        def backtrack(s,e,temp):
            if s==0 and e==0:
                res.append(temp)
                return
            if s>0:
                backtrack(s-1,e,temp+"(")
            if e>s:
                backtrack(s,e-1,temp+")")
        
        backtrack(n,n,"")
        return res