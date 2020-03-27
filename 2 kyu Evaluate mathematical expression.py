def calc(expression):
    ###########################################
    def evaluate(string):
        first = {
        '*' : lambda x, y : x*y,
        '/' : lambda x, y : x/y
        
        }
        second = {
            '+' : lambda x, y : x+y,
            '-' : lambda x, y : x-y
        }


        
        i = 0
        while i < len(string):
            if string[i] in first:
                temp = first[string[i]](float(string[i-1]), float(string[i+1]))
                string = string[:i-1] + [str(temp)] + string[i+2:]
                i = 0
            i += 1
        i = 0
        while i < len(string):
            if string[i] in second:
                temp = second[string[i]](float(string[i-1]), float(string[i+1]))
                string = string[:i-1] + [str(temp)] + string[i+2:]
                i = 0
            i += 1
        return ''.join(string)
    #################################################
    def spli(str):
        tab = []
        op = ['*','/','+','-']
        count = 1
        for i in range(len(str)):
            if str[i] in op:
                count += 2

        for i in range(count):
            tab.append("")
        count = 0
        for i in range(len(str)):
            if str[i] not in op:
                tab[count] += str[i]
            else:
                count += 1
                tab[count] += str[i]
                count += 1
        return tab
    ##################################################
    expression = expression.replace(' ', '')
    print(expression)
    i = 0
    while i < len(expression) - 1:
        if expression[i] == '-' and expression[i+1] == '-':
            expression = expression.replace(expression[i] + expression[i+1], '+')
            i = 0
        elif (expression[i] == '+' and expression[i+1] == '-') or (expression[i] == '-' and expression[i+1] == '+'):
            expression = expression.replace(expression[i] + expression[i+1], '-')
            i = 0
        i += 1
    openPar = 0
    closePar = 0
    while '(' in expression:
        i = 0
        while i < len(expression):
            if expression[i] == '(':
                openPar = i
            elif  expression[i] == ')':
                closePar = i
                break
            i += 1
        temp = evaluate(spli(expression[openPar+1:closePar]))
        expression = expression[0:openPar] + temp + expression[closePar+1:] 
    return expression
    

print(calc("(((10))))"))
print(calc("10- 2- -5"))
print(calc("-7 * -(6 / 3)"))
"""
 ["1 + 1", 2],
    ["8/16", 0.5],
    ["3 -(-1)", 4],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["-7 * -(6 / 3)", 14]
"""