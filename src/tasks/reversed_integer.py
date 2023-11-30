

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











