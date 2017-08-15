# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_string = ''
        maxLength = len(sub_string)
        for i in s:
            if i not in sub_string:
                # 如果i不在子串中，则将i添加到子串中
                sub_string += i
                maxLength = len(sub_string) if len(sub_string) > maxLength else maxLength
            else:
                # 如果在
                index = sub_string.find(i)
                sub_string = sub_string[index+1:len(sub_string)] + i
                maxLength = len(sub_string) if len(sub_string) > maxLength else maxLength
        print('maxLength is {maxLength}'.format(maxLength=maxLength))
        return maxLength


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3, 'abcabcbb is 3'
    assert s.lengthOfLongestSubstring('bbbbb') == 1, 'bbbbb is 1'
    assert s.lengthOfLongestSubstring('pwwkew') == 3, 'pwwkew is 3'
    assert s.lengthOfLongestSubstring("nfpdmpi") == 5, 'nfpdmpi is 5'

