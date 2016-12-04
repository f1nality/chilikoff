from sympy import Poly, div
from helpers import poly_from_int, int2base

base = 2
expression = Poly('x**2 + 1', modulus=base)

# enumerate polynomials
enumerate_from = '010'
enumerate_to = '111'
digits = len(enumerate_to)

for i in range(int(enumerate_from, base), int(enumerate_to, base) + 1):
    print(int2base(i, base).rjust(digits, '0'))

    divider = poly_from_int(i, base)
    q, r = div(expression.as_expr(), divider.as_expr(), modulus=base)

    if r != 0:
        continue

    print('%s - OK' % divider)
