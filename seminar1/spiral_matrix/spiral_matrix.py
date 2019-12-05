def spiral_matrix(n):
    if n == 0: return [[]]
    elif n == 1: return [[1]]
    matrix = spiral_matrix(n-2)
    new_matrix = \
           [[n ** 2                                  -  i             for i in range(n)]] \
         + [[n ** 2 + j - 4*(n - 1) + 1] + matrix[j] + [n**2 - n - j] for j in range(n-2)] \
         + [[n ** 2                      - 3*(n - 1) +  i             for i in range(n)]]
    return new_matrix
