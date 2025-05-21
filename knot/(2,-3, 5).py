from sympy import symbols, Eq, linear_eq_to_matrix, pprint

x_vars = symbols('x1:11')
x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = x_vars

eqs = [
    Eq(2*x3 - x1 - x2, 0),
    Eq(2*x2 - x3 - x4, 0),
    Eq(2*x3 - x10 - x5, 0),
    Eq(2*x5 - x3 - x6, 0),
    Eq(2*x6 - x5 - x4, 0),
    Eq(2*x6 - x2 - x7, 0),
    Eq(2*x7 - x6 - x8, 0),
    Eq(2*x8 - x7 - x9, 0),
    Eq(2*x9 - x8 - x1, 0),
    Eq(2*x1 - x9 - x10, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)
A_reduced = A[:-1, :-1]
det_reduced = A_reduced.det()

print(det_reduced)
