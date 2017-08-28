class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman = s.upper()
        result = 0

        roman = roman[::-1]  # reverse
        pre_num = None
        for i in roman:
            if pre_num == None:
                result += roman_num_map[i]
                pre_num = i
            elif roman_num_map[i] >= roman_num_map[pre_num]:
                result += roman_num_map[i]
                pre_num = i
            else:
                result -= roman_num_map[i]
                pre_num = i
        return result

if __name__ == '__main__':
    s = Solution()
    assert s.romanToInt('MCMLXXX') == 1980, 'Error'
