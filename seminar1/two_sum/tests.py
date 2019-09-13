import pytest
from two_sum import *


def test_contains_1():
    nums = [1, 2, 3, 4]
    assert contains(nums, 2) == 1

def test_contains_2():
    nums = [1, 2, 50, 400]
    assert contains(nums, 3) == -1

def test_contains_3():
    nums = [1, 2, 50, 400]
    assert contains(nums, 1) == 0

def test_contains_4():
    nums = [1, 2, 50, 400]
    assert contains(nums, 400) == 3

def test_contains_5():
    nums = []
    assert contains(nums, 400) == -1

def test_sorted():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    output = two_sum_with_one_solution(nums, target)
    assert output == expected

def test_not_sorted():
    nums = [2, -7, 11, 15]
    target = 4
    expected = [1, 2]
    output = two_sum_with_one_solution(nums, target)
    assert output == expected

def test_without_solving():
    nums = [2, -7, 11, 15]
    target = 1
    assert two_sum_with_one_solution(nums, target) == False

def test_with_repetition():
    nums = [2, -7, 11, 15]
    target = 22
    assert two_sum_with_one_solution(nums, target) == False

def test_sorted_twice():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    output = two_sum_with_repetition(nums, target)
    assert output == expected

def test_not_sorted_twice():
    nums = [2, -7, 11, 15]
    target = 26
    expected = [2, 3]
    output = two_sum_with_repetition(nums, target)
    assert output == expected

def test_without_solving_twice():
    nums = [2, -7, 11, 15]
    target = 1
    assert two_sum_with_repetition(nums, target) == False

def test_with_repetition_twice():
    nums = [2, -7, 11, 15]
    target = 22
    assert two_sum_with_repetition(nums, target) == [2, 2]


