def prediction(lst):
    a = lst[0]
    b = lst[1]
    c = lst[2]
    function = a * abs(b) - ((a + b) * c)
    return function


all_equations = [[2,-5,7], [4,-3,7], [2,-5,5], [2,-3,5], [2,-5,11], [3,-3,1], [2,-3,7]]

for equation in all_equations:
    print(f"(+{equation[0]}, {equation[1]}, +{equation[2]}) = {prediction(equation)}")