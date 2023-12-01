from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def node_to_list(self, ls: Optional[ListNode]):
        result_list = []
        current_value = ls.val
        while True:
            result_list.append(current_value)
            if ls.next is None:
                break
            ls = ls.next
            current_value = ls.val
        return result_list


    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_reversed = self.node_to_list(l1)[::-1]
        l2_reversed = self.node_to_list(l2)[::-1]

        sum_result = int("".join([str(x) for x in l1_reversed])) + int("".join([str(x) for x in l2_reversed]))

        sum_result_str = str(sum_result)[::-1]
        result_list = [int(i) for i in sum_result_str]

        result_list_node: ListNode = ListNode(result_list[0])
        current_node = result_list_node
        for i in range(1, len(result_list)):
            current_element = result_list[i]
            current_node.next = ListNode(current_element)
            current_node = current_node.next
        return result_list_node


class TestAddNumbersFromReverseList:

    def test_simple_list(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))
        l2 = ListNode(5, ListNode(6, ListNode(4)))
        actual = Solution().addTwoNumbers(l1, l2)
        expected = ListNode(7, ListNode(0, ListNode(8)))
        assert actual == expected

    def test_one_zero_list(self):
        l1 = ListNode(0)
        l2 = ListNode(0)
        assert Solution().addTwoNumbers(l1, l2) == ListNode(0)

    def test_long_list(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
        assert Solution().addTwoNumbers(l1, l2) == \
               ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
