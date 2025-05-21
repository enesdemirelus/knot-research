from sympy import symbols, Eq, linear_eq_to_matrix, pprint

x_vars = symbols('x1:19')
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18 = x_vars

eqs = [
    Eq(2*x2 - x1 - x3, 0),
    Eq(2*x3 - x2 - x4, 0),
    Eq(2*x2 - x6 - x7, 0),
    Eq(2*x7 - x2 - x8, 0),
    Eq(2*x8 - x7 - x9, 0),
    Eq(2*x9 - x8 - x5, 0),
    Eq(2*x5 - x4 - x9, 0),
    Eq(2*x1 - x6 - x10, 0),
    Eq(2*x10 - x1 - x11, 0),
    Eq(2*x11 - x10 - x12, 0),
    Eq(2*x12 - x11 - x13, 0),
    Eq(2*x13 - x12 - x14, 0),
    Eq(2*x14 - x13 - x15, 0),
    Eq(2*x15 - x14 - x16, 0),
    Eq(2*x16 - x15 - x17, 0),
    Eq(2*x17 - x16 - x18, 0),
    Eq(2*x18 - x17 - x5, 0),
    Eq(2*x5 - x18 - x3, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)
A_reduced = A[:-1, :-1]
det_reduced = A_reduced.det()

print(det_reduced)
