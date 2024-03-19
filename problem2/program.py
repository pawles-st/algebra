from itertools import zip_longest

def div_rem(x, y):
    dividend = x.copy()
    dividend_deg = len(dividend) + 1
    divisor = y.copy()
    divisor_deg = len(divisor) + 1
    quotient = []
    while dividend_deg >= divisor_deg:
        subtrahend = [0] * (dividend_deg - divisor_deg) + divisor.copy()
        coefficient = dividend[-1] / subtrahend[-1]
        quotient.insert(0, coefficient)
        dividend = [a - b for a, b in zip(dividend, subtrahend)]
        dividend.pop()
        dividend_deg -= 1
    return (quotient, dividend)

def gcd(x, y):
    if len(x) < len(y):
        x, y = y, x
    while len(y) > 0:
        x, y = y, div_rem(x, y)[1]
    return x

def multiply(x, y):
    result = [0] * (len(x) + len(y) - 1)
    for (deg, value) in enumerate(y):
        addend = [0] * deg + x.copy()
        result = [a + value * b for a, b in zip_longest(result, addend, fillvalue = 0)]
    return result

def lcm(x, y):
    return div_rem(multiply(x, y), gcd(x, y))[0]

print(gcd([1, 0, 1], [1, 2, 1]))
print(lcm([1, 0, 1], [1, 2, 1]))


            

