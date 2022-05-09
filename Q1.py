def question1(num):
    """
    Qs1
    """
    # WRITE YOUR CODE HERE!
    i = num // 2

    def sum_of_div(x, y, z=0):
        if x > 0:
            if y % x == 0:
                z += x
                x -= 1
                sum_of_div(x, y, z)
            else:
                pass
        else:
            return z

    div_sum = sum_of_div(i, num)
    if div_sum == num:
        return True
    else:
        return False


question1(67)