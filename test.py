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
            return 1 + size_of_group(mat1, row, col + 1) + size_of_group(mat1, row, col - 1) + size_of_group(mat1, row + 1, col) + size_of_group(mat1, - 1, col)
        else:
            return 0
    else:
        return 0


a = [[1, 0, 0, 3, 0], [0, 0, 2, 3, 0], [2, 0, 0, 2, 0], [0, 1, 2, 3, 3]]
print(size_of_group(a, 0, 1))