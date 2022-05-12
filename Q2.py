def question2(lst, x):
    """
    Qs2
    """
    # WRITE YOUR CODE HERE!

    def subset_sub(lst1, main_num):
        """
        this is a recursive function that solve the subset sum problem.
        the function will break up the list to sub lists until empty list.
        each time it will check if the length of the list equal to the number, if not the function will call it's self
        and subtract the first number in the list form the main number. if at the end of the recursion the main number
        will not be equal to zero the function will return zero and if it does it will return 1. at the last row of the
        code, we'll have a combination between the two calls and at the ens of the recursion we'll get the number of the
        ways we can combine the main number from the number in the list
        :param lst1: a list of numbers
        :param main_num: the combination number we check
        :return: the number of ways we can combine the main number from the numbers in the list
        """
        if len(lst1) == 0:
            if main_num == 0:
                return 1
            else:
                return 0
        else:
            return subset_sub(lst1[1:], main_num) + subset_sub(lst1[1:], main_num - lst1[0])

    return subset_sub(lst, x)


print(question2([7, 6, 1, 20, 1], 14))