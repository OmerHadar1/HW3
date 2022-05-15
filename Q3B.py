def question3_b(mat):
    """
    Qs3b
    """
    # WRITE YOUR CODE HERE!
    def size_of_group(mat1, row, col):
        """

        :param mat1:
        :param row:
        :param col:
        :param num:
        :return:
        """
        if len(mat1[0]) > col > -1 and len(mat1) > row > -1:
            if mat1[row][col] == 0:
                mat1[row][col] = 1
                return 1 + size_of_group(mat1, row, col + 1) + size_of_group(mat1, row, col - 1) + size_of_group(mat1, row + 1,col) + size_of_group( mat1, - 1, col)
            else:
                return 0
        else:
            return 0

    def find_max_group(mat2, row2, col2, count=0):
        if row2 == len(mat2):
            return count
        if col2 == len(mat2[0]):
            if size_of_group(mat2, row2, col2) > count:
                count = size_of_group(mat2, row2, col2)
                return count, find_max_group(mat2, row2+1, 0, count)
        else:
            if size_of_group(mat2, row2, col2) > count:
                count = size_of_group(mat2, row2, col2)
                return count, find_max_group(mat2, row2, col2+1, count)

    return find_max_group(mat, 0, 0)


a = [[1, 0, 0, 3, 0], [0, 0, 2, 3, 0], [2, 0, 0, 2, 0], [0, 1, 2, 3, 3]]
print(question3_b(a, 0, 1))





















