from sympy import Symbol, Poly


def int2base(decimal, base):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    other_base = ''

    while decimal != 0:
        other_base = alphabet[decimal % base] + other_base
        decimal = decimal / base

    return other_base


def poly_from_int(i, base):
    present_exponents = {}
    i_str = int2base(i, base)[::-1]

    for j in range(0, len(i_str)):
        if i_str[j] != '0':
            present_exponents[(j,)] = int(i_str[j])

    return Poly(present_exponents, Symbol('x'), modulus=base)
