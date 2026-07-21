class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        start = "({["
        end = ")}]"
        pairs = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in start:
                stack.append(char)
            elif char in end:
                if not stack:
                    return False
                last = stack.pop()
                if pairs.get(last) != char:
                    return False
        return not stack