# PAYPALISHIRING->

# P   A   H   N
# A P L S I I G
# Y   I   R

# PYAIHRN
# APLSIIG

# PAHNAPLSIIGYIR


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        mat = [[] for _ in range(numRows)]
        step = 1
        row = 0
        for c in s:
            if numRows > row >= 0:
                mat[row].append(c)
                row += step
            else:
                step = -step
                row += step
                row += step
                mat[row].append(c)
                row += step
        result = []
        for i in mat:
            result += i
        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    assert s.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR', 'Error 1'
    assert s.convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING', 'Error 2'
    assert s.convert('PAYPALISHIRING', 2) == 'PYAIHRNAPLSIIG', 'Error 3'
