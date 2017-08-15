class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """





    def isPalindromic(self, s):
        """
        :param s: a string
        :return: True is s is a palindromic string
        :rtype: bool
        """

        head, tail = 0, len(s) - 1
        while True:
            if head > tail:
                break
            else:
                if s[head] == s[tail]:
                    head += 1
                    tail -= 1
                else:
                    return False
        return True
