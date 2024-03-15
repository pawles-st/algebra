def div_rem(x, y):
    exact = x / y
    q = round(exact.real) + round(exact.imag) * 1j
    r = x - q * y
    return (q, r)

def gcd(x, y):
    if abs(x) < abs(y):
        x, y = y, x
    while abs(y) > 0:
        x, y = y, div_rem(x, y)[1]
    return x

def lcm(x, y):
    return x * y / gcd(x, y)

print(gcd(complex(3, 4), complex(1, 3)))
print(lcm(complex(3, 4), complex(1, 3)))
