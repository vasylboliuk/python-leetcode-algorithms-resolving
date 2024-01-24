from typing import List

from assertpy import assert_that


class PlusOneSolution:
    def plus_one(self, digits: List[int]) -> List[int]:
        pass



class TestPlusOneSolution:

    def test_plus_one_simple(self):
        input = [1, 2, 3]
        output = PlusOneSolution().plus_one([1, 2, 4])
        assert_that(input).is_equal_to(output)