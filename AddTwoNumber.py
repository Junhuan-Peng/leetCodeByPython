'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        link_one, link_two = l1, l2
        result = ListNode(-1)  # 头结点
        result_ptr = result
        temp = 0
        while link_one is not None or link_two is not None:
            if link_one is not None and link_two is not None:
                sum_ = link_one.val + link_two.val + temp
                temp = sum_ // 10
                tempLnode = ListNode(x=(sum_ % 10))
                result_ptr.next = tempLnode
                result_ptr = result_ptr.next
                link_one = link_one.next
                link_two = link_two.next

            elif link_one is not None and link_two is None:
                sum_ = link_one.val + temp
                temp = sum_ / 10
                tempLnode = ListNode(x=(sum_ % 10))
                result_ptr.next = tempLnode
                result_ptr = result_ptr.next
                link_one = link_one.next
                
            elif link_two is not None and link_one is None:
                sum_ = link_two.val + temp
                temp = sum_ / 10
                tempLnode = ListNode(x=(sum_ % 10))
                result_ptr.next = tempLnode
                result_ptr = result_ptr.next
                link_two = link_two.next

        if temp != 0:
            result_ptr.next = ListNode(temp)
        return result.next

if __name__ == '__main__':
    l1 = ListNode(0)
    # l1.next = ListNode(7)
    # l1.next.next = ListNode(3)

    l2 = ListNode(7)
    l2.next = ListNode(3)
    # l2.next.next = ListNode(4)

    s = Solution()
    s.addTwoNumbers(l1,l2)