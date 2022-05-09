def question1(num):
    """
    Qs1
    """
    # WRITE YOUR CODE HERE!
    def is_num_per(main_num, div, sum_of_div):
        if sum_of_div == main_num:
            return True
        else:
            if div > 1:
                if main_num % div == 0:
                    sum_of_div += div
                    is_num_per(main_num, div - 1, sum_of_div)
                else:
                    is_num_per(main_num, div - 1, sum_of_div)
            elif div == 1:
                sum_of_div += div

    return is_num_per(num, num // 2, 0),
print(question1(6))