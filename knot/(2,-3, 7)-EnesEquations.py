from sympy import symbols, Eq, linear_eq_to_matrix, pprint

x_vars = symbols('x1:13')

x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12 = x_vars

eqs = [
    Eq(2*x3 - x1 - x2, 0),
    Eq(2*x2 - x3 - x4, 0),
    Eq(2*x3 - x10 - x5, 0),
    Eq(2*x5 - x3 - x6, 0),
    Eq(2*x6 - x5 - x4, 0),
    Eq(2*x1 - x10 - x12, 0),
    Eq(2*x12 - x11 - x1, 0),
    Eq(2*x11 - x9 - x12, 0),
    Eq(2*x9 - x8 - x11, 0),
    Eq(2*x8 - x7 - x9, 0),
    Eq(2*x7 - x8 - x6, 0),
    Eq(2*x6 - x7 - x2, 0)
]

A, B = linear_eq_to_matrix(eqs, x_vars)

A_reduced = A[:-1, :-1]

pprint(A_reduced.det())
