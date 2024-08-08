# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return


if __name__ == "__main__":
    l10, l20 = [2,4,3], [5,6,4]
    l11, l21 = [0], [0]
    l12, l22 = [9,9,9,9,9,9,9],[9,9,9,9]
    print(Solution().addTwoNumbers(l10, l20))
    print(Solution().addTwoNumbers(l11, l21))
    print(Solution().addTwoNumbers(l12, l22))
