# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]

        x_add_len = 31 - len(x_bin)
        y_add_len = 31 - len(y_bin)

        for i in range(x_add_len):
            x_bin = '0' + x_bin
        for i in range(y_add_len):
            y_bin = '0' + y_bin
        result = 0
        for i in range(31):
            if x_bin[i] != y_bin[i]:
                result += 1
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.hammingDistance(1, 4) == 2, '2!Something error'
