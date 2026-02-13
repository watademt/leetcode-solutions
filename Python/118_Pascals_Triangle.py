# https://leetcode.com/problems/pascals-triangle/
# Сложность: Easy
# Тема: Dynamic Programming / Array Construction

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]

        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(len(prev_row) - 1):
                # Сумма двух элементов "сверху"
                summa = prev_row[j] + prev_row[j + 1]
                new_row.append(summa)

            new_row.append(1)
            triangle.append(new_row)

        return triangle