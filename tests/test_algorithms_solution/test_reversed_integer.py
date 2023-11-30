from src.tasks.reversed_integer import ReversedIntegerSolution


class TestReversedIntegerSolution:

    def test_positive_number(self):
        assert ReversedIntegerSolution.reverse(123) == 321

    def test_negative_number(self):
        assert ReversedIntegerSolution.reverse(-123) == -321

    def test_zero_end_number(self):
        assert ReversedIntegerSolution.reverse(120) == 21

    def test_big_int_number(self):
        """
        -2**31 <= x <= 2**31 - 1
        """
        assert ReversedIntegerSolution.reverse(1534236469) == 0


