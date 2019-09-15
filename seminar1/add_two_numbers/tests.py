import pytest
import add_two_numbers


def test_solution_1():
    l1 = add_two_numbers.ListNode(1)
    l2 = add_two_numbers.ListNode(2)
    l3 = add_two_numbers.ListNode(3)
    l4 = add_two_numbers.ListNode(4)

    l1.next = l2
    l3.next = l4

    s = add_two_numbers.Solution()
    res = s.addTwoNumbers(l1, l3)

    assert res.val == 4
    assert res.next.val == 6
    assert res.next.next == None

def test_solution_2():
    l1 = add_two_numbers.ListNode(5)
    l2 = add_two_numbers.ListNode(2)
    l3 = add_two_numbers.ListNode(7)
    l4 = add_two_numbers.ListNode(4)

    l1.next = l2
    l3.next = l4

    s = add_two_numbers.Solution()
    res = s.addTwoNumbers(l1, l3)

    assert res.val == 2
    assert res.next.val == 7
    assert res.next.next == None

def test_solution_3():
    l1 = add_two_numbers.ListNode(5)
    l2 = add_two_numbers.ListNode(7)
    l3 = add_two_numbers.ListNode(7)
    l4 = add_two_numbers.ListNode(4)

    l1.next = l2
    l3.next = l4

    s = add_two_numbers.Solution()
    res = s.addTwoNumbers(l1, l3)

    assert res.val == 2
    assert res.next.val == 2
    assert res.next.next.val == 1
    assert res.next.next.next == None

def test_solution_4():
    l1 = add_two_numbers.ListNode(5)
    l2 = add_two_numbers.ListNode(7)

    l3 = add_two_numbers.ListNode(7)
    l4 = add_two_numbers.ListNode(4)
    l5 = add_two_numbers.ListNode(4)
    l6 = add_two_numbers.ListNode(4)

    l1.next = l2

    l3.next = l4
    l4.next = l5
    l5.next = l6

    s = add_two_numbers.Solution()
    res = s.addTwoNumbers(l1, l3)

    assert res.val == 2
    assert res.next.val == 2
    assert res.next.next.val == 5
    assert res.next.next.next.val == 4
    assert res.next.next.next.next == None
