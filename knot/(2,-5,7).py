from sympy import symbols, Eq, linear_eq_to_matrix

x_vars = symbols('x1:15')

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = x_vars

eqs = [
    Eq(2*x7 - x8 - x1, 0),
    Eq(2*x1 - x7 - x2, 0),
    Eq(2*x7 - x9 - x6, 0),
    Eq(2*x6 - x7 - x5, 0),
    Eq(2*x5 - x6 - x4, 0),
    Eq(2*x4 - x5 - x3, 0),
    Eq(2*x3 - x4 - x2, 0),
    Eq(2*x8 - x10 - x9, 0),
    Eq(2*x10 - x11 - x8, 0),
    Eq(2*x11 - x10 - x12, 0),
    Eq(2*x12 - x11 - x13, 0),
    Eq(2*x13 - x12 - x14, 0),
    Eq(2*x14 - x3 - x13, 0),
    Eq(2*x3 - x14 - x1, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)

A_reduced = A[:-1, :-1]

det_reduced = A_reduced.det()

print(det_reduced)
