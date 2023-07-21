""" This volume is for the problems from 1 to 50 """

def prob01(top: int = 10, div: list[int] = [3, 5]) -> int:
    """ Problem 1

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    # Note: suppose div always has 2 elements.
    """
    sum = 0
    lcm = div[0] * div[1]  # Least common multiple

    for d in div:
        d_len = (top - 1) // d  # NOT inclusive

        sum += int(d * (1 + d_len) * d_len / 2)
    
    lcm_len = (top - 1) // lcm
    return sum - int(lcm * (1 + lcm_len) * lcm_len / 2)

print(prob01(1000))
