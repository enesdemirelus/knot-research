from sympy import symbols, Eq, linear_eq_to_matrix

x_vars = symbols('x1:9')
x1, x2, x3, x4, x5, x6, x7, x8 = x_vars

eqs = [
    Eq(2*x2 - x1 - x3, 0),
    Eq(2*x3 - x2 - x4, 0),
    Eq(2*x2 - x7 - x6, 0),
    Eq(2*x6 - x2 - x5, 0),
    Eq(2*x5 - x6 - x4, 0),
    Eq(2*x1 - x7 - x8, 0),
    Eq(2*x8 - x1 - x5, 0),
    Eq(2*x5 - x8 - x3, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)
A_reduced = A[:-1, :-1]
det_reduced = A_reduced.det()

print(det_reduced)
