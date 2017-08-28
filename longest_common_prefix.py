class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        theShortestLength = len(min(strs))
        for i in range(theShortestLength):
            s = set()
            for string in strs:
                s.add(string[i])
            if len(s) > 1:
                return strs[0][:i ]
        else:
            return strs[0][:theShortestLength]

if __name__ == '__main__':
    strs = ['qwerr','qwe33','qwe22']
    s = Solution()
    print(s.longestCommonPrefix(strs))