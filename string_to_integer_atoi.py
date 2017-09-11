import re


class Solution(object):
    def myAtoi(self, string):
        """
        :type string: str
        :rtype: int
        """

        if len(string) == 0:
            return 0
        pattern = re.compile('(?ims)[\D]*?(?P<number>[-|+]?\d*).*?')
        answer = pattern.findall(string)
        if len(answer) == 0:
            return 0
        else:
            for i in answer:
                if len(i) == 0:
                    continue
                else:
                    try:
                        result = int(i)
                        index = string.find(i)
                        if string[index] == '+' and index - 1 >= 0 and string[index - 1] == '-':
                            return 0
                        if string[index] == '-' and index - 1 >= 0 and string[index - 1] == '+':
                            return 0
                        if result >= 2 ** 31:
                            return 2 ** 31 - 1
                        if result <= -(2 ** 31):
                            return -(2 ** 31)
                        return result
                    except Exception as _:
                        pass
            else:
                return 0


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('wer 334') == 334, 'Error 334'
    assert s.myAtoi('') == 0, 'Error 0'
    assert s.myAtoi('w5r6 2') == 5, 'Error 5'
    assert s.myAtoi('-5') == -5, 'Error -5'
    assert s.myAtoi('ascr-8adsa45') == -8, 'Error -8'
    assert s.myAtoi('+-2') == 0, 'Error 0'
    assert s.myAtoi("2147483648") == 2147483647, 'Error 2147483647'
