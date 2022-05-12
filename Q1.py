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


