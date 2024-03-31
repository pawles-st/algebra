from itertools import product
import math

#A = [(i, j) for (i, j) in list(product(range(5, 16), range(5, 16))) if (i - 10) ** 2 + (j - 10) ** 2 <= 25]
A = [(i, j) for (i, j) in list(product(range(0, 5), range(-3, 4))) if abs(j) <= 3 * math.sin(i)]

def min_elem(A):
    M = set()
    
    def compare(x, y):
        for (a, b) in zip(x, y):
            if a > b:
                return False
        return True

    for a in A:
        minimum = True
        invalidated = set()
        for m in M:
            if compare(m, a):
                minimum = False
            elif compare(a, m):
                invalidated.add(m)
        if minimum:
            M.add(a)
        M = M - invalidated
    return M

M = min_elem(A)

print(A)
print(M)
