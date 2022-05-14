def question3_a(mat, indices, epidemic):
    """
    Qs3a
    """
    # WRITE YOUR CODE HERE!
    row1 = int(indices[0])
    col1 = int(indices[1])

    def epidemic_spread(mak, row, col, num):
        """

        :param mak:
        :param row:
        :param col:
        :param num:
        :return:
        """
        if mak[row][col] == 0:
            if col < len(mak[0])-1 and mak[row][col+1] == 0:
                mak[row][col] = num
                epidemic_spread(mak, row, col + 1, num)
            else:
                mak[row][col] = num
            if col > 0 and mak[row][col - 1] == 0:
                mak[row][col] = num
                epidemic_spread(mak, row, col - 1, num)
            else:
                mak[row][col] = num
            if row < len(mak)-1 and mak[row + 1][col] == 0:
                mak[row][col] = num
                epidemic_spread(mak, row + 1, col, num)
            else:
                mak[row][col] = num
            if row > 1 and mak[row - 1][col] == 0:
                mak[row][col] = num
                epidemic_spread(mak, row - 1, col, num)
        else:
            mak[row][col] = num

    epidemic_spread(mat, row1, col1, epidemic)


a = [[1, 0, 0, 3, 0], [0, 0, 2, 3, 0], [2, 0, 0, 2, 0], [0, 1, 2, 3, 3]]
question3_a(a, (0, 1), 3)
print(a)
