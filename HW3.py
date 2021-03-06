def question1(num):
    """
    Qs1
    """
    # WRITE YOUR CODE HERE!
    def sum_of_div(main_num, div):
        if div == 1:
            return div
        elif div > 1:
            if main_num % div == 0:
                return sum_of_div(main_num, div-1) + div
            else:
                return sum_of_div(main_num, div-1)

    return sum_of_div(num, num // 2) == num


def question2(lst, x):
    """
    Qs2
    """
    # WRITE YOUR CODE HERE!


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

def question3_b(mat):
    """
    Qs3b
    """
    # WRITE YOUR CODE HERE!


