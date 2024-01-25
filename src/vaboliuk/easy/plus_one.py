from typing import List

from assertpy import assert_that


class PlusOneSolution:
    """
    Task: You are given a large integer in array digits, where each digits[i] is the ith digit of the integer.
        Increment the large integer by one and return the resulting array of digits.
        Example: input list:
          - [1, 2, 3] -> [1, 2, 4]
          - [1, 2, 9] -> [1, 3, 0]
        But rules are:
            - 1 <= digits.length <= 100
    """

    def plus_one_solution_1(self, digits: List[int]) -> List[int]:
        item_str = "".join([str(i) for i in digits])
        result_str = str(int(item_str) + 1)
        result_list = [int(i) for i in result_str]
        return result_list

    def plus_one_solution_2(self, digits: List[int]) -> List[int]:
        inc = 1
        for i in range(len(digits) - 1, -1, -1):
            elm = digits[i] + inc
            if elm < 10:
                digits[i] = elm
                return digits
            else:
                digits[i] = 0
        digits = [1] + digits
        return digits


class TestPlusOneSolution1:

    def test_plus_one_simple(self):
        input_data = [1, 2, 3]
        output = PlusOneSolution().plus_one_solution_1(input_data)
        expected = [1, 2, 4]
        print(input_data)
        print(output)
        assert_that(output).is_equal_to(expected)

    def test_plus_one_nine_in_end(self):
        input_data = [1, 2, 9]
        output = PlusOneSolution().plus_one_solution_1(input_data)
        expected = [1, 3, 0]
        print(input_data)
        print(output)
        assert_that(output).is_equal_to(expected)


class TestPlusOneSolution2:

    def test_plus_one_simple(self):
        input_data = [1, 2, 3]
        output = PlusOneSolution().plus_one_solution_2(input_data)
        expected = [1, 2, 4]
        print(input_data)
        print(output)
        assert_that(output).is_equal_to(expected)

    def test_plus_one_nine_in_end(self):
        input_data = [1, 2, 9]
        output = PlusOneSolution().plus_one_solution_2(input_data)
        expected = [1, 3, 0]
        print(input_data)
        print(output)
        assert_that(output).is_equal_to(expected)

    def test_plus_all_nines(self):
        input_data = [9, 9, 9]
        output = PlusOneSolution().plus_one_solution_2(input_data)
        expected = [1, 0, 0, 0]
        print(input_data)
        print(output)
        assert_that(output).is_equal_to(expected)
