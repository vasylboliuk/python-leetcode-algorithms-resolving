from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def add_two_numbers(l1: list, l2: list) -> list:
        l1_reversed = l1[::-1]
        l2_reversed = l2[::-1]

        sum_result = int("".join([str(x) for x in l1_reversed])) + int("".join([str(x) for x in l2_reversed]))

        sum_result_str = str(sum_result)[::-1]
        result_list = [int(i) for i in sum_result_str]
        return result_list


class TestAddNumbersFromReverseList:

    def test_simple_list(self):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        assert Solution.add_two_numbers(l1, l2) == [7, 0, 8]

    def test_one_zero_list(self):
        l1 = [0]
        l2 = [0]
        assert Solution.add_two_numbers(l1, l2) == [0]

    def test_long_list(self):
        l1 = [9,9,9,9,9,9,9]
        l2 = [9,9,9,9]
        assert Solution.add_two_numbers(l1, l2) == [8,9,9,9,0,0,0,1]
