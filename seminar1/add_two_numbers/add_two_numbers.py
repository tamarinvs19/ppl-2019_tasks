class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = ListNode(0)
        l3 = start
        c = 0
        while l1 != None or l2 != None:
            a = l1.val if l1 != None else 0
            b = l2.val if l2 != None else 0
            s = a + b + c

            l3.next = ListNode(s % 10)
            c = s // 10

            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
            l3 = l3.next

        if c != 0:
            l3.next = ListNode(c)
        
        return start.next

