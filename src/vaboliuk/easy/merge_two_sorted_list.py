from typing import Optional

from assertpy import assert_that


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val}, {self.next}"


class MergeTwoSortedList:
    """
    Task: You are given the heads of two sorted linked lists list1 and list2.
        As a tech I would like to see one merged list.
        The list should be made by splicing together the nodes of the first two lists.
        Note: This is not simple list this is liked list ListNode(val=0, next=None)
    Examples:
        - Input: list1 = [1,2,4], list2 = [1,3,4] Output: [1,1,2,3,4,4]
        - Input: list1 = [], list2 = [] Output: []
        - Input: list1 = [], list2 = [5 Output: [5]
   """

    def list_to_liked_list(self, input_list: list) -> Optional[ListNode]:
        if not input_list:
            return None
        list_node = ListNode(input_list[0], None)
        current_node = list_node
        last_index = len(input_list)
        for i in range(1, last_index):
            current_node.next = ListNode(input_list[i])
            current_node = current_node.next
        return list_node

    def liked_list_to_list(self, liked_list: ListNode) -> list:
        result_list = []
        while liked_list is not None:
            result_list.append(liked_list.val)
            liked_list = liked_list.next
        return result_list

    def merge_two_liked_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_list = []
        temp_list.extend(self.liked_list_to_list(list1))
        temp_list.extend(self.liked_list_to_list(list2))
        temp_list.sort()
        return self.list_to_liked_list(temp_list)


class TestMergeTwoSortedList:
    def test_simple_list(self):
        list_1 = ListNode(1, ListNode(2, ListNode(3)))
        list_2 = ListNode(1, ListNode(3, ListNode(4)))
        output = MergeTwoSortedList().merge_two_liked_lists(list_1, list_2)
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4))))))
        act_list = MergeTwoSortedList().liked_list_to_list(output)
        expected_list = MergeTwoSortedList().liked_list_to_list(expected)
        print(f"\nActual: {act_list}")
        print(f"Expected: {expected_list}")
        assert_that(act_list).is_equal_to(expected_list)

    def test_convert_simple_list_to_node_list(self):
        input_list = [1, 2, 5, 6, 7]
        result = MergeTwoSortedList().list_to_liked_list(input_list)
        print()
        print(result)



