from sympy import symbols, Eq, linear_eq_to_matrix, pprint

x_vars = symbols('x1:13')
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = x_vars

eqs = [
    Eq(2*x5 - x1 - x12, 0),
    Eq(2*x12 - x5 - x6, 0),
    Eq(2*x5 - x8 - x7, 0),
    Eq(2*x7 - x5 - x4, 0),
    Eq(2*x4 - x7 - x6, 0),
    Eq(2*x1 - x9 - x8, 0),
    Eq(2*x9 - x1 - x2, 0),
    Eq(2*x2 - x9 - x10, 0),
    Eq(2*x10 - x2 - x3, 0),
    Eq(2*x3 - x10 - x11, 0),
    Eq(2*x11 - x3 - x4, 0),
    Eq(2*x4 - x11 - x12, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)
A_reduced = A[:-1, :-1]
det_reduced = A_reduced.det()

print(det_reduced)
