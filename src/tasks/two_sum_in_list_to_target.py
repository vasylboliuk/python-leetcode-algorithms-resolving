

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








