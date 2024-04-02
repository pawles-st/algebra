from itertools import zip_longest

def div_rem(x, y):
    dividend = x.copy()
    dividend_deg = len(dividend) + 1
    divisor = y.copy()
    divisor_deg = len(divisor) + 1
    quotient = []
    while dividend_deg >= divisor_deg:
        #if not divisor[-1] == 0:
        subtrahend = [0] * (dividend_deg - divisor_deg) + divisor.copy()
        coefficient = dividend[-1] / subtrahend[-1]
        quotient.insert(0, coefficient)
        dividend = [a - coefficient * b for a, b in zip(dividend, subtrahend)]
        dividend.pop()
        dividend_deg -= 1
    if quotient == []:
        quotient = [0]
    return (quotient, dividend)

def ext_gcd(x, y):
    if len(y) == 0 or y == [0]:
        return (x, [1], [0])
    else:
        (q, r) = div_rem(x, y)
        (d, a, b) = ext_gcd(y, r)
        new_a = b
        new_b = [a - v for a, v in zip_longest(a, multiply(b, q), fillvalue = 0)]
        return (d, new_a, new_b)

def multiply(x, y):
    result = [0] * (len(x) + len(y) - 1)
    for (deg, value) in enumerate(y):
        addend = [0] * deg + x.copy()
        result = [a + value * b for a, b in zip_longest(result, addend, fillvalue = 0)]
    return result

print(ext_gcd([1, 0, 1], [1, 2, 1]))
print(ext_gcd([1, 6, -7], [2, -2, 0, -4]))
