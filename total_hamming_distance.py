class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        length = len(nums)
        nums = [self.int2binaryStr(i)[::-1] for i in nums]
        for i in range(32):
            temp = 0
            for j in nums:
                temp += int(j[i])
            result += temp * (length - temp)
        return result

    def int2binaryStr(self, num):
        num_bin = bin(num)[2:]
        num_add_len = 32 - len(num_bin)
        for i in range(num_add_len):
            num_bin = '0' + num_bin
        return num_bin


if __name__ == '__main__':
    s = Solution()
    assert s.totalHammingDistance([4, 14, 2]) == 6, 'Error'
