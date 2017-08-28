# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# The brackets must close in the correct order,
#  "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        stack = []
        char_map = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if char_map[i] == stack[-1]:
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False
