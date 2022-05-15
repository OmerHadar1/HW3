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
        if mat1[row][col] == 0:
            if col < len(mat1[0])-1 and mat1[row][col + 1] == 0:
                mat3 = mat1[:]
                mat3[row][col] = 1
                return 1 + size_of_group(mat3, row, col + 1,)
            elif col > 0 and mat1[row][col - 1] == 0:
                mat3 = mat1[:]
                mat3[row][col] = 1
                return 1 + size_of_group(mat3, row, col - 1,)
            elif row < len(mat1)-1 and mat1[row + 1][col] == 0:
                mat3 = mat1[:]
                mat3[row][col] = 1
                return 1 + size_of_group(mat3, row + 1, col,)
            elif row > 1 and mat1[row - 1][col] == 0:
                mat3 = mat1[:]
                mat3[row][col] = 1
                return 1 + size_of_group(mat3, - 1, col,)
        else:
            return 0

    def find_max_group(mat2, row2, col2, count=0):
        if row2 == len(mat2):
            return count
        if col2 == len(mat2[0]):
            if size_of_group(mat2, row2, col2) > count:
                count = size_of_group(mat2, row2, col2)
                return find_max_group(mat2, row2+1, 0, count)
        else:
            if size_of_group(mat2, row2, col2) > count:
                count = size_of_group(mat2, row2, col2)
                return find_max_group(mat2, row2, col2+1)

    return find_max_group(mat, 0, 0)





















