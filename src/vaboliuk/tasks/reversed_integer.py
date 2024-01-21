

class ReversedIntegerSolution:

    @staticmethod
    def reverse(x: int):
        result = 0
        number_str = str(x)
        if x > 0:
            reverse_num = number_str[::-1]
            result = int(reverse_num)
        elif x < 0:
            reverse_num = number_str[::-1]
            result = int('-' + reverse_num[:-1])
        if result > 2**31 - 1 or result < -2**31:
            return 0
        return result


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
