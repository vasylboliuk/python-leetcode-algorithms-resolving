

class TwoSumInListToTargetSolution:

    @staticmethod
    def two_sum(input_list, target):
        result = []
        for index in range(len(input_list)):
            first_num = input_list[index]
            for y in range(index+1, len(input_list)):
                second_num = input_list[y]
                sum_nums = first_num + second_num
                if sum_nums == target:
                    result.append(index)
                    result.append(y)
                    return result


class TestTwoSumInListToTargetSolution:

    def test_in_first_indexes(self):
        input_data = [2, 4, 5, 8]
        target = 6
        output = TwoSumInListToTargetSolution.two_sum(input_data, target)
        expected = [0, 1]  # index of 1 and 2. 1+2=3
        assert output == expected

    def test_in_last_indexes(self):
        input_data = [2, 4, 3, 1]
        target = 4
        output = TwoSumInListToTargetSolution.two_sum(input_data, target)
        expected = [2, 3]  # index of 3 and 1. 3+1=4
        assert output == expected

    def test_in_diff_indexes_position(self):
        input_data = [3, 2, 3]
        target = 6
        output = TwoSumInListToTargetSolution.two_sum(input_data, target)
        expected = [0, 2]
        assert output == expected








