# Problem 52:
#     Permuted Multiples
#
# Description:
#     It can be seen that the number, 125874, and its double, 251748,
#       contain exactly the same digits, but in a different order.
#
#     Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def is_permutation(x: int, y: int) -> bool:
    """
    Return True iff `y` is a permutation of the digits of `x`

    Args:
        x (int): Natural number
        y (int): Natural number

    Returns:
        (bool): True iff y is a permutation of x

    Raises:
        AssertError: if incorrect args are given
    """
    return ''.join(sorted(list(str(x)))) == ''.join(sorted(list(str(y))))


def main() -> int:
    """
    Returns the smallest positive integer `x` such that
      the digits of each of the multiples x, 2x, 3x, 4x, 5x, and 6x
      are permutations of each other.

    Returns:
        (int): Smallest number whose first 6 multiples are permutations of each other.
    """
    # Idea:
    #     Consider the desired number `x` based on its `n` digits.
    #
    #     FACTS:
    #       * x = _ ... _ (n digits)
    #       * 10^(n-1) <= x < 10^n
    #
    #       * All multiples (x, ..., 6x) must have the same number of digits,
    #           since they must be permutations of each other.
    #
    #       * x < 10^n / 6,
    #           else 6*x >= 10^n, and so 6*x would have more than n digits.
    #
    #       * First digit of x must be 1
    #
    #       * Must have n >= 6
    #           => Already know from previous fact that x = 1 _ ... _,
    #                and each multiple will differ from the previous by x,
    #                so each next multiple will start with a new greater digit,
    #                thus x must have at least 6 distinct digits
    n = 6
    while True:
        for x in range(10**(n-1), 10**n // 6 + 1):
            good = True
            for i in range(2, 7):
                if not is_permutation(x, i*x):
                    good = False
                    break
            if good:
                return x
        n += 1


if __name__ == '__main__':
    permuted_multiplicand = main()
    print('Smallest multiplicand having permuted multiples:')
    for multiplier in range(1, 7):
        print('  {} × {} = {}'.format(multiplier, permuted_multiplicand, multiplier*permuted_multiplicand))
