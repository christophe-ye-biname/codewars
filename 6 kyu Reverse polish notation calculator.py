import operator

def calc1(expr):
    # TODO: Your awesome code here
    op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res = [0]
    for token in expr.split(' '):
        if token in op:
            res.pop()
            res.pop()
            res.append(op[token](op1, op2))
        elif token:
            res.append(float(token))
    return res.pop()

print(calc1("5 1 2 + 4 * + 3 -"))