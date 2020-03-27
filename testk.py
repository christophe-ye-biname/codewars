def calc(expr):
    # TODO: Your awesome code here
    arr = 0
    expr = list(' '.join(expr))
    return expr,type(expr)


print(calc("5 1 2 + 4 * + 3 -"))
print(calc("3.5 7 + 8 +")) #18.5