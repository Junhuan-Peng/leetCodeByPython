class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # target = nums[i] + nums[j]
        length = len(nums)
        values = {}
        for j in range(length):
            values[nums[j]] = j

        for i in range(length):
            num_1 = nums[i]  # nums[i]
            num_2 = target - num_1  # 找到一个值为num_2的数组元素
            try:
                x = values[num_2]
                if i == x:
                    continue
                return [i, x]
            except Exception as e:
                continue

if __name__ == '__main__':
    s = Solution()
    a = [3,2,4]
    target = 6
    print(s.twoSum(a,target=target))