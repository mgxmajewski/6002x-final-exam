import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np
import itertools



def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    choices_arr = np.array(choices)
    number_of_zeroes = len(choices)
    which = np.array(list(itertools.combinations(range(number_of_zeroes), 2)))
    grid = np.zeros((len(which), number_of_zeroes))

    grid[np.arange(len(which))[None].T, which] = 1

    result = np.array([])
    for combination in range(len(grid)):
        if sum(grid[combination]*choices_arr) == total:
                result = grid[combination]

    new_result = []
    for integer in range(len(result)):
        new_result.append(result[integer])

    final_result = np.array(new_result)

    return final_result.astype(int)



print(find_combination([1,2,2,3],4))

